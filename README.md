# AI-Play DL-API

Deep Learning의 실제 활용 사례 경험을 제공하기 위한 API 서버

## Stack

- Python 3.8.12
- [FastAPI 0.73.0](fastapi.tiangolo.com)
- Google Cloud Platform
  - App Engine
  - Cloud Build

## 준비 사항

```
# 필요한 모듈 및 패키지 설치
python -m pip install -r requirements.txt

# DB 테이블 마이그레이션
#(배포 시에 한 번 시행하고 이후에는 내용 변경되지 않는 한 배포마다 매번 할 필요 없음.)
#(Dockerfile 내의 해당 코드를 필요에 따라 주석 처리 혹은 해제 후 배포하기)
alembic upgrade head
```

## 개발 서버 실행

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

- 이후 Cloud Build에 Github Repo를 연결하여 배포 진행하였음
