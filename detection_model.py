from ultralytics import YOLO
import cv2
import sys

model = YOLO('yolov8n.pt')
image_path='C:/Users/Shivendra Srivastava/Downloads/yolov88/S3.png'
video_path = 'C:/Users/Shivendra Srivastava/Downloads/yolov88/track.mp4'

def detect_from_image(image_path):
    # Read the image 'C:\Yolov9/runs/track.mp4'    'C:/Users/Shivendra Srivastava/Pictures/Screenshots/S4.png' 
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image from {image_path}")
        return
    
    # Perform object detection
    results = model(image)
    
    # Visualize 
    annotated_image = results[0].plot()
    
    cv2.imshow('YOLOv8 Detection - Image', annotated_image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

def detect_from_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return
    
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform object detection on the frame
        results = model(frame)
        
        annotated_frame = results[0].plot()
        
        # Display the annotated frame
        cv2.imshow('YOLOv8 Detection - Video', annotated_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def detect_from_webcam():
    # Open the default camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform object detection on the frame
        results = model(frame)
        
        # Visualize 
        annotated_frame = results[0].plot()
        
        cv2.imshow('YOLOv8 Detection - Webcam', annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Ask the user to choose the detection source
print("Choose the detection source:")
print("1. Image")
print("2. Video ")
print("3. Live Camera")
print("Note- For stopping either video or live detection press q")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    detect_from_image(image_path)
elif choice == '2':
    detect_from_video(video_path)
elif choice == '3':
    detect_from_webcam()
else:
    print("Invalid choice. Exiting.")
    sys.exit()
