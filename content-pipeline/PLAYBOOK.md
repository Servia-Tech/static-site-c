# Karachi Hijama — Daily Content Pipeline Playbook

**Purpose:** publish 1 new, genuinely good, unique, SEO-optimized article to karachihijama.com per firing
(this Routine fires 3x/day → 3 articles/day), rotating between local-area pages, disease/condition pages,
and other-service/city-guide pages, with proper internal + external linking, then push it live and ping
search engines. Fully autonomous — no human input required per run.

## 0. Repo & access
- Repo: `https://github.com/Servia-Tech/static-site-c` (private). Served live via GitHub Pages at
  `https://karachihijama.com/` (CNAME file in repo root — do not remove it).
- Clone/push with the PAT: read it from `~/servia_credentials/SERVIA-CREDENTIALS.md` on the ThinkPad
  (`ssh winbox`, HostName ssh.servia.ae, already configured in this environment's `~/.ssh/config`) —
  search that file for "static-site-c" / "github token". If not there, check
  `/home/user/servia_work/SERVIA_NOTES.md` or ask via `git config --get remote.origin.url` on an existing
  ThinkPad checkout at `C:\Users\Lenovo\servia_automation\static-site-c` (a working clone with credentials
  already cached may exist there).
- Clone: `git clone https://<PAT>@github.com/Servia-Tech/static-site-c.git`
- Push: `git push https://<PAT>@github.com/Servia-Tech/static-site-c.git HEAD:main` (or plain `git push`
  once the remote has the token embedded).

## 1. Pick the next topic
- Open `content-pipeline/topics.json`.
- Find the first entry with `"status": "pending"`, rotating category if possible so the day's 3 posts
  aren't all the same category (check `content-pipeline/topics.json` git log or `published_date` of the
  last few entries to infer what category was posted most recently, and pick a different one next).
- **If fewer than 15 `pending` topics remain**, generate 20-30 more before continuing — same 3 categories
  (`area` = a real, well-known Karachi neighbourhood not yet covered; `condition` = a real health complaint
  people search for, not yet covered, staying within honest/complementary-care framing; `other` = a
  Pakistani city guide, a service (Homeopathy/Reiki/Herbal), or an evergreen guide topic). Add them to the
  JSON array in the same shape before picking the next topic.

## 1.5. Research real "People Also Ask" questions for the topic (operator's explicit direction, 2026-07-28)
Before writing, think about (or if you have live web/search access, actually look up) the real questions
Google shows in "People Also Ask" for this topic — the operator's example was searching "reiki" and getting
"Does Reiki healing really work?", "What are the negatives of Reiki?", "What are the five rules of Reiki?",
"What to avoid after Reiki?", "What do doctors think of Reiki?", "How long does it take for Reiki to work?",
"Is Reiki healing against God?", "How many Reiki sessions are needed?" etc. **Every article's FAQPage schema
+ visible FAQ section should answer THAT KIND of real, specific, high-intent question for its own topic** —
not generic filler questions. This is what gets a page pulled into Google's PAA/rich-result boxes, which is
the explicit goal. For a condition/service, ask yourself: what would a worried/curious person actually type
right before or after searching this term? Answer honestly, in the same complementary-care, never-a-cure,
see-a-doctor-if-needed voice as the rest of the site. For anything touching religion (e.g. Reiki, an energy
practice some scholars view as incompatible with Islamic theology, vs Hijama which is explicitly Sunnah) —
present it neutrally and factually, note genuine differing scholarly views, and never issue a personal
religious ruling; let the reader form their own view alongside their own religious understanding.

## 2. Write the article — match the EXISTING template exactly
Three templates already exist in the repo — copy the closest one and adapt, don't invent a new layout:
- **`category: "area"`** → copy `hijama-home-service-dha-karachi.html` (repo root, not `blog/`). This is a
  **local landing page**: fixed-price home-service framing, "why patients in [area] choose home service",
  an honest disclaimer that the clinic is based in Model Colony and home service means the practitioner
  travels to them (never claim a branch clinic in that area), a WhatsApp CTA with area name pre-filled in
  the message, and a Related section linking to `wet-cupping-hijama-karachi.html`, `dry-cupping-karachi.html`,
  `packages.html`, `dr-misbah-shaheen-cheena.html`.
- **`category: "condition"`** → copy `blog/hijama-for-diabetes.html`. This is a **blog article** (goes in
  `blog/`): TOC box, "what people notice" + honest evidence framing, a `.cond` callout with "when to see a
  doctor first" advice, FAQPage schema (3-5 real questions), and — critically — the same **complementary
  care disclaimer used throughout the site**: Hijama is never a cure, never a replacement for medication/
  a doctor, and any condition with red-flag symptoms should see a doctor first. Do NOT write anything that
  could read as a medical claim to cure/treat/diagnose — this is what every existing article does and it
  is why this site is safe to keep publishing at scale; don't drift from it.
- **`category: "other"` (`subtype: "city-guide"`)** → copy `online-hijama-unani-consultation-uae.html` but
  reframe for a **domestic Pakistani city**: the clinic is Karachi-only and physical cupping needs an
  in-person visit, so this page is honest content for someone researching Hijama in their city — it offers
  a WhatsApp consultation to discuss suitability/aftercare and plan a Karachi visit (medical-tourism style),
  NOT a claim of a branch or remote cupping service. Price in PKR, not AED.
