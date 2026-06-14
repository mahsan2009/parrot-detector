# 🦜 Parrot Detector

A computer-vision system that detects my three pet cockatiels **individually** and labels each one by
name — live on a webcam and as a batch over a folder of images/videos. Everything runs **locally** and
uses **free** tools.

> ⚠️ **Status: Work in progress.** This project is being built step by step as a first end-to-end machine
> learning project. Sections marked _coming soon_ will be filled in as the project progresses.

---

## The problem

I have three cockatiels — **Cookie**, **Nona**, and **White-tota**. They are the *same species* and look
fairly similar, so telling them apart by name is a genuine "fine-grained" recognition challenge. The goal
is a model that can look at a camera feed (or a folder of photos/videos) and draw a labeled box around
each bird with the correct name.

## What it does (planned)

- 🎥 **Live webcam mode** — point a camera at the birds and see each one boxed and named in real time.
- 🗂️ **Batch mode** — run it over a folder of images/videos and get labeled outputs.
- 💻 **Runs locally** on an NVIDIA GPU; no cloud or paid services required.

## Tech stack

| Tool | What it's for |
| --- | --- |
| **Python 3.12** + **uv** | Language + environment/package manager |
| **Ultralytics YOLO** | The object-detection model (training + detection) |
| **PyTorch (CUDA)** | The engine YOLO runs on, using the GPU |
| **OpenCV** | Reading the webcam and drawing boxes/labels |
| **ffmpeg** | Pulling still frames out of videos |
| **Label Studio** | Drawing the training labels (bounding boxes) by hand |
| **git + GitHub** | Version control and hosting |

## Project structure

```
parrot-detector/
├── data/
│   ├── raw_videos/   # original videos of the birds
│   └── frames/       # still images extracted from the videos
├── scripts/          # Python programs (webcam detection, batch, frame extraction)
├── models/           # trained model files
├── notebooks/        # experiments
├── README.md         # this file
├── PROGRESS.md       # step-by-step progress tracker
└── .gitignore        # files git should ignore
```

## The classes (birds)

| Label | Bird |
| --- | --- |
| `Cookie` | Cookie 🐦 |
| `Nona` | Nona 🐦 |
| `White-tota` | White-tota 🐦 |

## Results

_Coming soon — model accuracy and a confusion matrix will go here after training (Phase 6)._

## Demo

_Coming soon — a screenshot/GIF of live detection will go here (Phase 8)._

## How to run

_Coming soon — setup and run instructions will be written once the detection scripts exist (Phase 7–8)._

---

_Built as a learning project, one phase at a time. See `PROGRESS.md` for the current status._
