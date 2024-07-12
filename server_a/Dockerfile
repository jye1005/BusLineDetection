
FROM python:3.8

WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 로컬 파일 시스템에서 앱 파일 복사
COPY . /app

# Python 의존성 설치
RUN pip3 install streamlit Flask 

# Streamlit 포트 노출
EXPOSE 8501

# Streamlit 헬스 체크
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Streamlit 앱 실행
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

