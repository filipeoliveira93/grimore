#!/usr/bin/env python3
import os
import shutil
from datetime import datetime

def cleanup_logs():
    log_dir = ".sdd-toolkit/logs"
    archive_dir = ".sdd-toolkit/logs/archive"
    
    if not os.path.exists(log_dir):
        return

    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    logs = [f for f in os.listdir(log_dir) if os.path.isfile(os.path.join(log_dir, f)) and f.endswith(".md")]
    
    for log_file in logs:
        shutil.move(os.path.join(log_dir, log_file), os.path.join(archive_dir, log_file))
        print(f"Archived: {log_file}")

if __name__ == "__main__":
    cleanup_logs()
