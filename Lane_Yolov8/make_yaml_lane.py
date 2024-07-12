import yaml

data = {
    "train" : 'dataset/train/images',
        "val" : 'dataset/val/images',
        "test" : 'dataset/test/images',
        "names" : {0 : 'lane_blue'}}

with open('dataset/data.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('dataset/data.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)