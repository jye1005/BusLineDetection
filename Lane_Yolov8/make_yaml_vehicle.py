import yaml

data = {
    "train" : 'dataset_vehicle/train/images',
        "val" : 'dataset_vehicle/val/images',
        "test" : 'dataset_vehicle/test/images',
        "names" : {0 : 'vehicle_car', 1: 'vehicle_bike', 2: 'vehicle_bus', 3:'vehicle_truck'}}

with open('dataset_vehicle/data.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('dataset_vehicle/data.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)