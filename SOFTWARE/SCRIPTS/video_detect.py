import argparse
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[2]
YOLOV5_ROOT = PROJECT_ROOT / "SOFTWARE" / "yolov5"
DEFAULT_WEIGHTS = PROJECT_ROOT / "SOFTWARE" / "TRAINED_MODELS" / "last.pt"
DOWNLOAD_DIR = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "video_downloads"
RESULTS_DIR = PROJECT_ROOT / "SOFTWARE" / "RESULTS"

if str(YOLOV5_ROOT) not in sys.path:
    sys.path.insert(0, str(YOLOV5_ROOT))

from detect import run


def download_video(url: str, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(request, timeout=60) as response, destination.open("wb") as output:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)

    if destination.stat().st_size == 0:
        raise RuntimeError(f"Downloaded file is empty: {destination}")

    return destination


def filename_from_url(url: str) -> str:
    name = Path(unquote(urlparse(url).path)).name
    return name if Path(name).suffix else "downloaded_video.mp4"


def parse_args():
    parser = argparse.ArgumentParser(description="Download and run YOLOv5 detection on a video.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--url", help="Direct video URL, such as an MP4 URL")
    source.add_argument("--video", type=Path, help="Path to a local video file")
    parser.add_argument("--weights", type=Path, default=DEFAULT_WEIGHTS)
    parser.add_argument("--conf-thres", type=float, default=0.25)
    parser.add_argument("--img", type=int, default=640)
    parser.add_argument("--device", default="", help="CUDA device such as 0, or cpu")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.weights.is_file():
        raise FileNotFoundError(f"Weights file not found: {args.weights}")

    if args.url:
        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
        download_path = DOWNLOAD_DIR / filename_from_url(args.url)
        print(f"Downloading video to: {download_path}")
        source = download_video(args.url, download_path)
    else:
        source = args.video.resolve()
        if not source.is_file():
            raise FileNotFoundError(f"Video file not found: {source}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Running detection on: {source}")
    run(
        weights=args.weights.resolve(),
        source=source,
        imgsz=(args.img, args.img),
        conf_thres=args.conf_thres,
        device=args.device,
        project=RESULTS_DIR,
        name="video",
        exist_ok=True,
        nosave=False,
        view_img=False,
    )
    print(f"Detection output: {RESULTS_DIR / 'video'}")


if __name__ == "__main__":
    main()