# AI-Play DL-API

**(추가되는 내용에 맞춰 지속 수정 필요)**

Deep Learning 기능을 위한 API 서버

## Stack

Python 3.8.12  
[FastAPI 0.73.0](fastapi.tiangolo.com)

## 준비 사항

```
# 필요한 모듈 및 패키지 설치
python -m pip install -r requirements.txt

# DB 테이블 마이그레이션
#(배포 시에는 배포 완료 후 별도로 시행할 것. 처음 한 번 하면 내용 변경되지 않는 한 또 할 필요 없음.)
alembic upgrade head
```

## 실행

```
uvicorn main:app --reload
```

## 배포 플랫폼 및 서버 주소

- 플랫폼 : Google App Engine
- 주소 : [https://ai-play-dl-api.du.r.appspot.com](https://ai-play-dl-api.du.r.appspot.com)

## 배포 과정

0. app.yaml, Dockerfile 작성(port 8080으로 변경 필요 - App Engine default), .env 배포용으로 변경(이를 읽어들임)
1. gcloud app create --project=ai-play-dl-api
2. gcloud components install app-engine-python
3. gcloud app deploy # 이전에 Google App Engine 프로젝트에 결제 설정 되어 있는지 확인 필요
