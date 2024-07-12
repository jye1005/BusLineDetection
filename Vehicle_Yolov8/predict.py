from ultralytics import YOLO

model = YOLO('runs/segment/train10/weights/best.pt')
results= model('datasets/test/images/', save=True) #save_txt=True