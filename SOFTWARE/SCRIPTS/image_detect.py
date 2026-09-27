import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
YOLOV5_ROOT = PROJECT_ROOT / "SOFTWARE" / "yolov5"
DEFAULT_WEIGHTS = PROJECT_ROOT / "SOFTWARE" / "TRAINED_MODELS" / "last.pt"
RESULTS_DIR = PROJECT_ROOT / "SOFTWARE" / "RESULTS"

if str(YOLOV5_ROOT) not in sys.path:
    sys.path.insert(0, str(YOLOV5_ROOT))

from detect import run


def parse_args():
    parser = argparse.ArgumentParser(description="Run YOLOv5 drone detection on single photos or a directory of images.")
    parser.add_argument("--source", type=Path, required=True, help="Path to an image file (.jpg, .png) or directory of images")
    parser.add_argument("--weights", type=Path, default=DEFAULT_WEIGHTS, help="Path to trained model weights (.pt)")
    parser.add_argument("--conf-thres", type=float, default=0.25, help="Confidence threshold")
    parser.add_argument("--img", type=int, default=640, help="Inference image size")
    parser.add_argument("--device", default="", help="CUDA device (e.g. 0) or cpu")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.weights.is_file():
        raise FileNotFoundError(f"Weights file not found: {args.weights}")

    source = args.source.resolve()
    if not source.exists():
        raise FileNotFoundError(f"Image source not found: {source}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Running drone detection on image source: {source}")

    run(
        weights=args.weights.resolve(),
        source=source,
        imgsz=(args.img, args.img),
        conf_thres=args.conf_thres,
        device=args.device,
        project=RESULTS_DIR,
        name="image",
        exist_ok=True,
        nosave=False,
        view_img=False,
    )
    print(f"Detection output saved to: {RESULTS_DIR / 'image'}")


if __name__ == "__main__":
    main()
