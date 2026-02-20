import os
from ultralytics import YOLO
import cv2

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load a pre-trained YOLOv8 model
model = YOLO('./object-detection-yolo/weights/yolov8n.pt')

# Construct the absolute path to the image
image_path = os.path.join(script_dir, 'images', '2.jpg')

# Check if file exists
if not os.path.exists(image_path):
    print(f"Error: {image_path} not found.")
else:
    # Run inference on an image
    results = model(image_path)

    # Display results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        cv2.imshow('YOLOv8 Detection', im_array)
        cv2.waitKey(0)

cv2.destroyAllWindows()
