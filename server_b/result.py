import os
import glob
import tempfile
from shapely.geometry import Polygon
from ultralytics import YOLO  # YOLO model library
from PIL import Image  # Import PIL library for image handling

# Initialize models
model_V = YOLO('./Vehicle_Yolov8/runs/segment/train10/weights/best.pt')
model_L = YOLO('./Lane_Yolov8/runs/segment/train64/weights/best.pt')

def get_latest_predict_file(base_path):
    txt_files = glob.glob(os.path.join(base_path, 'labels', '*.txt'))
    if not txt_files:
        return None
    return max(txt_files, key=os.path.getctime)

def process_image(image):
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        image.save(tmp, format='JPEG')
        tmp_path = tmp.name

    try:
        results_V = model_V(tmp_path, project='Vehicle_Yolov8/runs/segment', name='predict', save=True, save_txt=True)
        results_L = model_L(tmp_path, project='Lane_Yolov8/runs/segment', name='predict', save=True, save_txt=True)

        vehicle_model_path = results_V[0].save_dir if results_V else "Vehicle_Yolov8/runs/segment/predict"
        lane_model_path = results_L[0].save_dir if results_L else "Lane_Yolov8/runs/segment/predict"

        vehicle_file = get_latest_predict_file(vehicle_model_path)
        lane_file = get_latest_predict_file(lane_model_path)

        if not vehicle_file or not lane_file:
            return "There is no lane or vehicle data available."

        def parse_file(file_path):
            with open(file_path, 'r') as file:
                data = file.read().strip()
            return [line.split() for line in data.split('\n') if line]

        vehicle_polygons = []
        lane_polygons = []
        lane_class_found = False

        for parts in parse_file(vehicle_file):
            class_id, coords = int(parts[0]), [(float(parts[i]), float(parts[i+1])) for i in range(1, len(parts), 2)]
            if class_id == 2:  # Class number for buses
                return "Bus detected, processing terminated."
            vehicle_polygons.append(Polygon(coords))

        for parts in parse_file(lane_file):
            class_id, coords = int(parts[0]), [(float(parts[i]), float(parts[i+1])) for i in range(1, len(parts), 2)]
            if class_id == 0:  # Class number for blue lanes
                lane_polygons.append(Polygon(coords))
                lane_class_found = True

        if not lane_class_found:
            return "No lane data available."

        for v_poly in vehicle_polygons:
            for l_poly in lane_polygons:
                if v_poly.intersects(l_poly):
                    return "Lane violation detected. Reporting is needed."

        return "Vehicle is compliant."
    finally:
        os.remove(tmp_path)  # Clean up the temporary file

# Sample Flask endpoint (assuming Flask app is defined elsewhere)
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    image = Image.open(file.stream)  # Open the image from file stream
    result = process_image(image)  # Call the process image function
    return jsonify({'message': result})
