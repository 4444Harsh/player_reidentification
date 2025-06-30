
# Soccer Player Tracking System
### Google Drive Submission Package

 **Drive Folder Structure**:
```
PLAYER_TRACKING/
├── README.md               (This file)
├── Technical_Report.pdf
├──  Code/
│   ├── main.py               (Main program)
│   ├── detector.py           (YOLO detection)
│   └── tracker.py            (Re-ID logic)
├──  Models/
│   └── best.pt            (Pre-trained weights)
├──  data/
│   ├── input_videos.mp4             (Sample input)
├── output/            (Processed result)
└──  requirements.txt       (Dependencies)
```

## Quick Start Guide

### 1. Download Files
1. **Download the entire folder** from Google Drive
2. **Preserve the folder structure** exactly as shown above

### 2. Install Requirements
```bash
pip install -r requirements.txt
```
* Pro Tip: Use Python 3.8+ and a virtual environment*

### 3. Run the Program
```bash
python Code/main.py
```
▶ **Expected Output**: 
- Processed video saved to `Videos/output.mp4`
- Terminal will show real-time progress:
  ```
  Processing Frame 45: 12 players tracked (1.3s/frame)
  ```

## Detailed Setup

### For Custom Videos:
1. Replace `Videos/input.mp4` with your video
2. Edit these paths in `Code/main.py`:
   ```python
   INPUT_VIDEO = "Videos/your_video.mp4"
   OUTPUT_VIDEO = "Videos/custom_output.mp4" 
   ```


## How It Works
### Core Pipeline:
1. **Frame Extraction** → Reads video at 30 FPS
2. **Player Detection** → YOLOv11 model
3. **Feature Storage** → Saves jersey color/position
4. **Re-Identification** → Matches players across frames

![Tracking Demo](outputs/tracked_output.mp4) *Live tracking example*

##  Need Help?
**Common Issues**:
-  *"Missing model weights"* → Ensure `yolov11.pt` is in ⚙️ Models/
-  *Slow performance* → Try reducing resolution in `detector.py`
-  *Video playback issues* → Use VLC Player

 **Contact Support**: guptaharshbly@gmail.com (mailto:)

---