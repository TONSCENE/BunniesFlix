#!/usr/bin/env python3
import subprocess
import os
import sys

REPO_URL = "https://github.com/TONSCENE/BunniesFlix"
PAGES_URL = "https://tonscene.github.io/BunniesFlix/"

def deploy(msg="Update BunniesFlix"):
    print(f"🚀 Deploying BunniesFlix to GitHub Pages ({PAGES_URL})...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        subprocess.run(["git", "add", "index.html", "db.js", "bilibili_db.js", "bilibili_archives.json", "images/", "deploy.py"], check=True)
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            subprocess.run(["git", "commit", "-m", msg], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"✅ Pushed changes to GitHub ({REPO_URL})")
        else:
            print("ℹ️ No new changes to commit.")
        print(f"🎉 Live now at: {PAGES_URL}")
    except Exception as e:
        print(f"❌ Deploy error: {e}")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Update BunniesFlix content"
    deploy(msg)
