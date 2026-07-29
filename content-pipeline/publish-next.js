#!/usr/bin/env node
/**
 * Publishes the next pending article from content-pipeline/queue/.
 *
 * Runs unattended from GitHub Actions on a cron schedule. Does NOT need a Claude
 * session, the ThinkPad, or any LLM at run time — articles are written ahead of
 * time into the queue, this script just puts the next one live and wires it in.
 *
 * Steps per run:
 *   1. pick the first pending entry in queue.json
 *   2. move its HTML from queue/ to the real target path
 *   3. add it to sitemap.xml
 *   4. if it's a blog post, add the card + BlogPosting JSON-LD to blog/index.html
 *   5. mark it published in queue.json and topics.json
 *   6. ping IndexNow (best effort — never fails the run)
 *
 * Committing/pushing is left to the workflow so this stays testable locally.
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.resolve(__dirname, '..');
const QUEUE_DIR = path.join(__dirname, 'queue');
const QUEUE_JSON = path.join(__dirname, 'queue.json');
const TOPICS_JSON = path.join(__dirname, 'topics.json');
const SITEMAP = path.join(ROOT, 'sitemap.xml');
const BLOG_INDEX = path.join(ROOT, 'blog', 'index.html');
const SITE = 'https://karachihijama.com';
const INDEXNOW_KEY = 'f381dff8a72f4bc563bb943551e6faa6';

const today = new Date().toISOString().slice(0, 10);

function readJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }
function writeJson(p, o) { fs.writeFileSync(p, JSON.stringify(o, null, 2) + '\n'); }
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

function ping(url) {
  return new Promise(resolve => {
    const u = `https://api.indexnow.org/indexnow?url=${encodeURIComponent(url)}&key=${INDEXNOW_KEY}`;
    https.get(u, r => { r.resume(); console.log(`  IndexNow ${r.statusCode} ${url}`); resolve(); })
         .on('error', e => { console.log(`  IndexNow failed (non-fatal): ${e.message}`); resolve(); });
  });
}

function addToSitemap(urlPath, priority) {
  let xml = fs.readFileSync(SITEMAP, 'utf8');
  const loc = `${SITE}/${urlPath}`;
  if (xml.includes(`<loc>${loc}</loc>`)) { console.log('  sitemap: already present'); return; }
  const entry = `  <url><loc>${loc}</loc>\n    <lastmod>${today}</lastmod><changefreq>monthly</changefreq><priority>${priority}</priority></url>\n`;
  xml = xml.replace('</urlset>', entry + '</urlset>');
  fs.writeFileSync(SITEMAP, xml);
  console.log('  sitemap: added');
}

function addToBlogIndex(item) {
  if (!item.target.startsWith('blog/')) return;
  let html = fs.readFileSync(BLOG_INDEX, 'utf8');
  const href = path.basename(item.target);
  if (html.includes(`href="${href}"`)) { console.log('  blog index: already present'); return; }

  const card = `    <a class="post-card reveal" href="${href}">
      <span class="post-tag" data-lang="en">${esc(item.tag_en)}</span><span class="post-tag" data-lang="ur">${esc(item.tag_ur)}</span>
      <h2><span data-lang="en">${esc(item.title_en)}</span><span data-lang="ur">${esc(item.title_ur)}</span></h2>
      <p><span data-lang="en">${esc(item.blurb_en)}</span><span data-lang="ur">${esc(item.blurb_ur)}</span></p>
      <span class="more" data-lang="en">Read →</span><span class="more" data-lang="ur">پڑھیں →</span>
    </a>
`;
  html = html.replace('  <div class="post-grid">\n', '  <div class="post-grid">\n' + card);

  const ld = `    {"@type":"BlogPosting","headline":"${item.title_en.replace(/"/g, '\\"')}","url":"${SITE}/${item.target}","author":{"@type":"Person","name":"Dr. Misbah Shaheen Cheena"},"datePublished":"${today}"},\n`;
  html = html.replace('  "blogPost":[\n', '  "blogPost":[\n' + ld);

  fs.writeFileSync(BLOG_INDEX, html);
  console.log('  blog index: card + JSON-LD added');
}

function markTopicPublished(slug, url) {
  if (!fs.existsSync(TOPICS_JSON)) return;
  const d = readJson(TOPICS_JSON);
  const topics = Array.isArray(d) ? d : d.topics;
  if (!topics) return;
  const t = topics.find(x => x.slug === slug);
  if (t) { t.status = 'published'; t.published_date = today; t.published_url = url; writeJson(TOPICS_JSON, d); console.log('  topics.json: marked published'); }
}

(async () => {
  if (!fs.existsSync(QUEUE_JSON)) { console.log('No queue.json — nothing to publish.'); process.exit(0); }
  const queue = readJson(QUEUE_JSON);
  const item = queue.find(q => q.status === 'pending');
  if (!item) { console.log('QUEUE EMPTY — no pending articles. Refill content-pipeline/queue/.'); process.exit(0); }

  const src = path.join(QUEUE_DIR, item.file);
  if (!fs.existsSync(src)) { console.error(`Queued file missing: ${item.file} — marking error and skipping.`); item.status = 'error'; writeJson(QUEUE_JSON, queue); process.exit(1); }

  const dest = path.join(ROOT, item.target);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
  fs.unlinkSync(src);
  console.log(`Publishing: ${item.target}`);

  addToSitemap(item.target, item.target.startsWith('blog/') ? '0.7' : '0.8');
  addToBlogIndex(item);

  const liveUrl = `${SITE}/${item.target}`;
  item.status = 'published';
  item.published_date = today;
  writeJson(QUEUE_JSON, queue);
  if (item.slug) markTopicPublished(item.slug, liveUrl);

  await ping(liveUrl);
  await ping(`${SITE}/sitemap.xml`);

  const remaining = queue.filter(q => q.status === 'pending').length;
  console.log(`DONE: ${liveUrl}`);
  console.log(`Queue remaining: ${remaining}`);
  if (remaining <= 3) console.log('WARNING: queue nearly empty — refill soon.');

  // surfaced to the workflow so it can put it in the commit message / job summary
  if (process.env.GITHUB_OUTPUT) {
    fs.appendFileSync(process.env.GITHUB_OUTPUT, `published_url=${liveUrl}\npublished_title=${item.title_en}\nremaining=${remaining}\n`);
  }
})();
