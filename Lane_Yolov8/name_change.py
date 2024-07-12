import os

def replace_blue_in_directory(directory):
    # 특정 디렉터리 내의 파일 목록 가져오기
    file_list = os.listdir(directory)

    # 디렉터리 내의 각 파일에 대해 작업 수행
    for filename in file_list:
        # 새로운 파일명 생성 (여기서는 '_BLUE_'로 대체)
        new_filename = filename.replace('[BLUE]', '_BLUE_')

        # 기존 파일 경로와 새로운 파일 경로 생성
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        # 파일명 변경
        os.rename(old_path, new_path)

# 데이터셋 디렉터리의 경로를 지정
dataset_directory = 'dataset_vehicle'

# 'test', 'train', 'val' 디렉터리에 대해 함수 호출
for subset in ['val']:
    subset_directory = os.path.join(dataset_directory, subset)

    # 'images', 'labels' 디렉터리에 대해 함수 호출
    for data_type in ['vehicle_annotations']:
        data_directory = os.path.join(subset_directory, data_type)

        # 함수 호출
        replace_blue_in_directory(data_directory)
