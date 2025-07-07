import numpy as np


class PlayerTracker:
    def __init__(self):
        self.players = {}  # {player_id: {"bbox": [x1,y1,x2,y2], "features": []}}
        self.next_id = 1

    def update(self, detections):
        updated_players = {}
        for bbox, _ in detections:
            matched = False
            for pid, player in self.players.items():
                if self._iou(bbox, player["bbox"]) > 0.5:  # Simple IoU matching
                    updated_players[pid] = {"bbox": bbox, "features": player["features"]}
                    matched = True
                    break

            if not matched:  # New player
                updated_players[self.next_id] = {"bbox": bbox, "features": []}
                self.next_id += 1

        self.players = updated_players
        return self.players

    def _iou(self, box1, box2):
        # Calculate Intersection over Union
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        inter = max(0, x2 - x1) * max(0, y2 - y1)
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        return inter / (area1 + area2 - inter)