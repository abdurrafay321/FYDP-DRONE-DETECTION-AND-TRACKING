from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[2]
NIGHT_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "night" / "Drone.v1i.yolov5pytorch"
WEATHER_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "weather" / "VisioDECT Dataset Upload"
FINAL_DATASET = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "FINAL DATASET"

TRAIN_IMG = FINAL_DATASET / "images" / "train"
VAL_IMG = FINAL_DATASET / "images" / "val"
TEST_IMG = FINAL_DATASET / "images" / "test"

TRAIN_LBL = FINAL_DATASET / "labels" / "train"
VAL_LBL = FINAL_DATASET / "labels" / "val"
TEST_LBL = FINAL_DATASET / "labels" / "test"

for folder in [
    TRAIN_IMG,
    VAL_IMG,
    TEST_IMG,
    TRAIN_LBL,
    VAL_LBL,
    TEST_LBL,
]:
    folder.mkdir(parents=True, exist_ok=True)

print("Folders ready.")

# ===============================
# NIGHT DATASET
# ===============================

night_train_images = NIGHT_ROOT / "train" / "images"
night_train_labels = NIGHT_ROOT / "train" / "labels"

count = 0

for img in night_train_images.glob("*.*"):

    label = night_train_labels / f"{img.stem}.txt"

    if label.exists():

        shutil.copy(img, TRAIN_IMG / img.name)
        shutil.copy(label, TRAIN_LBL / label.name)

        count += 1

print(f"Night train copied: {count}")

# ===============================
# WEATHER DATASET
# ===============================

weather_count = 0

for txt in WEATHER_ROOT.rglob("*.txt"):

    if "labels" not in str(txt):
        continue

    image_name = txt.stem

    image_found = None

    for ext in [".jpg", ".jpeg", ".png"]:

        matches = list(
            WEATHER_ROOT.rglob(image_name + ext)
        )

        if matches:
            image_found = matches[0]
            break

    if image_found is None:
        continue

    shutil.copy(
        image_found,
        TRAIN_IMG / image_found.name
    )

    shutil.copy(
        txt,
        TRAIN_LBL / txt.name
    )

    weather_count += 1

print(f"Weather copied: {weather_count}")