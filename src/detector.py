import os
import cv2
from ultralytics import YOLO
import yaml


class PlayerDetector:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "../configs/paths.yaml")
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        model_path = os.path.join(script_dir, config["paths"]["model"])
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                detections.append(([x1, y1, x2, y2], conf))
        return detections