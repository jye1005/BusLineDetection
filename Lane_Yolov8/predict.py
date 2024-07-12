from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load a model

model = YOLO('runs/segment/train64/weights/best.pt')  # load a custom model


results = model.predict(source='dataset/test/images', save=True)