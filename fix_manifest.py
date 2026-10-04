#!/usr/bin/env python3
import json, os, re

MANIFEST = "src/data/manifest.json"
POSTS_DIR = "src/generated/posts"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def extract_meta(html):
    """Extract title, image, date from HTML"""
    title = ""
    image = ""
    date = ""

    # Title — <title> or first <h1>
    m = re.search(r'<title>([^<]+)</title>', html, re.I)
    if m:
        title = m.group(1).strip()

    # First image
    m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    if m:
        image = m.group(1)

    # Date — ISO format ya meta
    m = re.search(r'(\d{4}-\d{2}-\d{2})', html)
    if m:
        date = m.group(1)

    return title, image, date

def main():
    print("🔧 Generating manifest from posts...")

    if not os.path.isdir(POSTS_DIR):
        print(f"❌ {POSTS_DIR} not found")
        return

    files = sorted(os.listdir(POSTS_DIR))
    html_files = [f for f in files if f.endswith('.html')]

    if not html_files:
        print("❌ No HTML files found")
        return

    print(f"📄 Found {len(html_files)} HTML files")

    posts = []
    for fname in html_files:
        slug = fname[:-5]  # remove .html
        path = os.path.join(POSTS_DIR, fname)

        try:
            html = open(path, encoding="utf-8").read()
        except:
            continue

        title, image, date = extract_meta(html)

        if not title:
            title = slug.replace('-', ' ').title()

        posts.append({
            "slug": slug,
            "title": title,
            "excerpt": "",
            "cover": image,
            "date": date or "2026-01-01",
            "site": "CoinAINews",
            "categories": ["Market News"],
            "format": "standard",
            "bodyClass": "single-post",
            "file": f"posts/{fname}",
            "path": f"/{slug}/"
        })

    manifest = {
        "posts": posts,
        "pages": []
    }

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    covers = sum(1 for p in posts if p["cover"])
    print(f"✅ {len(posts)} posts manifest me add hui")
    print(f"🖼️  {covers} posts me cover image mili")

if __name__ == "__main__":
    main()
