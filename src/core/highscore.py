import json
import os

from src.core.constants import *


os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump({"highscore": 0, "pacifist_highscore": 0 }, f)

def load_highscore() -> tuple[int,int]:
    data = {"highscore": 0, "pacifist_highscore": 0}

    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r") as f:
                loaded = json.load(f)
                data.update(loaded)
        except (json.JSONDecodeError, IOError):
            pass

    normal = data.get("highscore", 0)
    pacifist = data.get("pacifist_highscore",0)

    return normal,pacifist


def save_highscore(score, pacifist=False) -> None:
    current, pacifist_current = load_highscore()
    new_data = {
        "highscore": current,
        "pacifist_highscore": pacifist_current,
    }

    if pacifist:
        new_data["pacifist_highscore"] = score
    else:
        new_data["highscore"] = score

    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(new_data, f)


def update_highscore(score: int, time, pacifist_mode=False) -> bool:
    current,pacifist_current = load_highscore()

    if pacifist_mode and time > pacifist_current:
        save_highscore(time,pacifist_mode)
        return True
    if score > current:
        save_highscore(score,pacifist_mode)
        return True
    return false