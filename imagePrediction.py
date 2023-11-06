from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO('/home/jaswanth/projects/Wall-Crack-Detection/models/objectDetection/best.pt')  # Replace with the correct path to your YOLO model

# Load the image
image_path = "/home/jaswanth/projects/Wall-Crack-Detection/test images/IMG_20231105_104521.jpg"
image = cv2.imread(image_path)

# Perform object detection on the image
results = model(image)

# Access the detected objects and their information for a single image (index 0)
if results[0] is not None:
    for pred in results[0]:
        if len(pred) == 6:
            class_id, confidence, x_center, y_center, width, height = pred

            # Calculate coordinates of the bounding box
            left = int(x_center - width / 2)
            top = int(y_center - height / 2)
            right = int(x_center + width / 2)
            bottom = int(y_center + height / 2)

            # Get the class label for the detected object
            class_label = model.names[int(class_id)]

            # Print the class label and confidence score
            print(f"Class: {class_label}, Confidence: {confidence:.2f}")

            # Draw bounding boxes on the image
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image, f"{class_label}: {confidence:.2f}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with bounding boxes and labels
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
