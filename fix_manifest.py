#!/usr/bin/env python3
"""
Keep ONLY posts that have HTML files in src/generated/posts/
Remove all Atlas demo posts.
"""
import os
import json

MANIFEST_FILE = "src/data/manifest.json"
POSTS_DIR = "src/generated/posts"

def main():
    print("🔧 Loading manifest...")
    
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    # Get all HTML files
    if os.path.exists(POSTS_DIR):
        files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    else:
        files = []
    
    print(f"📁 Found {len(files)} HTML files")
    
    # Valid slugs
    valid_slugs = {f[:-5] for f in files}
    
    old_count = len(manifest.get("posts", []))
    
    # Keep only posts with HTML files
    cleaned = [p for p in manifest.get("posts", []) if p.get("slug") in valid_slugs]
    
    manifest["posts"] = cleaned
    
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Posts: {old_count} → {len(cleaned)}")
    print(f"❌ Removed: {old_count - len(cleaned)} Atlas demo posts")

if __name__ == "__main__":
    main()
