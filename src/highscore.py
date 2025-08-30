import json
import os
from src.abstractions.constants import *




os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump({"highscore": 0}, f)

def load_highscore() -> int:
    """Load the saved high score, or return 0 if file doesn't exist."""
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            data = json.load(f)
            return data.get("highscore", 0)
    except (json.JSONDecodeError, IOError):
        return 0


def save_highscore(score: int) -> None:
    """Save a new high score, overwriting the old one."""
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump({"highscore": score}, f)


def update_highscore(score: int) -> bool:
    """
    Update the high score if the given score is higher.
    Returns True if a new high score was set, False otherwise.
    """
    current = load_highscore()
    if score > current:
        save_highscore(score)
        return True