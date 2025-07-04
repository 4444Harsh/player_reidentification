import os
import cv2
import yaml
from detector import PlayerDetector
from tracker import PlayerTracker


def get_absolute_path(relative_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, relative_path))



def main():
    # 1. PATH CONFIGURATION
    config_path = get_absolute_path("../configs/paths.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    input_path = get_absolute_path(config["paths"]["input_video"])
    output_path = get_absolute_path(config["paths"]["output_video"])

    # Create output directory if not exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 2. VIDEO SETUP
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video at {input_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 3. VIDEO WRITER CONFIG (MOST COMPATIBLE SETTINGS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Primary option
    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps if fps > 0 else 30.0,  # Fallback to 30 FPS
        (width, height),
        True
    )

    if not out.isOpened():
        # Fallback to alternative codec
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), True)
        if not out.isOpened():
            raise RuntimeError("Failed to initialize VideoWriter with both codecs")

    # 4. PROCESSING LOOP
    detector = PlayerDetector()
    tracker = PlayerTracker()

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            detections = detector.detect(frame)
            players = tracker.update(detections)

            for pid, player in players.items():
                x1, y1, x2, y2 = player["bbox"]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"ID: {pid}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            out.write(frame)

    finally:
        # 5. PROPER CLEANUP
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Verify output file
        if os.path.exists(output_path) and os.path.getsize(output_path) > 1024:
            print(f"Success! Output saved to: {output_path}")
        else:
            print("Video file creation failed - trying alternative method...")
            try_ffmpeg_conversion()


def try_ffmpeg_conversion():
    """Fallback method using FFmpeg if OpenCV fails"""
    import subprocess
    temp_dir = "temp_frames"
    os.makedirs(temp_dir, exist_ok=True)

    # (Re-process and save frames as PNG images)
    # [...] Add your frame saving logic here

    # Convert to MP4 using FFmpeg
    subprocess.run([
        'ffmpeg', '-y',
        '-framerate', '30',
        '-i', f'{temp_dir}/frame_%04d.png',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        get_absolute_path("../outputs/ffmpeg_output.mp4")
    ])

    print("Fallback FFmpeg conversion completed!")


if __name__ == "__main__":
    main()