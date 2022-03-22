# 사용법

python StarGAN/test.py

test.py의 40~41번째 줄이 이미지의 경로를 받아서 모델에 Input 값으로
넣어주게 됩니다.

# AI-Play DL-API

**(추가되는 내용에 맞춰 지속 수정 필요)**

Deep Learning 기능을 위한 API 서버

## Stack

Python 3.8.12  
[FastAPI 0.73.0](fastapi.tiangolo.com)

## 준비 사항

```
python -m pip install -r requirements.txt
```

## 실행

```
uvicorn main:app --reload --port 8002
```
