import json
import os
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.json"
MAX_LEADERBOARD_ENTRIES = 10

def load_leaderboard():
    """
    Load leaderboard from disk
    Returns a list of dicts sorted by rounds descending
    """

    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        pass
    return []

def save_score(name: str, survived: int):
    """ 
    Append new entry to leaderboard and save
    Keeps only top MAX_LEADERBOARD_ENTRIES entries sorted by rounds descending
    Returns updated leaderboard
    """

    entries = load_leaderboard()

    entry = {
        "name": name.strip() or "Anonymous",
        "rounds": survived,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    entries.append(entry)

    entries.sort(key=lambda x: x["rounds"])
    entries = entries[:MAX_LEADERBOARD_ENTRIES]

    try:
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(entries, f, indent=2)
    except IOError as e:
        print(f"Error saving leaderboard: {e}")

    return entries

def get_rank(survived: int):
    """
    Get rank for a given rounds survived
    Returns 1-based rank or None if not in top leaderboard
    """

    entries = load_leaderboard()
    rank = sum(1 for e in entries if e["rounds"] > survived) + 1
    return rank