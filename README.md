# 🚀 CI/CD Pipeline with GitHub Actions, Docker & Kubernetes

![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Workflow-blue?style=for-the-badge&logo=githubactions)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployment-326CE5?style=for-the-badge&logo=kubernetes)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.1-black?style=for-the-badge&logo=flask)

A practical end-to-end **CI/CD automation project** that demonstrates how to test, build, publish, and deploy a Python Flask application using GitHub Actions, Docker Hub, and a local Kubernetes cluster with Minikube.

The pipeline automatically runs tests, builds and pushes a Docker image, and deploys the updated application to Minikube whenever code is pushed to the `main` branch.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objectives](#-project-objectives)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Application Features](#-application-features)
- [CI/CD Pipeline Workflow](#-cicd-pipeline-workflow)
- [Docker Configuration](#-docker-configuration)
- [Kubernetes Deployment](#-kubernetes-deployment)
- [Local Setup and Execution](#-local-setup-and-execution)
- [Verification](#-verification)
- [Project Screenshots](#-project-screenshots)
- [GitHub and Docker Hub](#-github-and-docker-hub)
- [Key Learnings](#-key-learnings)

---

## 📖 Project Overview

The objective of this project is to implement an automated CI/CD pipeline for a containerized Flask application without depending on a cloud Kubernetes service.

The pipeline uses:

- **GitHub Actions** for continuous integration and delivery.
- **Pytest** for automated application testing.
- **Docker** for containerizing the Flask application.
- **Docker Hub** for storing and distributing Docker images.
- **Self-hosted GitHub Actions Runner** for local deployment execution.
- **Minikube** for running Kubernetes locally.
- **Kubernetes Deployment and Service** for application orchestration and access.

The deployment process is automated after a successful build and test process.

## 🎯 Project Objectives

- Implement Continuous Integration using GitHub Actions.
- Automate Python application testing using Pytest.
- Build Docker images automatically.
- Push Docker images to Docker Hub.
- Configure a self-hosted GitHub Actions runner.
- Deploy the application to a local Minikube cluster.
- Manage application replicas using Kubernetes Deployments.
- Expose the application through a Kubernetes NodePort Service.
- Verify application health and deployment status.

---

## 🏗️ Architecture

```text
              Developer
                  |
                  | Git Push
                  v
             GitHub Repository
                  |
                  v
          GitHub Actions Workflow
                  |
                  v
          +-------------------+
          |   CI: Run Tests   |
          |      Pytest       |
          +-------------------+
                  |
                  v
          +-------------------+
          | Build Docker Image|
          |     Docker        |
          +-------------------+
                  |
                  v
             Docker Hub
                  |
                  v
          Self-Hosted Runner
                  |
                  v
             Minikube
                  |
                  v
          Kubernetes Deployment
                  |
                  v
             Kubernetes Pods
                  |
                  v
          Kubernetes NodePort
                  |
                  v
          Flask Application
```

### 🔄 Pipeline Flow

1. Developer pushes code to GitHub.
2. GitHub Actions triggers the workflow.
3. Python dependencies are installed.
4. Pytest executes the application tests.
5. Docker image is built after successful tests.
6. Docker image is pushed to Docker Hub.
7. Self-hosted runner executes the deployment job.
8. Kubernetes Deployment updates the application image.
9. Kubernetes verifies the rollout.
10. Application availability is tested.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Flask 3.1.1 | Web application framework |
| Pytest 8.3.5 | Automated testing |
| Git & GitHub | Version control and source code hosting |
| GitHub Actions | CI/CD automation |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Docker Compose | Local container management |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes cluster |
| kubectl | Kubernetes cluster management |
| WSL Ubuntu | Linux development environment |

---

## 📁 Project Structure

```text
github-actions-docker-cicd/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD workflow
│
├── app/
│   ├── __init__.py
│   └── main.py                 # Flask application
│
├── tests/
│   └── test_app.py             # Automated application tests
│
├── k8s/
│   ├── deployment.yaml         # Kubernetes Deployment
│   └── service.yaml            # Kubernetes NodePort Service
│
├── screenshots/                # Project screenshots
│
├── .dockerignore
├── .gitignore
├── Dockerfile                  # Docker image configuration
├── docker-compose.yml          # Local container configuration
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ Application Features

The Flask application provides three HTTP endpoints.

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Returns application information |
| `/health` | GET | Returns application health status |
| `/version` | GET | Returns application version information |

### Example API Responses

**GET /**

```json
{
  "application": "CI/CD Demo Application",
  "message": "Welcome! Application is running successfully.",
  "status": "Running"
}
```

**GET /health**

```json
{
  "status": "healthy"
}
```

**GET /version**

```json
{
  "version": "1.0",
  "deployment": "Local"
}
```

---

## 🔁 CI/CD Pipeline Workflow

The workflow is configured in:

`.github/workflows/ci.yml`

### Job 1: Run Python Tests

- Checks out the GitHub repository.
- Sets up Python 3.12.
- Installs project dependencies.
- Executes automated tests using Pytest.

### Job 2: Build and Push Docker Image

Runs after successful tests.

- Configures Docker Buildx.
- Authenticates with Docker Hub using GitHub Secrets.
- Builds the Docker image.
- Pushes two image tags:
  - `latest`
  - Git commit SHA

### Job 3: Deploy to Local Minikube

Runs after the Docker image has been pushed.

- Uses the self-hosted Linux runner.
- Verifies Kubernetes connectivity.
- Updates the Kubernetes Deployment with the new image.
- Checks rollout status.
- Verifies Deployments, Pods, and Services.

### 🔐 GitHub Repository Secrets

The following repository secrets are configured:

| Secret | Purpose |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_TOKEN` | Docker Hub access token |

Secrets are stored in GitHub repository settings and are not included in the source code.

---

## 🐳 Docker Configuration

The application is packaged into a Docker image using the project Dockerfile.

### Build Docker Image

```bash
docker build -t cicd-app .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 --name cicd-app-local cicd-app
```

### Verify Container

```bash
docker ps
```

### Docker Hub Repository

Published image:

`ruchiamey3117/cicd-app`

[View Docker Hub Repository](https://hub.docker.com/r/ruchiamey3117/cicd-app)

---

## ☸️ Kubernetes Deployment

The application is deployed to a local Minikube Kubernetes cluster.

### Start Minikube

```bash
minikube start --driver=docker
```

### Apply Kubernetes Manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Verify Deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### Deployment Configuration

- Deployment name: `cicd-app`
- Desired replicas: `2`
- Container port: `5000`
- Service type: `NodePort`
- NodePort: `30007`

### Access the Application

Start port forwarding:

```bash
kubectl port-forward service/cicd-app-service 5002:5000
```

Keep this command running in the terminal.

Open another terminal and test:

```bash
curl http://127.0.0.1:5002/
curl http://127.0.0.1:5002/health
curl http://127.0.0.1:5002/version
```

---

## 🧪 Local Setup and Execution

### Prerequisites

Install the following tools:

- Git
- Python 3.12
- Docker Desktop
- Docker Compose
- kubectl
- Minikube

### 1. Clone Repository

```bash
git clone https://github.com/ruchi1792/github-actions-docker-cicd-Elevate--labs.git
```

### 2. Navigate to Project

```bash
cd github-actions-docker-cicd-Elevate--labs
```

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run Tests

```bash
python3 -m pytest -v
```

### 5. Build Docker Image

```bash
docker build -t cicd-app .
```

### 6. Start Minikube

```bash
minikube start --driver=docker
```

### 7. Deploy Application

```bash
kubectl apply -f k8s/
```

### 8. Verify Kubernetes Resources

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

---

## ✅ Verification

The project pipeline was successfully tested with the following results:

| Component | Verification |
|---|---|
| Python application | Running |
| Pytest | 3 tests passed |
| GitHub Actions CI | Successful |
| Docker image build | Successful |
| Docker Hub push | Successful |
| Self-hosted runner | Connected |
| Minikube cluster | Running |
| Kubernetes Deployment | 2/2 replicas ready |
| Kubernetes Pods | 2 Pods running |
| Kubernetes Service | NodePort configured |
| Flask endpoints | Successfully responding |

---

## 📸 Project Screenshots

The following screenshots demonstrate the implementation and successful execution of the CI/CD pipeline.

### 1. GitHub Repository Overview

Shows the project repository, source code, configuration files, and project structure.

![GitHub Repository](screenshots/01-github-repository.png)

### 2. GitHub Actions – Successful CI/CD Pipeline

Demonstrates the successful execution of all three workflow jobs: testing, Docker build and push, and Kubernetes deployment.

![GitHub Actions Pipeline](screenshots/02-github-actions-success.png)

### 3. Python Automated Testing

Shows the Pytest execution results and successful application test cases.

![Python Test Results](screenshots/03-python-tests.png)

### 4. Docker Image Build and Push

Demonstrates the Docker image build process and successful publishing to Docker Hub.

![Docker Build and Push](screenshots/04-docker-build-push.png)

### 5. Docker Hub Repository

Shows the published Docker image and available image tags.

![Docker Hub Repository](screenshots/05-docker-hub.png)

### 6. Kubernetes Deployment and Pods

Shows the Kubernetes Deployment and the two running application Pods in Minikube.

![Kubernetes Deployment and Pods](screenshots/06-kubernetes-pods.png)

### 7. Kubernetes Service

Demonstrates the Kubernetes NodePort Service configuration used to expose the application.

![Kubernetes Service](screenshots/07-kubernetes-service.png)

### 8. Flask Application Running

Shows the successful responses from the Flask application endpoints.

![Flask Application Responses](screenshots/08-application-running.png)

---

## 🔗 GitHub and Docker Hub

**GitHub Repository**

[github.com/ruchi1792/github-actions-docker-cicd-Elevate--labs](https://github.com/ruchi1792/github-actions-docker-cicd-Elevate--labs)

**Docker Hub Repository**

[hub.docker.com/r/ruchiamey3117/cicd-app](https://hub.docker.com/r/ruchiamey3117/cicd-app)

---

## 📚 Key Learnings

Through this project, I gained practical experience in:

- Designing automated CI/CD workflows.
- Implementing continuous integration with GitHub Actions.
- Writing and executing Python unit tests.
- Containerizing applications using Docker.
- Publishing Docker images to Docker Hub.
- Configuring GitHub self-hosted runners.
- Deploying applications to Kubernetes.
- Managing Kubernetes Deployments, Pods, and Services.
- Automating local Kubernetes deployments.
- Troubleshooting CI/CD and container deployment issues.

---

## 🎓 Project Conclusion

This project demonstrates an end-to-end CI/CD implementation using GitHub Actions, Docker, Docker Hub, and Kubernetes with Minikube.

The automated pipeline successfully tests the Flask application, builds and publishes Docker images, and deploys the updated application to a local Kubernetes cluster.

It provides practical experience with DevOps automation, containerization, and Kubernetes deployment without requiring a cloud-hosted Kubernetes environment.

**Project Status: Successfully Implemented and Verified.**

---

⭐ If you find this project useful, consider giving the repository a star!
