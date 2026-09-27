from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEATHER_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "weather" / "VisioDECT Dataset Upload"

count = 0

for ext in ["*.jpg", "*.jpeg", "*.png"]:

    count += len(list(WEATHER_ROOT.rglob(ext)))

print("Total Images:", count)