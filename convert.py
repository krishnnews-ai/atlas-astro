#!/usr/bin/env python3
"""
Blogger Feed → Atlas Astro Converter
- Reads feeds.txt (Blogger Atom feed)
- Extracts all posts and pages
- Unescapes HTML
- Writes Atlas theme .html fragments
- Updates manifest.json
"""

import re
import html
import json
import os
from pathlib import Path
from datetime import datetime

# ============ CONFIG ============
FEED_FILE = "feeds.txt"
OUTPUT_ROOT = "src/generated"
POSTS_DIR = os.path.join(OUTPUT_ROOT, "posts")
PAGES_DIR = os.path.join(OUTPUT_ROOT, "pages")
MANIFEST_FILE = "src/data/manifest.json"
# ================================


def slugify(text: str) -> str:
    """Convert title to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def extract_tag(content: str, tag: str) -> str:
    """Extract content of a tag (supports namespaced tags)."""
    pattern = rf"<{re.escape(tag)}[^>]*>(.*?)</{re.escape(tag)}>"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_categories(entry: str) -> list:
    """Extract category terms from an entry."""
    return re.findall(r'<category[^>]*term=[\'"]([^\'"]+)[\'"]', entry)


def parse_feed(raw: str) -> list:
    """Parse Blogger Atom feed into list of entries."""
    entries = re.findall(r"<entry>(.*?)</entry>", raw, re.DOTALL)
    print(f"📥 Total entries found: {len(entries)}")
    return entries


def process_entry(entry: str, index: int) -> dict:
    """Process a single entry into a structured dict."""
    # Title
    title_raw = extract_tag(entry, "title")
    title = html.unescape(title_raw) if title_raw else f"Untitled {index}"

    # Type (POST or PAGE)
    entry_type = extract_tag(entry, "blogger:type") or "POST"

    # Status
    status = extract_tag(entry, "blogger:status") or "LIVE"

    # Content
    content_raw = extract_tag(entry, "content")
    content = html.unescape(content_raw) if content_raw else ""

    # Meta description
    meta_desc = extract_tag(entry, "blogger:metaDescription")
    meta_desc = html.unescape(meta_desc) if meta_desc else ""

    # Author
    author = extract_tag(entry, "name") or "CoinAINews Staff"

    # Published date
    published = extract_tag(entry, "published")

    # Updated date
    updated = extract_tag(entry, "updated")

    # Categories
    categories = extract_categories(entry)

    # Original Blogger filename (for slug)
    blogger_filename = extract_tag(entry, "blogger:filename")
    if blogger_filename:
        # Extract slug from /2026/09/some-slug.html
        match = re.search(r"/([^/]+)\.html$", blogger_filename)
        slug = match.group(1) if match else slugify(title)
    else:
        slug = slugify(title)

    # ID
    entry_id = extract_tag(entry, "id")

    return {
        "id": entry_id,
        "title": title,
        "slug": slug,
        "type": entry_type,
        "status": status,
        "content": content,
        "metaDescription": meta_desc,
        "author": author,
        "published": published,
        "updated": updated,
        "categories": categories,
        "filename": blogger_filename,
    }


def write_post_file(post: dict) -> str:
    """Write a single post as .html fragment. Returns filepath."""
    filename = f"{post['slug']}.html"

    if post["type"] == "PAGE":
        out_dir = PAGES_DIR
    else:
        out_dir = POSTS_DIR

    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, filename)

    # Build HTML fragment (Atlas-style)
    fragment = f"""<!--
Title: {post['title']}
Author: {post['author']}
Published: {post['published']}
Updated: {post['updated']}
Categories: {', '.join(post['categories'])}
MetaDescription: {post['metaDescription']}
-->

<article class="atlas-post" data-slug="{post['slug']}">
  <header class="atlas-post__header">
    <h1 class="atlas-post__title">{html.escape(post['title'])}</h1>
    <div class="atlas-post__meta">
      <span class="atlas-post__author">{html.escape(post['author'])}</span>
      <time class="atlas-post__date" datetime="{post['published']}">{post['published']}</time>
    </div>
    <div class="atlas-post__categories">
      {''.join(f'<span class="atlas-post__category">{html.escape(c)}</span>' for c in post['categories'])}
    </div>
  </header>

  <div class="atlas-post__content">
{post['content']}
  </div>
</article>
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fragment)

    return filepath


def update_manifest(posts: list, pages: list):
    """Update manifest.json with new posts and pages."""
    # Load existing manifest or create new
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            try:
                manifest = json.load(f)
            except json.JSONDecodeError:
                manifest = {}
    else:
        manifest = {}

    # Ensure structure
    if "posts" not in manifest:
        manifest["posts"] = []
    if "pages" not in manifest:
        manifest["pages"] = []

    # Add posts
    for post in posts:
        entry = {
            "slug": post["slug"],
            "title": post["title"],
            "author": post["author"],
            "published": post["published"],
            "updated": post["updated"],
            "categories": post["categories"],
            "metaDescription": post["metaDescription"],
            "path": f"/{post['slug']}/",
            "file": f"posts/{post['slug']}.html",
        }
        # Avoid duplicates
        manifest["posts"] = [p for p in manifest["posts"] if p.get("slug") != post["slug"]]
        manifest["posts"].append(entry)

    # Add pages
    for page in pages:
        entry = {
            "slug": page["slug"],
            "title": page["title"],
            "author": page["author"],
            "published": page["published"],
            "updated": page["updated"],
            "metaDescription": page["metaDescription"],
            "path": f"/{page['slug']}/",
            "file": f"pages/{page['slug']}.html",
        }
        manifest["pages"] = [p for p in manifest["pages"] if p.get("slug") != page["slug"]]
        manifest["pages"].append(entry)

    # Write manifest
    os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✅ Manifest updated: {len(manifest['posts'])} posts, {len(manifest['pages'])} pages")


def main():
    print("🚀 Blogger Feed → Atlas Converter")
    print("=" * 50)

    # Check feed file
    if not os.path.exists(FEED_FILE):
        print(f"❌ Error: {FEED_FILE} not found!")
        return

    # Read feed
    with open(FEED_FILE, "r", encoding="utf-8") as f:
        raw = f.read()
    print(f"📄 Read {len(raw)} characters from {FEED_FILE}")

    # Parse entries
    entries = parse_feed(raw)

    # Process entries
    posts = []
    pages = []

    for i, entry in enumerate(entries, 1):
        post = process_entry(entry, i)

        # Skip trashed/deleted
        if post["status"] in ("SOFT_TRASHED", "TRASHED"):
            print(f"   ⏭️  Skipping trashed: {post['title'][:50]}")
            continue

        # Skip empty titles
        if not post["title"] or post["title"] == "Untitled":
            print(f"   ⏭️  Skipping empty title #{i}")
            continue

        # Write file
        filepath = write_post_file(post)

        if post["type"] == "PAGE":
            pages.append(post)
        else:
            posts.append(post)

        if i % 25 == 0:
            print(f"   📝 Processed: {i}/{len(entries)}")

    print(f"\n✅ Done!")
    print(f"   📝 Posts written: {len(posts)}")
    print(f"   📄 Pages written: {len(pages)}")

    # Update manifest
    update_manifest(posts, pages)

    print("\n🎉 Conversion complete!")


if __name__ == "__main__":
    main()
