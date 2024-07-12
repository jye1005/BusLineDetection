from ultralytics import YOLO
  # build a new model from scratch

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

model.train(data='dataset/data.yaml', epochs=10, optimizer='AdamW',dropout=0.3)
