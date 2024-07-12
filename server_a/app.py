import streamlit as st
import requests
from PIL import Image
import io

# Streamlit 페이지 설정
st.title('Image Processing')
st.write('이미지를 업로드 해주세요.')

# 이미지 업로드 위젯
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # 이미지를 서버 B로 전송
    url = 'http://server_b:5002/process_image'
    files = {'image': ('image', uploaded_file.getvalue(), uploaded_file.type)}
    response = requests.post(url, files=files)
    
    if response.ok:
        # 서버 B에서 반환된 결과를 출력
        result = response.json()
        st.write(result['message'])
        # 업로드된 이미지 표시
        
    else:
        # 오류 메시지 표시
        st.error('Failed to Server response: {}'.format(response.status_code))
        if response.text:
            st.error('Response error message: {}'.format(response.text))
