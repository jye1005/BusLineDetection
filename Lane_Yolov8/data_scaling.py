from sklearn.preprocessing import StandardScaler
import numpy as np 


from PIL import Image
import os

target_size = (416, 416)  # YOLO 모델에 맞는 크기로 설정


input_folder_test = 'datasets/차선/차선 images/split_data/test/images'

for filename in os.listdir(input_folder_test):
    if filename.endswith(('.jpg')):
        image_path = os.path.join(input_folder_test, filename)
        
        image = Image.open(image_path)
        image_resized = image.resize(target_size)
        image_array = np.array(image_resized)
        image_normalized = image_array / 255.0
        Image.fromarray((image_normalized * 255).astype(np.uint8)).save(image_path)

input_folder_val = 'datasets/차선/차선 images/split_data/val/images'

for filename in os.listdir(input_folder_val):
    if filename.endswith(('.jpg')):
        image_path = os.path.join(input_folder_val, filename)
        
        image = Image.open(image_path)
        image_resized = image.resize(target_size)
        image_array = np.array(image_resized)
        image_normalized = image_array / 255.0
        Image.fromarray((image_normalized * 255).astype(np.uint8)).save(image_path)


input_folder_train = 'datasets/차선/차선 images/split_data/train/images'

for filename in os.listdir(input_folder_train):
    if filename.endswith(('.jpg')):
        image_path = os.path.join(input_folder_train, filename)
        
        image = Image.open(image_path)
        image_resized = image.resize(target_size)
        image_array = np.array(image_resized)
        image_normalized = image_array / 255.0
        Image.fromarray((image_normalized * 255).astype(np.uint8)).save(image_path)

