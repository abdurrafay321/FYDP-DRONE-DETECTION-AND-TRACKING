# FYDP: Real-Time Drone Detection and Tracking System

A comprehensive computer vision and hardware acceleration framework for real-time drone detection and tracking. This repository combines deep learning object detection (YOLOv5), multi-domain dataset preprocessing pipelines, custom trained model checkpoints, and hardware acceleration designs (FPGA/DPU).

Repository Link: https://github.com/abdurrafay321/FYDP-DRONE-DETECTION-AND-TRACKING

---

## Project Structure

```text
FYDP-DRONE-DETECTION-AND-TRACKING/
├── DOCUMENTATION/       # Architectural specifications, project reports, and documentation
├── HARDWARE/            # FPGA hardware acceleration blocks and IP design
│   ├── CONVOLUTION/     # Hardware convolution logic modules
│   ├── DPU/             # Deep Learning Processing Unit architecture
│   ├── MAC/             # Multiply-Accumulate compute arrays
│   ├── MEMORY/          # On-chip memory buffers and interfaces
│   ├── PE/              # Processing Element arrays
│   └── VIVADO/          # Xilinx Vivado hardware project files
├── SOFTWARE/
│   ├── SCRIPTS/         # Preprocessing, format conversion, and detection execution scripts
│   ├── TRAINED_MODELS/  # Trained model checkpoint (last.pt)
│   └── yolov5/          # Integrated YOLOv5 object detection engine
├── requirements.txt     # Python environment dependency specifications
├── .gitignore           # Git version control exclusion rules
└── README.md            # System documentation
```

---

## Software Pipeline and Features

### 1. Detection and Inference Scripts
- **Image/Photo Detection (`SOFTWARE/SCRIPTS/image_detect.py`)**: Runs object detection on single images (`.jpg`, `.jpeg`, `.png`) or directories of images using the trained model weights `SOFTWARE/TRAINED_MODELS/last.pt`. Outputs are logged under `SOFTWARE/RESULTS/image/`.
- **Video Detection (`SOFTWARE/SCRIPTS/video_detect.py`)**: Runs object detection on local MP4 video files or direct video URLs using `SOFTWARE/TRAINED_MODELS/last.pt`. Outputs are logged under `SOFTWARE/RESULTS/video/`.
- **Webcam Detection (`SOFTWARE/SCRIPTS/webcam_detect.py`)**: Executes real-time drone detection on live camera feeds (device index 0) with bounding box visualization.

### 2. Dataset Processing Pipeline
The repository includes dedicated scripts in `SOFTWARE/SCRIPTS/` to aggregate, clean, and convert multi-domain drone datasets (DetFly, VisioDECT Weather, and Night datasets):
- **`01_weather_to_single_class.py`**: Normalizes multi-class annotations into a single drone target class (`class 0`).
- **`02_detfly_xml_to_yolo.py`**: Converts Pascal VOC XML bounding box annotations into normalized YOLO coordinate format `(class, x_center, y_center, width, height)`.
- **`03_merge_datasets.py` & `04_merge_detfly.py`**: Merges multi-source images and label files into consolidated training, validation, and testing splits under `SOFTWARE/DATASET/FINAL DATASET/`.
- **`05_copy_detfly.py`**: Automated distribution of train/valid/test split subsets.
- **Verification Tools**: `count_final_dataset.py`, `count_weather_images.py`, `count_weather_labels.py`, and `test_weather.py` provide dataset statistics and sanity checks.

### 3. Model Weights
- **`SOFTWARE/TRAINED_MODELS/last.pt`**: PyTorch weights trained on the consolidated drone dataset.

---

## Hardware Architecture

The `HARDWARE/` directory contains design components for FPGA-based hardware acceleration:
- **DPU (Deep Learning Processing Unit)**: Core hardware accelerator architecture.
- **PE & MAC Units**: Processing Element arrays and Multiply-Accumulate logic for parallel matrix operations.
- **Memory Subsystem**: Buffer management for feature maps and model parameters.
- **Vivado Integration**: Xilinx Vivado hardware synthesis and implementation files.

---

## Setup and Installation

### 1. Environment Preparation
Ensure Python 3.8+ and PyTorch are installed in your environment.

### 2. Repository Setup
```bash
git clone https://github.com/abdurrafay321/FYDP-DRONE-DETECTION-AND-TRACKING.git
cd FYDP-DRONE-DETECTION-AND-TRACKING
```

### 3. Dependency Installation
```bash
pip install -r requirements.txt
```

---

## Usage Instructions

### Running Detection on Photo / Image Files
To perform detection on a single image or a directory of images:
```bash
python SOFTWARE/SCRIPTS/image_detect.py --source path/to/drone_image.jpg --weights SOFTWARE/TRAINED_MODELS/last.pt
```

### Running Detection on Video Files
To perform detection on a local video file:
```bash
python SOFTWARE/SCRIPTS/video_detect.py --video path/to/sample_video.mp4 --weights SOFTWARE/TRAINED_MODELS/last.pt
```

To perform detection directly from a URL:
```bash
python SOFTWARE/SCRIPTS/video_detect.py --url "https://example.com/sample_video.mp4" --weights SOFTWARE/TRAINED_MODELS/last.pt
```

### Running Real-Time Webcam Detection
```bash
python SOFTWARE/SCRIPTS/webcam_detect.py
```

---

## Citation and Acknowledgments

- Final Year Design Project (FYDP).
- Object detection backbone powered by [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5).
