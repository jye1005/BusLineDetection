from ultralytics import YOLO
  # build a new model from scratch

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

model.train(data='Lane_Yolov8/dataset/data.yaml',epochs=100, optimizer='SGD',dropout=0.3)
