#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate a queue-ready bilingual article page for karachihijama.com.

Built 2026-09-03. The pipeline was never out of PLAN - topics.json holds 61
pending topics - it was out of WRITTEN PAGES. publish-next.js only moves an
existing file from content-pipeline/queue/ to its target; nobody had written
the files. This generator closes that gap.

It clones the live page shell (header, CSS, footer, scripts) straight out of an
existing published article, so a generated page cannot drift from the site's
markup, styling or navigation. Only the article content is authored per topic.

    from gen_article import build, write_queue_entry
    build(TOPIC)                      # -> content-pipeline/queue/<slug>.html

Every visible string is a pair: English AND Urdu. The site renders one or the
other from a data-lang toggle, so an unpaired string would leave a blank gap
for half the audience. build() refuses to emit a page whose data-lang counts
do not match.
"""
import html
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
QUEUE_DIR = os.path.join(HERE, "queue")
QUEUE_JSON = os.path.join(HERE, "queue.json")
SHELL_SRC = os.path.join(ROOT, "blog", "hijama-for-diabetes.html")
SITE = "https://karachihijama.com"
CLINIC = "Shaheen Shafi Unani Clinic &amp; Hijama Center"
AUTHOR = "Dr. Misbah Shaheen Cheena"

# Copied verbatim from the live page. The button is wired by the site's own
# JS through the data-wa attribute - hardcoding a wa.me URL would bypass that
# and would also hardcode a number that may change.
_WA_BUTTON = """<a class="btn btn-wa btn-lg" data-wa href="#">
      <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.2 1.6 6L4 29l8.2-1.6c1.8.9 3.7 1.4 5.8 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.9c-1.8 0-3.5-.5-5-1.4l-.4-.2-4.9 1 1-4.8-.3-.4c-1-1.6-1.5-3.4-1.5-5.3C4.4 9.5 9.5 4.4 16 4.4S27.6 9.5 27.6 16 22.5 24.9 16 24.9zm6.5-8c-.4-.2-2.1-1-2.4-1.1-.3-.1-.6-.2-.8.2s-.9 1.1-1.1 1.3c-.2.2-.4.2-.8.1-.4-.2-1.5-.6-2.9-1.8-1.1-1-1.8-2.2-2-2.6-.2-.4 0-.6.2-.8.2-.2.4-.4.5-.6.2-.2.2-.4.4-.6.1-.2 0-.5 0-.6-.1-.2-.8-2-1.1-2.7-.3-.7-.6-.6-.8-.6h-.7c-.2 0-.6.1-.9.5-.3.4-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.5 3.8 6 5.3.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 2.1-.9 2.4-1.7.3-.8.3-1.5.2-1.7-.1-.1-.3-.2-.7-.4z"/></svg>
      <span data-lang="en">Book on WhatsApp</span>
      <span data-lang="ur">واٹس ایپ پر بُک کریں</span>
    </a>"""



def _shell():
    """Pull style / header / footer / scripts out of a live page."""
    src = io.open(SHELL_SRC, encoding="utf-8").read()
    style = re.search(r"<style>.*?</style>", src, re.S).group(0)
    i_body = src.find("<body")
    i_art = src.find('<article class="article-wrap"')
    i_foot = src.find('<footer class="site-footer"')
    header = src[i_body:i_art]
    footer_and_tail = src[i_foot:]
    return style, header, footer_and_tail


def _e(s):
    return html.escape(s, quote=False)


def _pair(en, ur, tag="span"):
    return ('<%s data-lang="en">%s</%s><%s data-lang="ur">%s</%s>'
            % (tag, _e(en), tag, tag, _e(ur), tag))


def _para(en, ur):
    return ('      <p>\n        <span data-lang="en">%s</span>\n'
            '        <span data-lang="ur">%s</span>\n      </p>\n'
            % (en, ur))


def _jsonld(t):
    """MedicalWebPage + BreadcrumbList + FAQPage, matching the live pages."""
    url = "%s/%s" % (SITE, t["target"])
    med = {
        "@context": "https://schema.org", "@type": "MedicalWebPage",
        "@id": url + "#page", "url": url,
        "name": t["seo_title"], "description": t["seo_desc"],
        "inLanguage": ["en", "ur"],
        "datePublished": t["date"], "dateModified": t["date"],
        "author": {"@type": "Person", "name": AUTHOR,
                   "jobTitle": "Unani Physician & Hijama Practitioner"},
        "publisher": {"@type": "Organization",
                      "name": "Shaheen Shafi Unani Clinic & Hijama Center",
                      "url": SITE},
        "about": {"@type": "MedicalTherapy", "name": "Hijama (Wet Cupping)"},
        "audience": {"@type": "Patient"},
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog",
             "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": t["title_en"],
             "item": url},
        ]}
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q["q_en"],
             "acceptedAnswer": {"@type": "Answer", "text": q["a_en"]}}
            for q in t["faq"]]}
    out = []
    for obj in (med, crumbs, faq):
        out.append('<script type="application/ld+json">\n%s\n</script>'
                   % json.dumps(obj, ensure_ascii=False, indent=2))
    return "\n".join(out)


def _page_title(seo_title):
    """<title> should stay within ~60 characters so it is not truncated in results.
    The brand suffix is only added when it fits."""
    for suffix in (" | Shaheen Shafi Unani Clinic, Karachi", " | Karachi Hijama", ""):
        if len(seo_title + suffix) <= 60:
            return seo_title + suffix
    return seo_title


def _head(t, style):
    url = "%s/%s" % (SITE, t["target"])
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>%(page_title)s</title>
<meta name="description" content="%(seo_desc)s">
<meta name="keywords" content="%(keywords)s">
<link rel="canonical" href="%(url)s">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="Shaheen Shafi Unani Clinic &amp; Hijama Center">
<meta property="og:title" content="%(seo_title)s">
<meta property="og:description" content="%(og_desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:locale" content="en_PK">
<meta property="og:locale:alternate" content="ur_PK">
<meta property="og:image" content="%(site)s/img/clinic-1.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="900">
<meta property="og:image:alt" content="Registration certificates on the wall at Shaheen Shafi Unani Clinic &amp; Hijama Center, Model Colony, Karachi">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="%(site)s/img/clinic-1.jpg">
<meta name="twitter:title" content="%(seo_title)s">
<meta name="twitter:description" content="%(og_desc)s">

<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
<link rel="shortcut icon" href="/favicon.svg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="192x192">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Inter:wght@400;500;600;700&display=swap">

%(jsonld)s

%(style)s
<!-- Google tag (gtag.js) — GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-L0BJ0DVJEV"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-L0BJ0DVJEV');</script>
</head>
""" % dict(seo_title=_e(t["seo_title"]), seo_desc=_e(t["seo_desc"]),
           page_title=_e(_page_title(t["seo_title"])),
           keywords=_e(t["keywords"]), url=url, site=SITE,
           og_desc=_e(t.get("og_desc", t["seo_desc"])[:200]),
           jsonld=_jsonld(t), style=style)


