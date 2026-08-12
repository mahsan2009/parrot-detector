# Parrot Detector learning log

This file is the project's memory. Read the latest entry before starting a new session. Do not try to memorize every line of code; remember the main ideas, then use this log and the notebook to recover the details.

## Start-of-session routine (2–5 minutes)

1. Read the latest entry under **Session checkpoints**.
2. Without looking, answer its recall questions out loud or in a message.
3. Open the recorded notebook and rerun or inspect the last successful cell.
4. Continue from the recorded **Next step**.

## Core mental model

- `pyproject.toml`: the project's library requirements (the shopping list).
- `uv.lock`: the exact resolved library versions (the receipt).
- `.venv`: the isolated Python and installed libraries (the toolbox).
- `uv run ...`: run a command with this project's toolbox.
- Notebook Markdown: explanations for humans.
- Notebook code cells: instructions Python executes.
- Dataset: the images and annotations used as examples.

## Glossary

### Classification

One image or crop goes into the model; one class is chosen.

### Detection

One full image goes into the model; the model returns zero or more boxes, confidence scores, and class labels.

### Logits

Raw model scores. They may be negative and do not add up to 100%. Softmax converts logits into probabilities that add up to approximately 100%.

### Segmentation mask

An image-sized label map that says which category each pixel belongs to. In Oxford-IIIT Pet: `1` is animal, `2` is background, and `3` is the boundary.

### Bounding box

A rectangle written as `(x1, y1, x2, y2)`. In this project, we derive it from the segmentation mask by finding the minimum and maximum coordinates of non-background pixels.

### Train, validation, and test

- Train: examples used to change model weights.
- Validation: examples used to choose settings and the best checkpoint.
- Test: the untouched final exam, used only after choices are frozen.

## Session checkpoints

### 2026-07-21 — Notebook 1 EDA complete

Completed:

- Recalled weights, backpropagation, logits, softmax, augmentation, overfitting, masks, boxes, and the train/validation/test roles.
- Successfully ran the repaired EDA notebook through all 584 valid masks.
- Confirmed final counts: train `80/80/72`, validation `20/20/18`, test `98/100/96` for Abyssinian/Bengal/Egyptian Mau.
- Calculated mask-derived boxes for `584/584` valid images.
- Interpreted count, box-area-fraction, and box-aspect-ratio distributions.
- Inspected three crops per class and identified appearance cues plus background-shortcut risks.
- Reached the written EDA conclusion: training support is mildly imbalanced, only 1.7% of boxes cover under 20% of an image, and the hardest class cannot be known before validation predictions exist.

Important observations:

- Bengal samples often have orange/brown coats with bold spots or stripes.
- Egyptian Mau samples often have grey/silver coats with dark markings.
- Abyssinian samples show colour variation and may overlap visually with Bengal.
- Typical animal boxes cover roughly 60–75% of their images.
- Crops still contain background, so the classifier may learn background shortcuts.
- Aspect ratio is `box_width / box_height`; it describes shape, not raw pixel width.

Next step:

1. Save Notebook 1 in VS Code.
2. Review the tracked changes and create the first Part 2 Git checkpoint when authorized.
3. Begin Notebook 2: save reproducible crops and metadata, define train-only augmentation, and build `PetCropDataset`.

Recall questions:

1. Why is median usually more representative than maximum?
2. What does an aspect ratio greater than 1 mean?
3. Why can backgrounds inside a crop cause overfitting?
4. Why can the hardest class be identified only after validation predictions exist?

### 2026-07-16 — End-of-day checkpoint: data validation and kernel repair

Completed:

- Understood that training data changes weights, validation guides development choices, and test data is the untouched final exam.
- Learned the meanings of weights, backpropagation, augmentation, and overfitting.
- Created a deterministic, stratified train/validation split with `random_state=42`.
- Passed file-level checks for split overlap, duplicates, missing classes, images, and masks.
- Discovered a real content-level annotation defect: four Egyptian Mau masks contain only background pixels.
- Updated the notebook to report and exclude `Egyptian_Mau_162`, `Egyptian_Mau_165`, `Egyptian_Mau_196`, and `Egyptian_Mau_20` before splitting.
- Diagnosed VS Code's permanently spinning Jupyter cell. The project Python/PyTorch imports were healthy, but VS Code was probing a missing `pip` module and several orphan kernels existed.
- Stopped only the orphan notebook processes, added `pip` and `ipywidgets`, synced the environment, and re-registered `ParrotDetector`.
- Verified: pip 26.1.2, ipykernel 7.3.0, ipywidgets 8.1.8, and CPU PyTorch 2.13.0.

Current expected valid-data counts:

- Train: Abyssinian 80, Bengal 80, Egyptian Mau 72.
- Validation: Abyssinian 20, Bengal 20, Egyptian Mau 18.
- Test: Abyssinian 98, Bengal 100, Egyptian Mau 96.
- Total: 584 valid images.

Next step tomorrow:

1. Open VS Code and `notebooks/01_classification_eda.ipynb`.
2. Select the `ParrotDetector` kernel.
3. Run the first import/environment code cell and confirm it finishes.
4. Run cells from top to bottom (or use **Run All Above** when resuming later).
5. Confirm the notebook reports four excluded masks, `Total selected images: 584`, and the revised integrity message mentioning invalid masks.
6. Run the mask-to-box cell and confirm `Reading masks` reaches `584/584`.

Recall questions:

1. What is the difference between logits and softmax probabilities?
2. Which dataset split directly changes model weights?
3. Why did file-existence checks fail to catch the four bad masks?
4. Why must notebook cells be rerun after a laptop shutdown even when old output is still visible?

### 2026-07-16 — Environment, public data, and annotation parsing

Completed:

- Installed `uv` and Python 3.12.
- Created the CPU-only `.venv` with PyTorch 2.13 and Torchvision 0.28.
- Registered/selected the `parrotdetector` Jupyter kernel.
- Downloaded Oxford-IIIT Pet: 3,680 official trainval images and 3,669 official test images.
- Selected learning classes: Abyssinian, Bengal, and Egyptian Mau.
- Opened `notebooks/01_classification_eda.ipynb`.
- Passed the path/data preflight check.
- Parsed the official annotation text files into Pandas tables.

What the latest table means:

- Each row describes one image.
- `image_id` is its unique name without the file extension.
- `class_name` is the human-readable breed.
- Numeric IDs are zero-based because Python commonly counts from zero.
- `image_path` points to the color image.
- `mask_path` points to its pixel-level segmentation annotation.
- `head()` displayed the first five rows; it did not reduce the full dataset to five rows.

Next step:

Read **Select three classes and create validation data**, then run its code cell. Inspect the train/validation/test counts table before continuing.

Recall questions:

1. Which values add up to approximately 100%: logits or softmax probabilities?
2. What is more precise: a segmentation mask or a bounding box?
3. Why do we need a validation set in addition to training and test sets?
4. What does one row in the annotation table represent?

## End-of-session routine (2–5 minutes)

Before stopping, update or ask Codex to update this file with:

- what was completed;
- the last successful notebook cell;
- the next exact step;
- new vocabulary in plain language;
- two to four recall questions.
