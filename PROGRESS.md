# Parrot Detector — Progress Tracker

This file tracks where we are. Each session, read the top to remember what's done.

**Project:** Detect 3 pet cockatiels (Cookie, Nona, White-tota) individually on webcam + in image/video folders. Runs locally + free.

---

## Current position
> **Phase 1 COMPLETE ✅ → next: Phase 2 — Data collection (filming + ffmpeg frames)**
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
- [ ] **Phase 2 — Data collection** (filming tips, avoid background trap, ffmpeg frames)
- [ ] **Phase 3 — Annotation** (Label Studio, bounding boxes, export YOLO format)
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
- Dependencies tracked via **pyproject.toml** + **uv.lock** (set up early via `uv init`). Add libraries with `uv add <name>`.
- Jupyter notebooks enabled in the venv via **ipykernel**; experiment notebooks live in notebooks/.
- `main.py` is the default `uv init` stub (harmless); notebooks/test.ipynb is a scratch test.
