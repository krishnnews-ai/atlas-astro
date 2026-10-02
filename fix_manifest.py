#!/usr/bin/env python3
import os, json

POSTS_DIR = "src/generated/posts"
MANIFEST_FILE = "src/data/manifest.json"
DEFAULT_BODY_CLASS = "post-template-default single single-post single-format-standard wp-embed-responsive theme-atlas s-front site-skin site-light box-solid wheading-simple sticky-header-active reading-indicator-bottom sticky-sidebar elementor-default elementor-kit-6"

def main():
    print("Fixing manifest...")
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            try:
                manifest = json.load(f)
            except:
                manifest = {}
    else:
        manifest = {}

    if "posts" not in manifest or not isinstance(manifest["posts"], list):
        manifest["posts"] = []
    if "pages" not in manifest or not isinstance(manifest["pages"], list):
        manifest["pages"] = []

    manifest["posts"] = [p for p in manifest["posts"] if isinstance(p, dict)]

    if os.path.exists(POSTS_DIR):
        files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith(".html")])
        print(f"Found {len(files)} posts")

        for filename in files:
            slug = filename[:-5]
            title = slug.replace("-", " ").replace("_", " ").title()

            found = False
            for p in manifest["posts"]:
                if p.get("slug") == slug:
                    p["title"] = p.get("title") or title
                    p["file"] = f"posts/{filename}"
                    p["path"] = f"/{slug}/"
                    p["excerpt"] = p.get("excerpt", "")
                    p["cover"] = p.get("cover", "")
                    p["date"] = p.get("date", "2026-10-02")
                    p["site"] = p.get("site", "default")
                    p["categories"] = p.get("categories", ["crypto"])
                    p["format"] = p.get("format", "standard")
                    p["bodyClass"] = p.get("bodyClass", DEFAULT_BODY_CLASS)
                    found = True
                    break

            if not found:
                manifest["posts"].append({
                    "slug": slug, "title": title, "excerpt": "", "cover": "",
                    "date": "2026-10-02", "site": "default", "categories": ["crypto"],
                    "format": "standard", "bodyClass": DEFAULT_BODY_CLASS,
                    "file": f"posts/{filename}", "path": f"/{slug}/"
                })

    os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Done. Total posts: {len(manifest['posts'])}")

if __name__ == "__main__":
    main()
