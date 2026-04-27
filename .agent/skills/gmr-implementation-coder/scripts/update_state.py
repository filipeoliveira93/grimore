#!/usr/bin/env python3
import os
import re
from datetime import datetime

def update_state(task_id, status="completed"):
    state_file = "state.md"
    if not os.path.exists(state_file):
        print("state.md not found.")
        return

    with open(state_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Update task status in a simplified way for the example
    # Usually: - [ ] Task Name -> - [x] Task Name
    pattern = rf"- \[ \] (.*{task_id}.*)"
    new_content = re.sub(pattern, rf"- [x] \1", content)
    
    # Update last updated timestamp
    timestamp_pattern = r"Last Updated: .*"
    new_timestamp = f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    if re.search(timestamp_pattern, new_content):
        new_content = re.sub(timestamp_pattern, new_timestamp, new_content)
    else:
        new_content += f"\n\n---\n{new_timestamp}"

    with open(state_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated status for task {task_id} in {state_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        update_state(sys.argv[1])
    else:
        print("Usage: update_state.py <task_id>")
