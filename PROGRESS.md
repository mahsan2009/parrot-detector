# Parrot Detector — Progress Tracker

This file tracks where we are. Each session, read the top to remember what's done.

**Project:** Detect 3 pet cockatiels (Cookie, Nona, White-tota) individually on webcam + in image/video folders. Runs locally + free.

---

## Current position
> **Phase 0 — Setup · Step 3: Install git + learn version control**

## Phase checklist
- [ ] **Phase 0 — Setup**: terminal basics, GPU check, uv virtual environment, git + GitHub, first commit
  - [x] Step 1: Confirm NVIDIA GPU with `nvidia-smi`  → RTX 3060, 12 GB, CUDA 13.3 driver ✅
  - [x] Step 2: Understand uv + create the project virtual environment (.venv, Python 3.12.13) ✅
  - [ ] Step 3: Install git, explain version control  ← *you are here*
  - [ ] Step 4: Create GitHub account/repo
  - [ ] Step 5: First commit + push
- [ ] **Phase 1 — Project plan & structure** (folders, README, .gitignore)
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
