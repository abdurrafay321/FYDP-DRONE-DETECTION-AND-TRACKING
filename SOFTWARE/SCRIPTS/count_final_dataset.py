from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "FINAL DATASET"

train_images = len(list((ROOT / "images" / "train").glob("*.*")))
val_images = len(list((ROOT / "images" / "val").glob("*.*")))
test_images = len(list((ROOT / "images" / "test").glob("*.*")))

train_labels = len(list((ROOT / "labels" / "train").glob("*.txt")))
val_labels = len(list((ROOT / "labels" / "val").glob("*.txt")))
test_labels = len(list((ROOT / "labels" / "test").glob("*.txt")))

print("TRAIN IMAGES :", train_images)
print("TRAIN LABELS :", train_labels)

print("VAL IMAGES   :", val_images)
print("VAL LABELS   :", val_labels)

print("TEST IMAGES  :", test_images)
print("TEST LABELS  :", test_labels)