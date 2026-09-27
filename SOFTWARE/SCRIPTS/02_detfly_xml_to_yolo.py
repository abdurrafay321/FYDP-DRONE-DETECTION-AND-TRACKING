from pathlib import Path
import xml.etree.ElementTree as ET

PROJECT_ROOT = Path(__file__).resolve().parents[2]
XML_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "drones" / "det_fly" / "annotations" / "Annotations"
OUTPUT_ROOT = PROJECT_ROOT / "SOFTWARE" / "DATASET" / "raw" / "drones" / "det_fly" / "yolo_labels"

OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

xml_files = list(XML_ROOT.rglob("*.xml"))

print(f"Found {len(xml_files)} XML files")

for xml_file in xml_files:

    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find("size")

    width = float(size.find("width").text)
    height = float(size.find("height").text)

    yolo_lines = []

    for obj in root.findall("object"):

        bbox = obj.find("bndbox")

        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height

        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height

        yolo_lines.append(
            f"0 {x_center} {y_center} {box_width} {box_height}"
        )

    output_file = OUTPUT_ROOT / f"{xml_file.stem}.txt"

    with open(output_file, "w") as f:
        f.write("\n".join(yolo_lines))

print("Conversion complete")