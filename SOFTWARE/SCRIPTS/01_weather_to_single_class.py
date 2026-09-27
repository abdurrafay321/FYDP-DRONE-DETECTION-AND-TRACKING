from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEATHER_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "weather" / "VisioDECT Dataset Upload"

txt_files = list(WEATHER_ROOT.rglob("*.txt"))

print(f"Found {len(txt_files)} label files")

for txt_file in txt_files:

    new_lines = []

    with open(txt_file, "r") as f:
        lines = f.readlines()

    for line in lines:

        parts = line.strip().split()

        if len(parts) < 5:
            continue

        # Force class to drone = 0
        parts[0] = "0"

        new_lines.append(" ".join(parts))

    with open(txt_file, "w") as f:
        f.write("\n".join(new_lines))

print("Done.")