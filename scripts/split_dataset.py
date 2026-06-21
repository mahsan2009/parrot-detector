"""Split the labeled dataset into train/val/test BY RECORDING SESSION.

Why by session? Frames from the same video clip are near-identical. If we split
randomly, near-duplicate frames could land in BOTH training and test, letting the
model "cheat" on its exam. Keeping each whole clip (a "session") in ONE split gives
an honest score on footage the model has never seen.

Run from the project root (with the venv active):
    python scripts/split_dataset.py
"""
import re
import shutil
from pathlib import Path

# --- folders ---
SRC = Path("data/label_export")   # the unzipped Label Studio export (images/ + labels/)
OUT = Path("data/dataset")        # where the YOLO-ready split will be created

# --- which clips become the final exam (test) and the practice quizzes (val) ---
# Any clip NOT listed here goes into the training set.
TEST_SESSIONS = {
    "CookieOnTowel", "CookieOnCage",
    "NonaTryingToEatCage",
    "WhiteTotaTryingToGetOut",
}
VAL_SESSIONS = {
    "CookieSitting", "CookieChilling",
    "NonaChilling", "NonaDenyingFood",
    "WhiteTotaClimbing", "WhiteTotaChilling",
}


def session_of(stem: str) -> str:
    """'0095ada7-WhiteTotaTryingToGetOut_001' -> 'WhiteTotaTryingToGetOut'."""
    no_hash = re.sub(r"^[^-]+-", "", stem)   # drop the 'hash-' prefix Label Studio added
    return re.sub(r"_\d+$", "", no_hash)     # drop the '_001' frame number


def split_for(session: str) -> str:
    if session in TEST_SESSIONS:
        return "test"
    if session in VAL_SESSIONS:
        return "val"
    return "train"


# --- create the output folder structure YOLO expects ---
for split in ("train", "val", "test"):
    (OUT / "images" / split).mkdir(parents=True, exist_ok=True)
    (OUT / "labels" / split).mkdir(parents=True, exist_ok=True)

counts = {"train": 0, "val": 0, "test": 0}
missing_labels = []

for img in sorted((SRC / "images").glob("*.jpg")):
    split = split_for(session_of(img.stem))

    # copy the image into images/<split>/
    shutil.copy(img, OUT / "images" / split / img.name)

    # copy its matching label into labels/<split>/ (same name, .txt)
    label = SRC / "labels" / (img.stem + ".txt")
    if label.exists():
        shutil.copy(label, OUT / "labels" / split / label.name)
    else:
        missing_labels.append(img.name)

    counts[split] += 1

print("Done. Frames per split:")
for split in ("train", "val", "test"):
    print(f"  {split:5s}: {counts[split]}")
print(f"  TOTAL: {sum(counts.values())}")
if missing_labels:
    print(f"WARNING: {len(missing_labels)} image(s) had no label file:")
    for name in missing_labels:
        print("   ", name)