def _body(t):
    parts = []
    parts.append('<article class="article-wrap">\n')
    parts.append("""
  <!-- Breadcrumb -->
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="../index.html#top"><span data-lang="en">Home</span><span data-lang="ur">ہوم</span></a>
    <span aria-hidden="true">&rsaquo;</span>
    <a href="index.html"><span data-lang="en">Blog</span><span data-lang="ur">بلاگ</span></a>
    <span aria-hidden="true">&rsaquo;</span>
    <span data-lang="en">%s</span><span data-lang="ur">%s</span>
  </nav>
""" % (_e(t["title_en"]), _e(t["title_ur"])))

    parts.append("""
  <div class="article">
    <header class="article-head">
      <p class="eyebrow"><span data-lang="en">%s</span><span data-lang="ur">%s</span></p>
      <h1>
        <span data-lang="en">%s</span>
        <span data-lang="ur">%s</span>
      </h1>
      <div class="article-meta">
        <span><b>%s</b></span>
        <span aria-hidden="true">&middot;</span>
        <span data-lang="en">Published %s</span><span data-lang="ur">شائع شدہ %s</span>
        <span aria-hidden="true">&middot;</span>
        <span data-lang="en">%s, Karachi</span>
        <span data-lang="ur">شاہین شافی یونانی کلینک و حجامہ سینٹر، کراچی</span>
      </div>
    </header>

    <div class="article-body">
""" % (_e(t["eyebrow_en"]), _e(t["eyebrow_ur"]),
       _e(t["title_en"]), _e(t["title_ur"]), AUTHOR,
       _e(t["date_en"]), _e(t["date_ur"]), CLINIC))

    parts.append('      <p class="lede-para">\n'
                 '        <span data-lang="en">%s</span>\n'
                 '        <span data-lang="ur">%s</span>\n      </p>\n'
                 % (t["lede_en"], t["lede_ur"]))

    parts.append("""
      <div class="disclaimer">
        <p><span data-lang="en">Hijama is a complementary traditional practice. It is not a cure and never replaces your doctor, your prescribed medication or emergency care. Always speak to your physician about your condition.</span><span data-lang="ur">حجامہ ایک معاون روایتی طریقہ ہے۔ یہ علاج کا متبادل نہیں اور آپ کے ڈاکٹر، تجویز کردہ دوا یا ہنگامی علاج کی جگہ کبھی نہیں لے سکتا۔ اپنی حالت کے بارے میں ہمیشہ اپنے معالج سے بات کریں۔</span></p>
      </div>
""")

    for s in t["sections"]:
        parts.append('\n      <h2><span data-lang="en">%s</span>'
                     '<span data-lang="ur">%s</span></h2>\n'
                     % (_e(s["h2_en"]), _e(s["h2_ur"])))
        for en, ur in s.get("paras", []):
            parts.append(_para(en, ur))
        if s.get("caution"):
            parts.append('      <div class="caution">\n        <p>'
                         '<span data-lang="en">%s</span>'
                         '<span data-lang="ur">%s</span></p>\n      </div>\n'
                         % (s["caution"][0], s["caution"][1]))
        if s.get("bullets"):
            parts.append('      <ul>\n')
            for en, ur in s["bullets"]:
                parts.append('        <li><span data-lang="en">%s</span>'
                             '<span data-lang="ur">%s</span></li>\n'
                             % (en, ur))
            parts.append('      </ul>\n')

    # FAQ - rendered visibly as well as in JSON-LD, so the schema is not orphaned
    parts.append('\n      <h2><span data-lang="en">Common questions</span>'
                 '<span data-lang="ur">عام سوالات</span></h2>\n')
    for q in t["faq"]:
        parts.append('      <h3><span data-lang="en">%s</span>'
                     '<span data-lang="ur">%s</span></h3>\n'
                     % (_e(q["q_en"]), _e(q["q_ur"])))
        parts.append(_para(q["a_en"], q["a_ur"]))

    parts.append("""
      <div class="disclaimer">
        <p><span data-lang="en">If your symptoms are severe, sudden or worsening, please see a doctor or go to a hospital first. Hijama can wait; urgent medical care cannot.</span><span data-lang="ur">اگر آپ کی علامات شدید، اچانک یا بگڑ رہی ہوں تو پہلے ڈاکٹر سے رجوع کریں یا اسپتال جائیں۔ حجامہ انتظار کر سکتا ہے؛ ہنگامی طبی امداد نہیں۔</span></p>
      </div>

    </div>
  </div>

  <section class="article-cta">
    <h2><span data-lang="en">%s</span><span data-lang="ur">%s</span></h2>
    <p>
      <span data-lang="en">%s</span>
      <span data-lang="ur">%s</span>
    </p>
%s
  </section>
""" % (_e(t["cta_en"]), _e(t["cta_ur"]),
       t["cta_body_en"], t["cta_body_ur"], _WA_BUTTON))

    # Related links keep a new page from being orphaned - internal links are how
    # a fresh URL gets crawled and how authority reaches it.
    if t.get("related"):
        parts.append('\n  <section class="related" aria-label="Related">\n'
                     '    <h2><span data-lang="en">Read more</span>'
                     '<span data-lang="ur">مزید پڑھیں</span></h2>\n'
                     '    <ul class="related-links">\n')
        for r in t["related"]:
            parts.append(
                '      <li>\n        <a href="%s">\n'
                '          <span data-lang="en">%s</span>\n'
                '          <span data-lang="ur">%s</span>\n'
                '          <span data-lang="en">%s</span>\n'
                '          <span data-lang="ur">%s</span>\n'
                '        </a>\n      </li>\n'
                % (r["href"], _e(r["t_en"]), _e(r["t_ur"]),
                   _e(r["d_en"]), _e(r["d_ur"])))
        parts.append('    </ul>\n  </section>\n')

    parts.append('</article>\n</main>\n\n')
    return "".join(parts)


