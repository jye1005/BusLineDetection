import os
import shutil

# 데이터셋 폴더 경로
dataset_folder = "datasets/차선"
# 원천데이터 폴더 안 폴더 경로
source_folder = os.path.join(dataset_folder, "labeling", "VL/B/BLUE") # 파일 경로 수정 필요 

final_destination_folder = "datasets/차선/차선 annotations"

for folder_number in range(100000):
    folder_name = f"[{folder_number:05d}]B_BLUE"
    source_folder_path = os.path.join(source_folder, folder_name)
    
    # 숫자로 이루어진 폴더가 존재하는지 확인
    if os.path.exists(source_folder_path):
        for file in os.listdir(source_folder_path):
            if file.endswith(".json"):
                # 목적지 데이터셋 폴더에 복사
                destination_path = os.path.join(final_destination_folder, file)

                # 목적지 폴더가 존재하지 않으면 생성
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # 복사 수행
                source_path = os.path.join(source_folder_path, file)
                print(f"Copying: {source_path} -> {destination_path}")
                shutil.copyfile(source_path, destination_path)

# 원천데이터 폴더 안 폴더 경로
source_folder2 = os.path.join(dataset_folder, "images", "VL/B/BLUE") # 파일 경로 수정 필요 

final_destination_folder = "datasets/차선/차선 images"

for folder_number in range(100000):
    folder_name = f"[{folder_number:05d}]B_BLUE"
    source_folder_path = os.path.join(source_folder2, folder_name)
    
    # 숫자로 이루어진 폴더가 존재하는지 확인
    if os.path.exists(source_folder_path):
        for file in os.listdir(source_folder_path):
            if file.endswith(".jpg"):
                # 목적지 데이터셋 폴더에 복사
                destination_path = os.path.join(final_destination_folder, file)

                # 목적지 폴더가 존재하지 않으면 생성
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # 복사 수행
                source_path = os.path.join(source_folder_path, file)
                print(f"Copying: {source_path} -> {destination_path}")
                shutil.copyfile(source_path, destination_path)
