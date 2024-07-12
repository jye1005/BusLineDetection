import os
import json

def extract_and_save_blue_lane_annotations(data, output_directory):
    image_filename = os.path.splitext(os.path.basename(data["data_set_info"]["sourceValue"]))[0]
    
    for annotation_data in data["data_set_info"]["data"]:
        object_id = annotation_data["objectID"]
        
        if object_id.endswith("_1") and "object_Label" in annotation_data["value"] and "lane_type" in annotation_data["value"]["object_Label"] and annotation_data["value"]["object_Label"]["lane_type"] == "lane_blue":
            # 해당 정보를 새로운 JSON 파일로 저장
            output_filename = f"{image_filename}.json"
            output_path = os.path.join(output_directory, output_filename)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                json.dump(annotation_data, output_file, ensure_ascii=False, indent=2)
            print(f"Successfully extracted blue lane annotation to {output_path}")

        if object_id.endswith("_2") and "object_Label" in annotation_data["value"] and "lane_type" in annotation_data["value"]["object_Label"] and annotation_data["value"]["object_Label"]["lane_type"] == "lane_blue":
            # 해당 정보를 새로운 JSON 파일로 저장
            output_filename = f"{image_filename}.json"
            output_path = os.path.join(output_directory, output_filename)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                json.dump(annotation_data, output_file, ensure_ascii=False, indent=2)
            print(f"Successfully extracted blue lane annotation to {output_path}")

all_blue_lane_annotations_directory = "dataset/train/blue_annotations"
os.makedirs(all_blue_lane_annotations_directory, exist_ok=True)

labels_directory = "dataset/train/annotations"

for filename in os.listdir(labels_directory):
    if filename.endswith(".json"):
        json_file_path = os.path.join(labels_directory, filename)
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            extract_and_save_blue_lane_annotations(data, all_blue_lane_annotations_directory)
