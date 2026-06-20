# Parrot Detector — Progress Tracker

This file tracks where we are. Each session, read the top to remember what's done.

**Project:** Detect 3 pet cockatiels (Cookie, Nona, White-tota) individually on webcam + in image/video folders. Runs locally + free.

---

## Current position
> **Phase 3 COMPLETE ✅ → next: Phase 4 — Data pipeline (YOLO folders + split by session)**
> Dataset: 231 frames; 227 labeled, 4 skipped. YOLO export zip in Downloads:
>   project-3-at-2026-06-20-16-50-636539de.zip (classes.txt + images/ + labels/). Filenames keep session prefix.
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
- [ ] **Phase 4 — Data pipeline** (YOLO folder layout, split by session, data config)
- [ ] **Phase 5 — Training & experiments** (CUDA PyTorch, YOLO, compare small models)
- [ ] **Phase 6 — Evaluation & comparison** (confusion matrix, pick winner)
- [ ] **Phase 7 — Deployment** (webcam script + batch folder script)
- [ ] **Phase 8 — Portfolio polish** (README, demo, push to GitHub)

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
