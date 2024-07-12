from flask import Flask, request, jsonify
from PIL import Image
import io
from result import process_image # 모델 함수 임포트

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # 메모리에서 이미지를 바로 처리
    image = Image.open(file.stream)
    result = process_image(image)  # 모델 함수를 사용하여 이미지 처리
    
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
