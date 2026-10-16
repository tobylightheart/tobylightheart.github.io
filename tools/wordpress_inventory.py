#!/usr/bin/env python3
"""Inventory public WordPress.com posts without account credentials."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from html.parser import HTMLParser
import json
import sys
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

DEFAULT_SITES = (
    "tobylightheart.wordpress.com",
    "mindtheleap.wordpress.com",
)
API_ROOT = "https://public-api.wordpress.com/wp/v2/sites"
USER_AGENT = "tobylightheart-site-migration-inventory/1.0"


class ImageSources(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "img":
            return
        values = dict(attrs)
        src = values.get("src")
        if src:
            self.urls.add(_without_query(src))
        for candidate in (values.get("srcset") or "").split(","):
            url = candidate.strip().split(" ", 1)[0]
            if url:
                self.urls.add(_without_query(url))


def _without_query(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def fetch(site: str, resource: str, fields: str) -> tuple[list[dict], int]:
    query = urlencode({"per_page": 100, "_fields": fields})
    request = Request(f"{API_ROOT}/{site}/{resource}?{query}", headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        records = json.load(response)
        total = int(response.headers["X-WP-Total"])
    if total > len(records):
        raise RuntimeError(f"{site}/{resource}: pagination required ({total} records)")
    return records, total


def inventory(site: str) -> tuple[dict, list[dict]]:
    posts, total = fetch(site, "posts", "id,date,link,title,content")
    comments, comment_total = fetch(site, "comments", "id,post,date,status,type")
    images = ImageSources()
    for post in posts:
        images.feed(post["content"]["rendered"])
    ordered = sorted(posts, key=lambda post: post["date"])
    years = Counter(post["date"][:4] for post in ordered)
    summary = {
        "site": site,
        "posts": total,
        "years": dict(sorted(years.items())),
        "first_post": ordered[0]["date"],
        "last_post": ordered[-1]["date"],
        "approved_public_comments": comment_total,
        "posts_with_approved_public_comments": len({comment["post"] for comment in comments}),
        "unique_inline_image_sources": len(images.urls),
        "note": "Image count covers public rendered post HTML, not the authenticated media library.",
    }
    rows = [
        {
            "site": site,
            "date": post["date"][:10],
            "title": post["title"]["rendered"],
            "url": post["link"],
        }
        for post in ordered
    ]
    return summary, rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", action="append", dest="sites", help="WordPress.com hostname; repeatable")
    parser.add_argument("--csv", help="write the complete permalink inventory to this path")
    args = parser.parse_args()

    summaries: list[dict] = []
    rows: list[dict] = []
    for site in args.sites or DEFAULT_SITES:
        summary, site_rows = inventory(site)
        summaries.append(summary)
        rows.extend(site_rows)

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as output:
            writer = csv.DictWriter(output, fieldnames=("site", "date", "title", "url"))
            writer.writeheader()
            writer.writerows(rows)
    json.dump({"sites": summaries, "total_posts": len(rows)}, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
