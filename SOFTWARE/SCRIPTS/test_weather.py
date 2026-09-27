from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEATHER_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "weather" / "VisioDECT Dataset Upload"

drone_path = WEATHER_ROOT / "Anafi-Extended"

imgs = list((drone_path / "images").rglob("*.jpg"))

print("Images found:", len(imgs))

if imgs:
    img = imgs[0]

    print("Image:")
    print(img)

    relative = img.relative_to(drone_path / "images")

    print("Relative:")
    print(relative)

    label = (
        drone_path
        / "labels"
        / relative.parent.name.lower()
        / f"{img.stem}.txt"
    )

    print("Expected label:")
    print(label)

    print("Exists:", label.exists())