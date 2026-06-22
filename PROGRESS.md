# Parrot Detector — Progress Tracker

This file tracks where we are. Each session, read the top to remember what's done.

**Project:** Detect 3 pet cockatiels (Cookie, Nona, White-tota) individually on webcam + in image/video folders. Runs locally + free.

---

## Current position
> **Phase 6 COMPLETE ✅ → next: Phase 7 — Deployment (webcam + batch scripts)**
> Decision: deploy current winner (Exp B) to finish the pipeline; improve with MORE DATA later (v2).
> Winner model: runs/detect/expB_small_pretrained/weights/best.pt (val 0.981, honest test 0.322).
> Installed: torch 2.12.1+cu130 (GPU OK), ultralytics 8.4.72, opencv. GPU: RTX 3060. (use workers=2)
> Dataset split BY SESSION: train 160 / val 44 / test 23 (all in data/dataset, YOLO layout).
> Config: data.yaml (classes 0 Cookie, 1 Nona, 2 White-tota). Split script: scripts/split_dataset.py.
> Repo live at: https://github.com/mahsan2009/parrot-detector

## Phase checklist
- [x] **Phase 0 — Setup** ✅ terminal basics, GPU check, uv venv, git + GitHub, first commit + push
  - [x] Step 1: Confirm NVIDIA GPU with `nvidia-smi`  → RTX 3060, 12 GB, CUDA 13.3 driver ✅
  - [x] Step 2: Understand uv + create the project virtual environment (.venv, Python 3.12.13) ✅
  - [x] Step 3: git ready (2.45.0), repo init, branch `main`, .gitignore, FIRST COMMIT 489ed8e ✅
  - [x] Step 4: Pushed to GitHub → https://github.com/mahsan2009/parrot-detector ✅
- [x] **Phase 1 — Project plan & structure** ✅ (folders, README, .gitignore)
  - [x] Step 1: Create the project folder structure (data/, scripts/, models/, notebooks/ + .gitkeep) ✅
  - [x] Step 2: Write the starter README (classes locked: Cookie, Nona, White-tota) ✅
  - [x] Step 3: Expanded .gitignore for data/models/runs; commit + push ✅
  - [ ] Step 3: Expand .gitignore for data/models; commit + push
- [x] **Phase 2 — Data collection** ✅ (filming, background-trap awareness, ffmpeg frames)
  - [x] Step 1: Filmed all 3 birds across varied spots/sessions (~31 clips total) ✅
  - [x] Step 2: Installed ffmpeg 8.1.1; extracted 231 frames at fps=0.5 (balanced ~77/bird) ✅
- [ ] **Phase 3 — Annotation** (Label Studio, bounding boxes, export YOLO format)  ← *you are here*
  - [x] Step 1: Installed Label Studio via `uv tool install label-studio` ✅
  - [x] Step 2: Launched, created "Parrot Detector" project, 3 labels, imported 231 tasks ✅
  - [x] Step 3: Drew boxes + labeled every visible bird (227 labeled, 4 skipped) ✅
  - [x] Step 4: Exported "YOLO with Images" zip (227 imgs + labels + classes.txt) ✅
- [x] **Phase 4 — Data pipeline** ✅ (YOLO folder layout, split by session, data config)
  - [x] Step 1: Learned train/val/test + why split by session; unzipped export ✅
  - [x] Step 2: scripts/split_dataset.py → split BY SESSION (train 160 / val 44 / test 23) ✅
  - [x] Step 3: Created data.yaml (paths + class names in classes.txt order) ✅
  - [x] Step 4: Verified images=labels per split; test pile has all 3 birds ✅
- [ ] **Phase 5 — Training & experiments** (CUDA PyTorch, YOLO, compare small models)  ← *you are here*
  - [x] Step 1: Installed GPU PyTorch (torch 2.12.1+cu130) + Ultralytics 8.4.72; GPU verified ✅
  - [x] Step 2: Exp A — fine-tuned YOLO nano (overall mAP50 0.93) ✅
  - [x] Step 3: Exp B — fine-tuned YOLO small (overall mAP50 0.981 — best; big Cookie gain) ✅
  - [x] Step 4: Exp C — nano FROM SCRATCH (0.697) — proved transfer learning's value ✅
  - [ ] Step 3: Exp B — fine-tune YOLO small (compare accuracy vs speed)
  - [ ] Step 4: Exp C — nano from scratch (see why transfer learning wins)
- [x] **Phase 6 — Evaluation & comparison** ✅ (read confusion matrix; honest test-set score)
  - [x] Read confusion matrix: birds rarely confused (1 Cookie→Nona); main issue = false alarms
  - [x] Honest test-set eval: mAP50 0.322 → overfitting / needs more varied data
  - [x] Decision: deploy current model now, improve with more data later (v2)
- [ ] **Phase 7 — Deployment** (webcam script + batch folder script)
- [ ] **Phase 8 — Portfolio polish** (README, demo, push to GitHub)

## Experiment results (val mAP50 — higher is better)
| Exp | Model | Notes | Overall | Cookie | Nona | White-tota |
|-----|-------|-------|---------|--------|------|------------|
| A | yolo11n (nano) | pretrained, 100 ep | 0.93 | 0.809 | 0.986 | 0.995 |
| B | yolo11s (small) | pretrained, 100 ep | 0.981 | 0.964 | 0.995 | 0.985 |
| C | yolo11n (nano) | FROM SCRATCH, 100 ep | 0.697 | 0.797 | 0.655 | 0.640 |

WINNER: **Exp B (yolo11s small, pretrained) = 0.981 (val)**. Model at runs/detect/expB_small_pretrained/weights/best.pt
HONEST TEST-SET score (never-seen clips): mAP50 **0.322** (Cookie 0.425, Nona 0.238, White-tota 0.304).
  → Big val→test gap = OVERFITTING / weak generalization. Root cause: not enough DATA VARIETY (too many similar/cage clips).
  → Fix: collect more clips per bird in genuinely different places/lighting/angles, then re-extract → re-label → retrain.
  → Test set is small (23 imgs) so number is noisy, but the gap is real.
Lessons proven: (1) transfer learning huge — A vs C same nano, 0.93 vs 0.697; (2) bigger model lifts hard bird Cookie.
Use workers=2 to avoid RAM crash on Windows.

## Decisions & notes
- OS: Windows 11 (use PowerShell)
- GPU: NVIDIA (train locally; Colab only as fallback)
- Tools: uv (Python/packages), git+GitHub, Label Studio, Ultralytics YOLO, OpenCV, ffmpeg
- Class names (must stay spelled identically everywhere): **Cookie, Nona, White-tota**
- Birds are the same species (cockatiels) → need lots of varied photos; watch confusion matrix closely.
- **Telling Cookie vs Nona apart (label consistently!):** Cookie = slightly DARKER grey; Nona = slightly LIGHTER grey. White-tota = white (easy). This is the hard pair — expect Phase 6 confusion matrix to show any mix-ups here.
- Dependencies tracked via **pyproject.toml** + **uv.lock** (set up early via `uv init`). Add libraries with `uv add <name>`.
- Jupyter notebooks enabled in the venv via **ipykernel**; experiment notebooks live in notebooks/.
- `main.py` is the default `uv init` stub (harmless); notebooks/test.ipynb is a scratch test.