- **`other` (`subtype: "service"` or `"guide"`)** → copy `blog/hijama-for-diabetes.html`'s structure but
  drop the disease-specific `.cond`/FAQ-safety framing for something more relevant to the topic (e.g. a
  Reiki or Homeopathy explainer, a myths/history/how-to guide). Keep the TOC, disclaimers, and Related links.

**Every article MUST have, no exceptions (this is what keeps the site Google-safe and on-brand):**
1. Full bilingual EN + `data-lang="ur"` Urdu content throughout (not just the title) — write real, fluent
   Urdu, not machine-literal translation. Match the tone of existing articles.
2. Complete `<head>`: title, meta description, meta keywords, canonical, OG + Twitter tags, geo tags (for
   area pages), author, favicon, fonts, `styles.css` link, the same `<style>` block pattern (article-wrap /
   article / article-body / caution / article-cta / related / toc classes — copy verbatim from the closest
   template, only add topic-specific CSS if truly needed).
3. JSON-LD: `Service` or `MedicalWebPage`/`Article` (whichever the closest template uses) + `BreadcrumbList`
   + `FAQPage` (3-5 real Q&As).
4. 900-1,500+ words of genuinely useful, original English content (plus the Urdu). No filler, no keyword
   stuffing — write like the existing articles: warm, honest, practical, name-checking Dr Misbah Shaheen
   Cheena, Model Colony, and the clinic's actual practices (single-use sterile equipment, fixed pricing).
5. **3-4 internal links** to genuinely related existing pages (other area pages, the condition most related
   to this topic, `packages.html`, `dr-misbah-shaheen-cheena.html`, `wet-cupping-hijama-karachi.html`, or
   relevant blog posts) — pick real, sensible relations, not random links.
6. **1-2 external links** to a genuinely authoritative source for anything factual/medical claimed (e.g. a
   Mayo Clinic, NIH/PubMed, or WHO page on the condition being discussed, or a reputable Hijama/cupping
   research summary) — `target="_blank" rel="noopener noreferrer nofollow"`. This is what makes health
   content credible to both readers and Google (E-E-A-T) — don't skip it on condition articles.
7. GA4 snippet (`G-L0BJ0DVJEV`) — copy the exact `<script>` tags from any existing page, unchanged.
8. A WhatsApp CTA section with `data-wa` + pre-filled `data-wa-msg-en`/`data-wa-msg-ur` referencing this
   specific topic (area name or condition), same visual pattern as existing pages.
9. A "Related" section (3-4 links) at the end — same markup as existing pages.

## 3. Wire the new page into the site (every single time, don't skip any of these)
1. Save the file at the right path: area/city-guide pages → repo root (`<slug>.html`); condition/service/
   guide pages → `blog/<slug>.html`.
2. **`sitemap.xml`** — add a new `<url>` entry (same format as existing ones; `<lastmod>` = today's date,
   `<changefreq>monthly</changefreq>`, `<priority>0.7</priority>` for blog posts or `0.8` for area/city
   pages).
3. **`blog/index.html`** (only for `blog/` pages) — add a new `.post-card` in the `.post-grid` (matching
   the existing card markup: tag, h2, one-line description, "Read →") AND add a matching entry to the
   `blogPost` array in the page's `Blog` JSON-LD script near the top (`headline`, `url`, `author`,
   `datePublished` = today).
4. **Cross-link back**: open 1-2 of the most relevant EXISTING pages you linked to from the new article and
   add a link back to the new article in their own Related section, so linking is bidirectional (real
   internal-linking strength, not one-way). Keep this light — 1-2 pages is enough per new article, don't
   rewrite unrelated pages.
5. Update `content-pipeline/topics.json`: set this topic's `"status": "published"`, add `"published_date"`
   and `"published_url"`.

## 4. Publish
```
git add -A
git commit -m "Add [title] — daily content pipeline"
git push https://<PAT>@github.com/Servia-Tech/static-site-c.git HEAD:main
```
Verify live (allow ~1-2 min for GitHub Pages to rebuild): `curl -sI https://karachihijama.com/<path>` → 200.

## 5. Request indexing (IndexNow — already configured, no setup needed)
The IndexNow key file `f381dff8a72f4bc563bb943551e6faa6.txt` already exists at the site root. Ping it for
the new URL(s) (works for Bing + participating engines instantly; also resubmit `sitemap.xml` itself since
it changed):
```
curl -s "https://api.indexnow.org/indexnow?url=https://karachihijama.com/<new-page>&key=f381dff8a72f4bc563bb943551e6faa6"
curl -s "https://api.indexnow.org/indexnow?url=https://karachihijama.com/sitemap.xml&key=f381dff8a72f4bc563bb943551e6faa6"
```
For Google specifically there is no public "request indexing" API for normal content — internal linking +
the sitemap + IndexNow + natural crawl frequency (the site already gets crawled regularly) is the correct,
ToS-safe approach. Do not use the Indexing API (that's restricted to job-posting/livestream markup only).

## 6. Report back (only if something is genuinely wrong)
This Routine should run silently end-to-end. Only surface a message to the user if: the GitHub push fails
and can't be recovered, the topic bank has run dry (<5 pending) and needs a bigger refresh than you can
safely do alone, or something in this playbook no longer matches the live site's structure (redesign etc.).
Otherwise just publish and stop — no status report needed for a normal successful run.
