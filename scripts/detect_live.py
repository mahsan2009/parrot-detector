"""Live parrot detection — read a camera OR a video file and draw each parrot's name on screen.

Examples:
    # run on a recorded video file (no webcam needed):
    python scripts/detect_live.py --source data/raw_videos/WhiteTotaOnTopOfCage.MOV

    # run on the default webcam (camera 0), if you have/connect one:
    python scripts/detect_live.py --source 0

Press the Q key in the video window to quit.
"""
import argparse
import cv2
from ultralytics import YOLO

# 1) Read the command-line options (with sensible defaults).
parser = argparse.ArgumentParser()
parser.add_argument("--source", default="0",
                    help="camera index like 0 or 1, OR a path to a video file")
parser.add_argument("--conf", type=float, default=0.5,
                    help="confidence threshold 0-1: only show guesses at least this sure")
args = parser.parse_args()

# A plain number means a camera index; anything else is treated as a file path.
source = int(args.source) if args.source.isdigit() else args.source

# 2) Load our trained model.
model = YOLO("models/parrot_best.pt")

# 3) Open the video source (camera or file).
cap = cv2.VideoCapture(source)
if not cap.isOpened():
    print(f"Could not open source: {source}")
    raise SystemExit

print("Running... press Q in the window to quit.")

# 4) Loop: read one frame at a time until the video ends or you quit.
while True:
    ok, frame = cap.read()
    if not ok:
        break  # no more frames (video ended) or camera error

    # 5) Run the model on this single frame.
    #    conf=... hides low-confidence guesses (helps with the 'false alarm' issue).
    results = model(frame, conf=args.conf, verbose=False)

    # 6) Draw the boxes + bird names onto the frame (Ultralytics does this for us).
    annotated = results[0].plot()

    # 7) Show the result in a window.
    cv2.imshow("Parrot Detector (press Q to quit)", annotated)

    # 8) Wait 1 ms for a key press; if it's 'q', stop the loop.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 9) Clean up: release the camera/file and close the window.
cap.release()
cv2.destroyAllWindows()
