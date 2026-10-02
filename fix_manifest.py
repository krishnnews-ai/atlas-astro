#!/usr/bin/env python3
"""
Quick fix: Update manifest.json with generated posts
"""
import os
import json

POSTS_DIR = "src/generated/posts"
MANIFEST_FILE = "src/data/manifest.json"

def main():
    print("🔧 Fixing manifest.json...")

    # Purana manifest load kar
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            try:
                manifest = json.load(f)
            except:
                manifest = {}
    else:
        manifest = {}

    # Ensure structure
    if "posts" not in manifest or not isinstance(manifest["posts"], list):
        manifest["posts"] = []
    if "pages" not in manifest or not isinstance(manifest["pages"], list):
        manifest["pages"] = []

    # Sirf dict wale entries rakho
    manifest["posts"] = [p for p in manifest["posts"] if isinstance(p, dict)]
    manifest["pages"] = [p for p in manifest["pages"] if isinstance(p, dict)]

    # Posts folder se saari .html files list kar
    if os.path.exists(POSTS_DIR):
        files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
        print(f"📁 Found {len(files)} post files")

        for filename in files:
            slug = filename[:-5]  # .html hatao

            # Check karo already manifest me hai?
            already = any(p.get("slug") == slug for p in manifest["posts"])

            if not already:
                manifest["posts"].append({
                    "slug": slug,
                    "title": slug.replace("-", " ").title(),
                    "file": f"posts/{filename}",
                    "path": f"/{slug}/"
                })

    # Save manifest
    os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✅ Manifest updated!")
    print(f"   📝 Total posts: {len(manifest['posts'])}")
    print(f"   📄 Total pages: {len(manifest['pages'])}")

if __name__ == "__main__":
    main()