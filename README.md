# ❇️ AI Play DL-API

- API server for deep learning experience models
- API server for managing machine learning and deep learning projects (Admin functions)

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

## :two: Deployment Platform and Server Address

- Platform: Google App Engine
- Address: [https://ai-play-dl-api.du.r.appspot.com](https://ai-play-dl-api.du.r.appspot.com)

<br/>

## :three: API Specifications

- DOCS(Swagger): [https://ai-play-dl-api.du.r.appspot.com/docs](https://ai-play-dl-api.du.r.appspot.com/docs)

| Method                   | URL                | Description                                                                              |
| ------------------------ | ------------------ | ---------------------------------------------------------------------------------------- |
| AI Project Management    |                    |                                                                                          |
| POST                     | /posts/            | Add a post to the list of AI experience projects in the web app (Admin only)             |
| PUT                      | /posts/{post_id}   | Edit a post in the list of AI experience projects in the web app (Admin only)            |
| DELETE                   | /posts/{post_id}   | Delete a post from the list of AI experience projects in the web app (Admin only)        |
| GET                      | /posts/            | Retrieve all posts in the list of AI experience projects in the web app (Admin only)     |
| GET                      | /posts/{div}       | Retrieve posts in the list of experience projects corresponding to the div (ml/dl) value |
| GET                      | /posts/{post_id}   | Retrieve a post from the list of AI experience projects based on the post_id value       |
| Deep Learning Experience |                    |                                                                                          |
| POST                     | /cv/hair_color_gen | Deep learning model API that changes hair color when a person image is input             |

<br/>

## :four: Troubleshooting Records

- [DL-API Discussions](https://github.com/AI-Play/DL-API/discussions)

<br/>

## :five: Deployment Process

1. Write app.yaml and Dockerfile (change port to 8080 -> ∵ default port value for App Engine)
2. Change .env for deployment (as it is read)
3. gcloud app create --project=ai-play-dl-api
4. gcloud components install app-engine-python
5. gcloud app deploy (Check if payment is set up for the Google App Engine project before deploying)
6. Connect the Github Repo to Cloud Build for deployment

<br/>

## :six: Development Environment Setup

<details>
  <summary><b>Prerequisites</b></summary>

```
# Install necessary modules and packages
python -m pip install -r requirements.txt

# DB table migration
# (To be done separately after deployment, unless the content changes. Uncomment or comment out the relevant code in the Dockerfile before deployment as needed)
alembic upgrade head
```

##### Run Development Server

```
uvicorn main:app --reload
```

</details>
