from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DETFLY_IMAGES = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "drones" / "det_fly" / "images"
DETFLY_LABELS = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "drones" / "det_fly" / "yolo_labels"
TRAIN_IMG = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "FINAL DATASET" / "images" / "train"
TRAIN_LBL = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "FINAL DATASET" / "labels" / "train"

count = 0

for img in DETFLY_IMAGES.rglob("*.*"):

    if img.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    label = DETFLY_LABELS / f"{img.stem}.txt"

    if not label.exists():
        continue

    shutil.copy(img, TRAIN_IMG / img.name)
    shutil.copy(label, TRAIN_LBL / label.name)

    count += 1

print(f"DetFly copied: {count}")