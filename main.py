from ultralytics import YOLO
import cv2


from ultralytics import YOLO

# Load YOLO model
model = YOLO('/home/jaswanth/projects/Wall-Crack-Detection/models/objectDetection/best.pt')  # Replace with the correct path to your YOLO model

# Open the webcam (camera source "0")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Perform object detection on the frame
        results = model(frame)

        # Access the detected objects and their information for a single frame (index 0)
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

                # Draw bounding boxes on the frame
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_label}: {confidence:.2f}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame with bounding boxes and labels
        cv2.imshow('Object Detection', frame)

        # Press 'q' to exit the real-time object detection
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

