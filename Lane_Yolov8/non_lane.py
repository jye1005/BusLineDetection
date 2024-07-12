import os
import json

def process_data(data):
    # 데이터에서 "lane_type"이 있는지 확인
    if 'object_Label' in data and 'lane_type' in data['object_Label']:
        lane_type = data['object_Label']['lane_type']
    else:
        # "lane_type"이 없는 경우 기본값으로 "non_lane" 할당
        lane_type = 'non_lane'
    
    # 다른 처리 로직을 여기에 추가할 수 있습니다.

    return lane_type

def process_directory(directory_path):
    # 디렉토리 안에 있는 파일들을 가져옴
    files = os.listdir(directory_path)

    for file_name in files:
        # 파일의 절대 경로 생성
        file_path = os.path.join(directory_path, file_name)

        # 파일인 경우에만 처리
        if os.path.isfile(file_path):
            # JSON 파일인지 확인
            if file_name.lower().endswith('.json'):
                # JSON 데이터 로드
                with open(file_path, 'r', encoding='utf-8') as file:
                    json_data = json.load(file)

                # 데이터 처리 함수 호출
                result = process_data(json_data)
                print(f'File: {file_name}, Result: {result}')

# 예시: train 디렉토리 처리
train_directory = 'yolov5/dataset/val'
process_directory(train_directory)
