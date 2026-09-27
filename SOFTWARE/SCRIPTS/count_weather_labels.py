from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEATHER_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "weather" / "VisioDECT Dataset Upload"

count = 0

for txt in WEATHER_ROOT.rglob("*.txt"):
    count += 1

print("Total TXT labels:", count)