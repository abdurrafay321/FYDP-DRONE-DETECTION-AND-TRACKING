from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
YOLOV5_ROOT = PROJECT_ROOT / "SOFTWARE" / "yolov5"
WEIGHTS = PROJECT_ROOT / "SOFTWARE" / "TRAINED_MODELS" / "last.pt"
DATA = YOLOV5_ROOT / "data" / "coco128.yaml"

if str(YOLOV5_ROOT) not in sys.path:
    sys.path.insert(0, str(YOLOV5_ROOT))

from detect import run


def main():
    if not WEIGHTS.is_file():
        raise FileNotFoundError(f"Trained checkpoint not found: {WEIGHTS}")

    run(
        weights=WEIGHTS,
        source="0",
        data=DATA,
        imgsz=(640, 640),
        conf_thres=0.25,
        device="",
        view_img=True,
        nosave=True,
        project=PROJECT_ROOT / "SOFTWARE" / "RESULTS",
        name="webcam",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()