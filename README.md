# ❇️ AI Play DL-API

- 딥 러닝 체험용 모델 API
- 머신 러닝 및 딥 러닝 프로젝트 관리 API (관리자 기능)

## :one: Stack

- Python 3.8.12
- FastAPI 0.73.0
- PyTorch 1.11.0
- JWT
- Swagger
- Google Cloud Platform
  - App Engine
  - Cloud Build

<br/>

## :two: 배포 플랫폼 및 서버 주소

- 플랫폼 : Google App Engine
- 주소 : https://ai-play-dl-api.du.r.appspot.com

<br/>

## :three: API 명세

- DOCS(Swagger) : https://ai-play-dl-api.du.r.appspot.com/docs

| Method                | URL                | Description                                                                               |
| --------------------- | ------------------ | ----------------------------------------------------------------------------------------- |
| AI 프로젝트 관리 기능 |                    |                                                                                           |
| POST                  | /posts/            | 웹 앱 내 인공지능 체험 프로젝트 목록의 게시물(post)을 추가하는 기능(관리자 전용)          |
| PUT                   | /posts/{post_id}   | 웹 앱 내 인공지능 체험 프로젝트 목록의 게시물(post)을 수정하는 기능(관리자 전용)          |
| DELETE                | /posts/{post_id}   | 웹 앱 내 인공지능 체험 프로젝트 목록의 게시물(post)을 삭제하는 기능(관리자 전용)          |
| GET                   | /posts/            | 웹 앱 내 인공지능 체험 프로젝트 목록의 게시물(post) 전체를 불러오는 기능(관리자 전용)     |
| GET                   | /posts/{div}       | div(ml/dl) 값에 해당되는 체험 프로젝트 목록의 게시물(post)들을 불러오는 기능              |
| GET                   | /posts/{post_id}   | 게시물 고유 번호(post_id) 값에 해당되는 체험 프로젝트 목록의 게시물(post)을 불러오는 기능 |
| 딥 러닝 체험 기능     |                    |                                                                                           |
| POST                  | /cv/hair_color_gen | 인물 이미지 넣으면 머리색 바꿔주는 딥 러닝 모델 API                                       |

<br/>

## :four: 트러블 슈팅 기록

- https://github.com/AI-Play/DL-API/discussions

<br/>

## :five: 배포 과정

1. app.yaml, Dockerfile 작성(port 8080으로 변경 필요 -> ∵ App Engine의 default port 값)
2. .env 배포용으로 변경 (∵ 이를 읽어들임)
3. gcloud app create --project=ai-play-dl-api
4. gcloud components install app-engine-python
5. gcloud app deploy (이전에 Google App Engine 프로젝트에 결제 설정 되어 있는지 확인 필요)
6. 이후 Cloud Build에 Github Repo를 연결하여 배포 진행

<br/>

## :six: 개발 환경 준비 사항

<details>
  <summary><b>준비 사항</b></summary>

  ```
  # 필요한 모듈 및 패키지 설치
  python -m pip install -r requirements.txt

  # DB 테이블 마이그레이션
  # (배포 시에는 배포 완료 후 별도로 시행할 것. 처음 한 번 하면 내용 변경되지 않는 한 또 할 필요 없음.)
  # (Dockerfile 내의 해당 코드를 필요에 따라 주석 처리 혹은 해제 후 배포하기)
  alembic upgrade head
  ```

  ##### 개발 서버 실행

  ```
  uvicorn main:app --reload
  ```
</details>