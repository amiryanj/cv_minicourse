import cv2
from ultralytics import YOLO

yolo_model = YOLO('yolov8n.pt')
img_file = "C:/workspace/cat.jpg"
img = cv2.imread(img_file)

results = yolo_model(img)
results.show()
