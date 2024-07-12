import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

dataset_path = "datasets/차선/차선 images" # 현재 프로그램에서는 삭제한 상태 
json_file_path = "datasets/차선/차선 labels"  

output_folder_path = Path(dataset_path) / "split_data"
train_folder = output_folder_path / "train"
test_folder = output_folder_path / "test"
val_folder = output_folder_path / "val"

image_files = [f for f in os.listdir(dataset_path) if f.endswith(".jpg")]


labels_files = [f for f in os.listdir(json_file_path) if f.endswith(".json")]

# 이미지 파일과 레이블 파일을 train, test, validation으로 나누기
train_images, test_images, train_labels, test_labels = train_test_split(image_files, labels_files, test_size=0.2, random_state=42)
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

for folder in [train_folder, test_folder, val_folder]:
    folder.mkdir(parents=True, exist_ok=True)

for folder, images in zip([train_folder, test_folder, val_folder], [train_images, test_images, val_images]):
    image_subfolder = folder / "images"
    image_subfolder.mkdir(parents=True, exist_ok=True)
    for file in images:
        shutil.copy(os.path.join(dataset_path, file), os.path.join(image_subfolder, file))
        
for folder, labels in zip([train_folder, test_folder, val_folder], [train_labels, test_labels, val_labels]):
    label_subfolder = folder / "labels"
    label_subfolder.mkdir(parents=True, exist_ok=True)
    for file in labels:
        shutil.copy(os.path.join(json_file_path, file), os.path.join(label_subfolder, file))

