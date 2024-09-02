# YOLOv8 Object Detection Project

This project demonstrates object detection using the YOLOv8 model from Ultralytics. The project supports detection from images, videos, and live webcam feeds, providing an interactive experience for visualizing detections.

## Features

- **Image Detection:** Perform object detection on a specified image and visualize the results.
- **Video Detection:** Detect objects in a video file with real-time visualization.
- **Webcam Detection:** Use the webcam to perform live object detection.

## Dependencies

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) - YOLOv8 model for object detection.
- OpenCV - For image and video processing.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Shivendraaaa/Realtime-Object-Detection.git
   ```

2. ## How to Run

### Choose the Detection Source:
The script allows you to select between image detection, video detection, and live webcam detection.

### Running the Script:
Run the script in a Python environment:

```bash
python detect.py
```

### Follow the On-Screen Prompts:
- **For Image Detection**: Ensure the image path is correctly set in the script.
- **For Video Detection**: Specify the correct video path.
- **For Webcam Detection**: Simply select the webcam option.

> **Note**: To stop video or webcam detection, press the `q` key.

### Notes
- Ensure the paths to the image and video files are correctly specified.
- The YOLOv8 model used is the 'n' (nano) version. You can change the model by modifying the model path in the script.

### License
This project is open-source and available under the MIT License.

**Happy detecting!**
