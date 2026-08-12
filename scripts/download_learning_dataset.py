"""Download and verify the public dataset used by the Part 2 learning track.

Run from the project root:
    uv run python scripts/download_learning_dataset.py

Torchvision downloads two official archives (images and annotations), verifies
their MD5 checksums, and extracts them under data/oxford-iiit-pet/.
"""

from collections import Counter
from pathlib import Path

from torchvision.datasets import OxfordIIITPet


DATA_ROOT = Path("data")
SELECTED_CLASSES = ("Abyssinian", "Bengal", "Egyptian Mau")


def main() -> None:
    print("Dataset: Oxford-IIIT Pet")
    print("Source: https://www.robots.ox.ac.uk/~vgg/data/pets/")
    print("License: Creative Commons Attribution-ShareAlike 4.0")
    print("Downloading and checking the official files (first run only)...")

    trainval = OxfordIIITPet(
        root=DATA_ROOT,
        split="trainval",
        target_types="category",
        download=True,
    )
    test = OxfordIIITPet(
        root=DATA_ROOT,
        split="test",
        target_types="category",
        download=True,
    )

    missing = [name for name in SELECTED_CLASSES if name not in trainval.class_to_idx]
    if missing:
        raise RuntimeError(f"Selected classes are missing from the dataset: {missing}")

    annotations = DATA_ROOT / "oxford-iiit-pet" / "annotations"
    trainval_counts = Counter(
        int(line.split()[1]) - 1
        for line in (annotations / "trainval.txt").read_text().splitlines()
    )
    test_counts = Counter(
        int(line.split()[1]) - 1
        for line in (annotations / "test.txt").read_text().splitlines()
    )

    print(f"Official trainval images (all 37 breeds): {len(trainval):,}")
    print(f"Official test images (all 37 breeds):     {len(test):,}")
    print("Selected learning classes:")
    for name in SELECTED_CLASSES:
        original_id = trainval.class_to_idx[name]
        trainval_count = trainval_counts[original_id]
        test_count = test_counts[original_id]
        print(f"  {name:14s} trainval={trainval_count:3d}  test={test_count:3d}")

    dataset_folder = (DATA_ROOT / "oxford-iiit-pet").resolve()
    print(f"Ready: {dataset_folder}")
    print("Next: open notebooks/01_classification_eda.ipynb and run top-to-bottom.")


if __name__ == "__main__":
    main()
