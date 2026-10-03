#!/usr/bin/env python3
"""
Fix manifest.json — keep ONLY posts that have HTML files in src/generated/posts/
Removes all Atlas demo posts.
"""
import os
import json

POSTS_DIR = "src/generated/posts"
MANIFEST_FILE = "src/data/manifest.json"
DEFAULT_BODY_CLASS = "post-template-default single single-post single-format-standard wp-embed-responsive theme-atlas s-front site-skin site-light box-solid wheading-simple sticky-header-active reading-indicator-bottom sticky-sidebar elementor-default elementor-kit-6"

def main():
    print("🔧 Cleaning manifest...")

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    if os.path.exists(POSTS_DIR):
        files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith(".html")])
    else:
        files = []

    print(f"📁 Found {len(files)} HTML files")

    valid_slugs = {f[:-5] for f in files}

    old_count = len(manifest.get("posts", []))
    
    cleaned_posts = []
    for post in manifest.get("posts", []):
        slug = post.get("slug", "")
        if slug in valid_slugs:
            cleaned_posts.append({
                "slug": slug,
                "title": post.get("title", slug.replace("-", " ").title()),
                "excerpt": post.get("excerpt", ""),
                "cover": post.get("cover", ""),
                "date": post.get("date", "2026-10-03"),
                "site": post.get("site", "default"),
                "categories": post.get("categories", ["Market News"]),
                "format": post.get("format", "standard"),
                "bodyClass": post.get("bodyClass", DEFAULT_BODY_CLASS),
                "file": f"posts/{slug}.html",
                "path": f"/{slug}/"
            })

    manifest["posts"] = cleaned_posts

    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✅ Posts: {old_count} → {len(cleaned_posts)}")
    print(f"   ❌ Removed {old_count - len(cleaned_posts)} Atlas demo posts")

if __name__ == "__main__":
    main()
