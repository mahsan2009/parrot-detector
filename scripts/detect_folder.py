"""Batch parrot detection — run the model over a folder of images/videos and SAVE labeled copies.

Example (run on the 23 held-out test images):
    python scripts/detect_folder.py --source data/dataset/images/test

The annotated results are written into the --out folder (default: outputs/results).
"""
import argparse
from ultralytics import YOLO

# 1) Options: which folder to read, where to save, and how sure the model must be.
parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True,
                    help="folder (or single file) of images/videos to run on")
parser.add_argument("--out", default="outputs",
                    help="folder where labeled results are saved")
parser.add_argument("--conf", type=float, default=0.5,
                    help="confidence threshold 0-1: only keep guesses at least this sure")
args = parser.parse_args()

# 2) Load our trained model.
model = YOLO("models/parrot_best.pt")

# 3) Run detection on everything in the source folder.
#    save=True writes annotated copies; it auto-handles images AND videos.
model.predict(
    source=args.source,
    conf=args.conf,
    save=True,
    project=args.out,
    name="results",
    exist_ok=True,   # reuse the same output folder instead of making results2, results3...
    verbose=True,
)

print(f"Done. Labeled results saved under: {args.out}/results")
