FROM ultralytics/ultralytics:latest-arm64

WORKDIR /app
COPY . /app
RUN pip install Flask shapely gunicorn 
RUN pip install dill 
# 필요한 경우, 추가적인 모델 파일 다운로드 명령어를 여기에 포함시킵니다.
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "app:app"]
EXPOSE 5002