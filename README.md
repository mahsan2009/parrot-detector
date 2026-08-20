# 🦜 Parrot Detector

A computer-vision system that detects my three pet cockatiels **individually** and labels each one by
name — live on a webcam and as a batch over a folder of images/videos. Everything runs **locally** and
uses **free** tools.

> ✅ **Part 1 status: v1 complete** — a working end-to-end YOLO pipeline (data → labels → training →
> evaluation → live & batch detection). The private data and model are not stored in Git.
>
> 📘 **Part 2 status: classification milestone complete** — a reproducible PyTorch learning track using
> the public Oxford-IIIT Pet dataset. A frozen-ResNet18 classifier achieved **82.7% official-test
> accuracy (243/294)** across three cat breeds. See [notebooks](notebooks/) and
> [LEARNING_PLAN.md](LEARNING_PLAN.md).

---

## The problem

I have three cockatiels — **Cookie**, **Nona**, and **White-tota**. They are the *same species* and look
fairly similar, so telling them apart by name is a genuine "fine-grained" recognition challenge. The goal
is a model that can look at a camera feed (or a folder of photos/videos) and draw a labeled box around
each bird with the correct name.

## What it does

- 🎥 **Live mode** (`scripts/detect_live.py`) — reads a webcam *or* a video file and draws each bird's
  name on screen in real time.
- 🗂️ **Batch mode** (`scripts/detect_folder.py`) — runs over a whole folder of images/videos and saves
  labeled copies.
- 💻 **Runs locally** on an NVIDIA GPU; no cloud or paid services required.

## Tech stack

| Tool | What it's for |
| --- | --- |
| **Python 3.12** + **uv** | Language + environment/package manager |
| **Ultralytics YOLO** | The object-detection model (training + detection) |
| **PyTorch** | The model/training engine (CPU in the current learning checkout; CUDA was used for Part 1) |
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

I trained on ~227 hand-labeled frames (split **by recording session** into train/val/test, so the test
set contains entirely unseen clips — an honest measure of generalization).

**Experiments compared** (validation mAP50 — higher is better, max 1.0):

| Experiment | Model | Setup | Overall mAP50 |
| --- | --- | --- | --- |
| A | YOLO11 nano | pretrained (transfer learning) | 0.93 |
| **B** | **YOLO11 small** | **pretrained (transfer learning)** | **0.98** 🏆 |
| C | YOLO11 nano | trained from scratch | 0.70 |

**Takeaways:**
- **Transfer learning matters a lot.** Same nano model, pretrained vs. from scratch: **0.93 vs 0.70**.
- **A bigger model helped the hard case.** The look-alike pair (Cookie/Nona, same colour) is the real
  challenge; the "small" model handled it best, so it's the chosen model.
- **Honest test-set score:** on never-seen clips the winner scored **mAP50 ≈ 0.32** — much lower than the
  validation number. That gap is the model **overfitting** to familiar scenes, and is the reason "more
  varied data" is the main next step. The confusion matrix showed the birds are rarely mistaken for *each
  other*; the main errors are **misses** and **false alarms** on unfamiliar backgrounds.

### Part 2 — PyTorch classification learning track

To learn the core training workflow by hand, I built a three-class cat-breed classifier using the public
Oxford-IIIT Pet dataset: **Abyssinian**, **Bengal**, and **Egyptian Mau**.

| Item | Result |
| --- | --- |
| Model | ImageNet-pretrained ResNet18; frozen feature extractor and new 3-class final layer |
| Training data | 232 mask-derived animal crops |
| Validation data | 58 crops, used for model selection |
| Official test data | 294 untouched crops |
| Selected checkpoint | Epoch 7 |
| Final official-test accuracy | **82.7% (243/294)** |

The selected model scored **82.8%** on validation and **82.7%** on the held-out official test split,
suggesting that its validation result generalised well to unseen images. The main limitation is a
recurring **Egyptian Mau → Bengal** confusion on visually similar spotted or striped cats. The notebooks
show data preparation, augmentation, raw logits, training, validation analysis, checkpoint selection,
and the final test evaluation.

## Demo

![Live detection demo](assets/demo.jpg)

_The detector boxing and naming a bird in a video frame._

## How to run

### Part 2 learning track (works on the current CPU-only Windows laptop)

```powershell
# 1) Reproduce the project environment from pyproject.toml + uv.lock
uv sync

# 2) Download and checksum the public Oxford-IIIT Pet data
uv run python scripts/download_learning_dataset.py

# 3) Open notebooks/01_classification_eda.ipynb and select .venv as its kernel
#    Run the notebooks in numeric order through 08_final_test_evaluation.ipynb
```

`uv` is the package/environment tool. `pyproject.toml` lists what the project needs; `uv.lock` records
the exact resolved versions; `.venv` is the isolated local Python installation. The downloaded public
data is ignored by Git and can always be recreated.

### Part 1 YOLO inference

This requires restoring the ignored `models/parrot_best.pt`. An NVIDIA GPU is optional for inference
but much faster; the original training experiments used one.

```powershell
# Live detection on a video file (or pass --source 0 for a webcam)
uv run python scripts/detect_live.py --source path/to/video.mov

# Batch detection over a folder of images/videos
uv run python scripts/detect_folder.py --source path/to/folder
```

> The trained model (`models/parrot_best.pt`) and the dataset are kept out of git (large files). The
> scripts in `scripts/` document the full pipeline: `split_dataset.py` builds the train/val/test split,
> and the two `detect_*.py` scripts run the model.

## Limitations & future work

This is an honest v1, not a finished product:

- **Generalization gap.** Strong on familiar scenes, weaker on brand-new ones (test mAP50 ≈ 0.32). The
  main fix is **more varied training data** — more clips of each bird in different places, lighting, and
  angles (avoiding the "background trap").
- **Cookie vs. Nona** (same colour) is the hardest pair, as expected for fine-grained recognition.
- **Next steps:** collect a more diverse dataset → re-label → retrain (a "v2"); then re-evaluate on the
  held-out test set to confirm the gap closes.
- **Part 2 classifier:** Egyptian Mau is frequently mistaken for Bengal when coat patterns overlap. A
  larger and more diverse public training subset, or carefully fine-tuning more of ResNet, would be
  reasonable future experiments—but the reported test result is not used to tune the current model.

---

_Built as a learning project, one phase at a time. See `PROGRESS.md` for the current status._
