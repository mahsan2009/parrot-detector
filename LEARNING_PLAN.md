# Part 2 learning plan — PyTorch from first principles

## Goal

Learn what a computer-vision pipeline is doing instead of only calling a high-level YOLO command. We will first solve **classification**, then **detection**, and compare their data and raw model outputs.

The unavailable private parrot data is replaced for this learning track by the public **Oxford-IIIT Pet Dataset**. We use three visually similar cat breeds:

- `Abyssinian`
- `Bengal`
- `Egyptian_Mau`

This is still a fine-grained recognition problem: the model must distinguish visually similar categories. The dataset provides category labels and segmentation masks. We can turn each mask into a bounding box, so the same images support classification crops and detection.

Dataset source: <https://www.robots.ox.ac.uk/~vgg/data/pets/>

License: Creative Commons Attribution-ShareAlike 4.0. Image copyright remains with the original owners.

## Current computer constraints

This checkout is on a different Windows laptop from Part 1:

- Intel Core i7-1165G7 CPU
- Intel Iris Xe integrated graphics (not a CUDA device)
- 8 GB RAM

Therefore PyTorch uses its official **CPU build**. EDA, data preparation, inference, and the small CNN are suitable locally. Use small batches (start at 8 or 16), `num_workers=0`, short experimental runs, and close memory-heavy programs. ResNet18 can still train, but slowly. Full detector fine-tuning is an optional short/subset exercise locally or can move to free Colab after the local code is understood and tested.

## Important corrections to the original continuation plan

1. **Add a data-acquisition and license step.** The old plan began by assuming ignored local files existed.
2. **Replace session splitting.** Public images do not have recording sessions. We keep the official test split untouched and make a seeded, stratified train/validation split from the official `trainval` set.
3. **Do not reuse the test set while developing.** Choose transforms, models, epochs, and confidence thresholds with validation data. Run the test evaluation only after those choices are frozen.
4. **Create a baseline.** Compare learned models with a majority-class baseline. Accuracy without context can mislead.
5. **Validate annotations.** Check missing images/masks, empty masks, invalid class IDs, zero-area boxes, boxes outside images, duplicates, and split overlap.
6. **Prevent background shortcuts.** Compare full-image classification with mask-derived crops and inspect whether backgrounds correlate with a class.
7. **Make experiments reproducible.** Record a random seed, package versions, selected classes, split membership, transforms, and model configuration.
8. **Save complete checkpoints.** Save model weights plus architecture name, class-to-ID mapping, image size, normalization, epoch, and validation score.
9. **Report more than overall accuracy.** Include per-class precision, recall, F1, confusion matrix, and error examples.
10. **Handle forced guesses.** A three-class softmax classifier always chooses one class, even for a bad detector crop. Tune an optional `unknown` threshold on validation data and explain its limits.
11. **Move stable logic into scripts early.** Notebooks are for explanation and experiments; shared parsing, splitting, datasets, training, and metrics should become importable Python modules once proven.
12. **Acknowledge the single-object limitation.** Oxford-IIIT Pet images usually contain one main animal. Detection still teaches boxes and outputs, but a later synthetic collage or small multi-object dataset exercise is needed to demonstrate multiple objects per image.
13. **Remember the detector background label.** Torchvision detectors reserve label `0` for background, so the three visible classes must use labels `1`, `2`, and `3`.
14. **Separate model selection from final reporting.** “Best model” means best validation result; the test set estimates how that already-chosen model generalizes.

## Stage 0 — Reproducible setup and data

- [x] Record all Python dependencies in `pyproject.toml`.
- [x] Ignore downloaded data, generated crops, reports, runs, and model weights.
- [x] Create/sync the CPU-only `.venv` from `uv.lock` and register the `parrotdetector` Jupyter kernel.
- [x] Download Oxford-IIIT Pet through Torchvision.
- [x] Verify archive contents and dataset license/source.
- [ ] Select the three classes and write deterministic split metadata.

## Stage A — Classification

### Notebook 1: EDA and annotation understanding ✅ complete

- Inspect Python, PyTorch, Torchvision, CUDA, and paths.
- Parse official split files and explain each column.
- Convert segmentation masks to pixel bounding boxes.
- Count examples by split and class; verify no overlap.
- Inspect image sizes, box sizes, aspect ratios, and sample crops.
- Write a short conclusion about imbalance, shortcuts, and likely failure cases.

### Notebook 2: data preparation and augmentation

- Save crops to `data/classification_crops/{train,val,test}/{class_name}/`.
- Save `metadata.csv` with source, mask, crop, split, class, and pixel box.
- Build `PetCropDataset` returning `(image_tensor, label_id)`.
- Use 224×224 inputs.
- Apply mild augmentation only to training data.
- Normalize with ImageNet statistics when using pretrained ResNet18.
- Start with `batch_size=16` and `num_workers=0` on this 8 GB Windows laptop.

### Notebook 3: models and raw outputs

- Build a small CNN manually.
- Load pretrained ResNet18 and replace its final layer.
- Confirm input shape `[batch, 3, 224, 224]` and output shape `[batch, 3]`.
- Explain logits, softmax probabilities, predicted IDs, and class names.
- Measure the majority-class baseline.

### Notebook 4: training loop

- Hand-write forward pass, loss, zeroing gradients, backward pass, and optimizer step.
- Use `CrossEntropyLoss`.
- First train a frozen ResNet head, then optionally fine-tune later layers.
- Start with 3–5 epochs as a pipeline check; increase only after timing one epoch.
- Track train/validation loss, accuracy, and macro F1.
- Add early stopping and save a complete best-validation checkpoint.

### Notebook 5: final evaluation

- Freeze all choices before touching test data.
- Report accuracy, per-class precision/recall/F1, confusion matrix, and errors.
- Show logits → softmax → predicted class.
- Compare full-image and crop-based classification if time permits.
- Compare classification with Part 1 YOLO in plain language.

### Notebook 6: inference

- Classify one known crop.
- Convert a mask or detector box into a crop, then classify it.
- Add a validation-tuned optional `unknown` threshold.
- Process a video file after still-image inference works.

## Stage B — Detection

- Inspect a high-level detector's `boxes`, `scores`, and `labels`, then draw boxes manually with OpenCV.
- Build a Torchvision detection dataset returning `(image_tensor, target_dict)`.
- Include absolute `xyxy` boxes, labels `1..3`, `image_id`, `area`, and `iscrowd`.
- Fine-tune a small Torchvision detector on a reduced subset/short run locally, or optionally use Colab for the finalized run.
- Explain why prediction output is a list of dictionaries rather than one logits matrix.
- Evaluate with IoU-based detection metrics, not classification accuracy.
- Finish with a multi-object exercise so one image can produce several predictions.

## Definition of done

Every notebook must restart and run top-to-bottom without hidden state. Each generated artifact must be reproducible from tracked code plus the documented public download. The test split is evaluated once per finalized experiment, and limitations are reported honestly.
