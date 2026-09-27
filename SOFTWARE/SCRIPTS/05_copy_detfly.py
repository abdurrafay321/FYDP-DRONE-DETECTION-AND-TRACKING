from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DETFLY = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "drones" / "det_fly" / "images"
FINAL = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "FINAL DATASET"

train_count = 0
val_count = 0
test_count = 0

# ==========================
# TRAIN
# ==========================

for img in (DETFLY / "train" / "images").glob("*.*"):

    label = DETFLY / "train" / "labels" / f"{img.stem}.txt"

    if label.exists():

        shutil.copy(
            img,
            FINAL / "images" / "train" / img.name
        )

        shutil.copy(
            label,
            FINAL / "labels" / "train" / label.name
        )

        train_count += 1

# ==========================
# VALID
# ==========================

for img in (DETFLY / "valid" / "images").glob("*.*"):

    label = DETFLY / "valid" / "labels" / f"{img.stem}.txt"

    if label.exists():

        shutil.copy(
            img,
            FINAL / "images" / "val" / img.name
        )

        shutil.copy(
            label,
            FINAL / "labels" / "val" / label.name
        )

        val_count += 1

# ==========================
# TEST
# ==========================

for img in (DETFLY / "test" / "images").glob("*.*"):

    label = DETFLY / "test" / "labels" / f"{img.stem}.txt"

    if label.exists():

        shutil.copy(
            img,
            FINAL / "images" / "test" / img.name
        )

        shutil.copy(
            label,
            FINAL / "labels" / "test" / label.name
        )

        test_count += 1

print("Train:", train_count)
print("Val:", val_count)
print("Test:", test_count)