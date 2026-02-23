#!/usr/bin/env python3
import os
import re
from datetime import datetime

def generate_changelog():
    log_dir = ".sdd-toolkit/logs"
    changelog_path = "CHANGELOG.md"
    
    if not os.path.exists(log_dir):
        print(f"Directory {log_dir} not found. Skipping changelog generation.")
        return

    logs = sorted([f for f in os.listdir(log_dir) if f.endswith(".md")], reverse=True)
    
    with open(changelog_path, "a") as changelog:
        changelog.write(f"\n## [{datetime.now().strftime('%Y-%m-%d')}]\n")
        
        for log_file in logs:
            file_path = os.path.join(log_dir, log_file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Find task summary or title
                match = re.search(r"# (.*)", content)
                if match:
                    title = match.group(1).strip()
                    changelog.write(f"- {title}\n")
    
    print(f"Changelog updated at {changelog_path}")

if __name__ == "__main__":
    generate_changelog()