def build(t, verbose=True):
    style, header, footer = _shell()
    page = _head(t, style) + header + _body(t) + footer
    en = page.count('data-lang="en"')
    ur = page.count('data-lang="ur"')
    if en != ur:
        raise ValueError("data-lang parity broken for %s: en=%d ur=%d"
                         % (t["slug"], en, ur))
    os.makedirs(QUEUE_DIR, exist_ok=True)
    out = os.path.join(QUEUE_DIR, t["slug"] + ".html")
    io.open(out, "w", encoding="utf-8").write(page)
    if verbose:
        words = len(re.sub(r"<[^>]+>", " ", page).split())
        print("  %-46s %6d bytes  ~%4d words  lang %d/%d"
              % (t["slug"] + ".html", len(page), words, en, ur))
    return out


def write_queue_entry(t):
    q = json.load(io.open(QUEUE_JSON, encoding="utf-8"))
    if any(e.get("slug") == t["slug"] for e in q):
        print("  queue: %s already present, skipped" % t["slug"])
        return False
    q.append({
        "file": t["slug"] + ".html",
        "target": t["target"],
        "slug": t["slug"],
        "title_en": t["title_en"], "title_ur": t["title_ur"],
        "tag_en": t["tag_en"], "tag_ur": t["tag_ur"],
        "blurb_en": t["blurb_en"], "blurb_ur": t["blurb_ur"],
        "status": "pending",
        "published_date": None,
    })
    io.open(QUEUE_JSON, "w", encoding="utf-8").write(
        json.dumps(q, ensure_ascii=False, indent=2) + "\n")
    return True
