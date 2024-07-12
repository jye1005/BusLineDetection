import os
import json

def merge_blue_lane_annotations(data):
    merged_annotations = {}

    for annotation_data in data["data_set_info"]["data"]:
        object_id = annotation_data["objectID"]
        
        if object_id.endswith("_1") or object_id.endswith("_2"):
            base_object_id = object_id[:-2]  # Remove "_1" or "_2"
            
            if base_object_id not in merged_annotations:
                merged_annotations[base_object_id] = {"objectID": base_object_id}

            if "object_Label" in annotation_data["value"] and "lane_type" in annotation_data["value"]["object_Label"] and annotation_data["value"]["object_Label"]["lane_type"] == "lane_blue":
                merged_annotations[base_object_id].update(annotation_data)

    return list(merged_annotations.values())

all_merged_blue_lane_annotations = []
labels_directory = "dataset/train/labels"

for filename in os.listdir(labels_directory):
    if filename.endswith(".json"):
        json_file_path = os.path.join(labels_directory, filename)
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            merged_blue_lane_annotations = merge_blue_lane_annotations(data)
            all_merged_blue_lane_annotations.extend(merged_blue_lane_annotations)

output_path = "dataset/train/merged_blue_lane_annotations.json" # train,test,val 디렉토리 경로 수정 필요 
merged_json_data = all_merged_blue_lane_annotations

with open(output_path, 'w', encoding='utf-8') as output_file:
    json.dump(merged_json_data, output_file, ensure_ascii=False, indent=2)

print(f"Successfully merged blue lane annotations to {output_path}")
