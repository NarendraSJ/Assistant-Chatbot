import json
import os

def save_submission(data, filename="submissions.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open(filename, "w") as f:
        json.dump(existing, f, indent=2)
