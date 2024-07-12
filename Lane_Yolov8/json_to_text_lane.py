import os
import json

def convert_json_to_txt(json_file_path, output_directory, image_width, image_height):
    CLASS_NAMES = ["lane_blue"]

    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    try:
        points = json_data["value"]["points"]
        lane_type = json_data["value"]["object_Label"]["lane_type"]
    except KeyError:
        print(f"Skipping {json_file_path}. Missing necessary keys.")
        return

    # Create TXT file name based on JSON file name
    txt_file_name = os.path.join(output_directory, os.path.splitext(os.path.basename(json_file_path))[0] + '.txt')

    with open(txt_file_name, 'w') as new_file:
        # Write class index to the file (assuming only one class per file)
        new_data = "{}".format(str(CLASS_NAMES.index(lane_type)))

        # Write normalized xy coordinates to the file
        for point in points:
            # Extract x and y coordinates
            x_coord = float(point['x'])
            y_coord = float(point['y'])

            # Normalize coordinates
            x_normalized = x_coord / image_width
            y_normalized = y_coord / image_height

            # Append normalized coordinates to the line
            new_data += " {} {}".format(str(x_normalized), str(y_normalized))

        # Add a newline character at the end
        new_data += "\n"

        # Write the data to the file
        new_file.write(new_data)

# Input and output directories
input_directory = 'dataset/val/blue_annotations'
output_directory = 'dataset/val/labels'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Specify the actual image size (replace with your actual values)
image_width = 1920
image_height = 1080

# Iterate through all JSON files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".json"):
        json_file_path = os.path.join(input_directory, filename)
        convert_json_to_txt(json_file_path, output_directory, image_width, image_height)

print("Conversion to TXT completed.")
