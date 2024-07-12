import os

# 파일 경로 및 이름 설정
path = "dataset_vehicle/val/images"  # train,test,val 직접 이름 넣기 
txt_file_name = "dataset_vehicle/val.txt"  # 새로 생성할 텍스트 이름 

# 이미지 파일 목록 가져오기
image_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# 텍스트 파일에 이미지 파일 이름 쓰기
with open(txt_file_name, "w") as txt_file:
    for image_name in image_names:
        txt_file.write(image_name + "\n")

print(f"Text file '{txt_file_name}' has been created.")
