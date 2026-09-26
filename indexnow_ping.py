#!/usr/bin/env python3
"""Submit every URL in sitemap.xml to IndexNow (Bing, Yandex, Seznam, Naver...).

Stdlib only. Run AFTER the site is deployed, so the key file is live:

    py -3.12 indexnow_ping.py            # submit all sitemap URLs
    py -3.12 indexnow_ping.py --dry-run  # just list what would be sent

The key file https://karachihijama.com/<KEY>.txt must contain exactly KEY.
It already exists in the repo root and is the same key content-pipeline/publish-next.js uses.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

HOST = "karachihijama.com"
KEY = "f381dff8a72f4bc563bb943551e6faa6"
KEY_LOCATION = "https://%s/%s.txt" % (HOST, KEY)
ENDPOINT = "https://api.indexnow.org/IndexNow"
ROOT = os.path.dirname(os.path.abspath(__file__))


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as fh:
        xml = fh.read()
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", xml)
    return [u for u in urls if u.startswith("https://%s/" % HOST)]


def main():
    dry = "--dry-run" in sys.argv
    with open(os.path.join(ROOT, KEY + ".txt"), encoding="utf-8") as fh:
        if fh.read().strip() != KEY:
            sys.exit("Key file content does not match KEY - aborting.")
    urls = sitemap_urls()
    print("%d URLs from sitemap.xml" % len(urls))
    if dry:
        print("\n".join(urls))
        return
    payload = json.dumps({"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION,
                          "urlList": urls}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=payload, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print("IndexNow HTTP %s (200/202 = accepted)" % resp.status)
    except urllib.error.HTTPError as e:
        # 400 bad request, 403 key not valid/not found, 422 URLs don't match host, 429 too many requests
        print("IndexNow HTTP %s: %s" % (e.code, e.read()[:300].decode("utf-8", "replace")))
        sys.exit(1)
    except urllib.error.URLError as e:
        print("Network error: %s" % e.reason)
        sys.exit(1)


if __name__ == "__main__":
    main()
