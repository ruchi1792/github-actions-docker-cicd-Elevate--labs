# 🚀 CI/CD Pipeline with GitHub Actions, Docker & Kubernetes

![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-2088FF?style=for-the-badge&logo=githubactions)

## 📌 Project Overview

This project demonstrates an automated **CI/CD (Continuous Integration and Continuous Deployment) pipeline** using GitHub Actions, Docker, Docker Hub, and Kubernetes (Minikube).

The pipeline automatically tests a Python Flask application, builds a Docker image, pushes the image to Docker Hub, and deploys the latest application version to a local Kubernetes cluster.

A self-hosted GitHub Actions runner is used to deploy the application to Minikube running locally through Docker Desktop.

☁️ **No cloud infrastructure is required!**

## 🎯 Project Objectives

- ⚙️ Automate Python application testing using GitHub Actions.
- 🐳 Build Docker images automatically.
- 📦 Push Docker images to Docker Hub.
- ☸️ Deploy applications automatically to Kubernetes.
- 🖥️ Use a self-hosted GitHub Actions runner for local deployment.
- 🔍 Verify application health and deployment status.

## 🏗️ Project Architecture

```text
           👨‍💻 Developer
                 |
                 v
          📂 GitHub Repository
                 |
                 v
          ⚙️ GitHub Actions
                 |
                 v
          🧪 Run Python Tests
                 |
                 v
          🐳 Build Docker Image
                 |
                 v
          📦 Push to Docker Hub
                 |
                 v
          🖥️ Self-Hosted Runner
                 |
                 v
          ☸️ Local Minikube
                 |
                 v
          🚀 Kubernetes Deployment
                 |
                 v
             🟢 2 App Pods
                 |
                 v
          🌐 Kubernetes Service
                 |
                 v
          🐍 Flask Application
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python 3.12 | Application development |
| 🌶️ Flask | Web application framework |
| 🧪 Pytest | Automated testing |
| 🐳 Docker | Containerization |
| 🖥️ Docker Desktop | Local container runtime |
| 📦 Docker Hub | Docker image registry |
| ⚙️ GitHub Actions | CI/CD automation |
| 🖥️ Self-hosted Runner | Local deployment automation |
| ☸️ Kubernetes | Container orchestration |
| 🚀 Minikube | Local Kubernetes cluster |
| 🔧 kubectl | Kubernetes management |
| 🐧 Ubuntu WSL | Development environment |

## 📁 Project Structure

```text
github-actions-docker-cicd/
│
├── 📂 app/
│   ├── __init__.py
│   └── main.py
│
├── 📂 tests/
│   └── test_app.py
│
├── 📂 k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── 📂 .github/
│   └── 📂 workflows/
│       └── ci.yml
│
├── 🐳 Dockerfile
├── 🚫 .dockerignore
├── 🐳 docker-compose.yml
├── 📋 requirements.txt
└── 📖 README.md
```

## 🐍 Application Details

The project uses a Python Flask application with three endpoints.

### 🏠 1. Home Endpoint

```http
GET /
```

Returns application information and a welcome message.

### ❤️ 2. Health Endpoint

```http
GET /health
```

Checks whether the application is healthy.

**Expected Response:**

```json
{
  "status": "healthy"
}
```

### 🔖 3. Version Endpoint

```http
GET /version
```

Returns application version and deployment information.

**Expected Response:**

```json
{
  "version": "1.0",
  "deployment": "Local"
}
```

## ⚙️ CI/CD Pipeline Workflow

The GitHub Actions workflow is configured in:

```text
.github/workflows/ci.yml
```

The pipeline contains three jobs.

### 🧪 Job 1: Run Python Tests

- Checks out the repository.
- Sets up Python 3.12.
- Installs application dependencies.
- Executes automated tests using Pytest.

### 🐳 Job 2: Build and Push Docker Image

- Runs after successful Python tests.
- Sets up Docker Buildx.
- Logs in to Docker Hub using GitHub Secrets.
- Builds the Docker image.
- Pushes the image to Docker Hub with `latest` and commit SHA tags.

📦 **Docker Hub Repository:**

https://hub.docker.com/r/ruchiamey3117/cicd-app

### ☸️ Job 3: Deploy to Local Minikube

- Runs on the self-hosted GitHub Actions runner.
- Verifies Kubernetes connectivity.
- Updates the Kubernetes Deployment with the newly published Docker image.
- Waits for the deployment rollout.
- Verifies Kubernetes Deployments, Pods, and Services.

🚀 The deployment job runs only after the Docker image has been successfully pushed from a push to the `main` branch.

## 🔐 GitHub Secrets Configuration

The following repository secrets are configured under:

**GitHub Repository → Settings → Secrets and variables → Actions**

| Secret Name | Description |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_TOKEN` | Docker Hub access token |

🔒 These secrets allow GitHub Actions to authenticate with Docker Hub without exposing credentials in the workflow file.

## ☸️ Kubernetes Configuration

Kubernetes manifests are stored in the `k8s/` directory.

### 🚀 Deployment

File: `k8s/deployment.yaml`

The Deployment:

- Creates two application replicas.
- Uses the Docker Hub application image.
- Exposes container port `5000`.
- Uses `Always` as the image pull policy.

### 🌐 Service

File: `k8s/service.yaml`

The Service:

- Uses NodePort service type.
- Exposes application port `5000`.
- Uses NodePort `30007`.
- Routes traffic to application Pods.

## 📋 Prerequisites

Install and configure the following tools:

- 🐙 Git
- 🐍 Python 3.12
- 🐳 Docker Desktop
- 🐧 Ubuntu on WSL
- ☸️ Minikube
- 🔧 kubectl
- 🐙 GitHub account
- 📦 Docker Hub account

⚠️ Docker Desktop and Minikube must be running for local Kubernetes deployment.

The self-hosted runner must also be online.

## 💻 Running the Project Locally

### Step 1️⃣: Clone the Repository

```bash
git clone https://github.com/ruchi1792/github-actions-docker-cicd-Elevate--labs.git
```

### Step 2️⃣: Navigate to the Project

```bash
cd github-actions-docker-cicd-Elevate--labs
```

### Step 3️⃣: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4️⃣: Run Automated Tests

```bash
python -m pytest -v
```

### Step 5️⃣: Build the Docker Image

```bash
docker build -t cicd-app .
```

### Step 6️⃣: Run the Docker Container

```bash
docker run -d -p 5000:5000 --name cicd-app cicd-app
```

🌐 Access the application:

```text
http://localhost:5000
```

## ☸️ Kubernetes Deployment

### 1️⃣ Start Minikube

```bash
minikube start --driver=docker
```

### 2️⃣ Check the Cluster

```bash
kubectl get nodes
```

### 3️⃣ Apply Kubernetes Manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4️⃣ Check Deployments

```bash
kubectl get deployments
```

### 5️⃣ Check Pods

```bash
kubectl get pods
```

### 6️⃣ Check Services

```bash
kubectl get services
```

## 🌐 Accessing the Application

Forward the Kubernetes Service to local port `5002`:

```bash
kubectl port-forward service/cicd-app-service 5002:5000
```

⚠️ Keep the port-forward terminal running.

Open another terminal and test the endpoints:

```bash
curl http://127.0.0.1:5002/
curl http://127.0.0.1:5002/health
curl http://127.0.0.1:5002/version
```

## 📊 Project Verification Results

The completed project was successfully tested.

| Component | Result |
|---|---|
| 🧪 Python automated tests | ✅ Successful |
| 🐳 Docker image build | ✅ Successful |
| 📦 Docker Hub image push | ✅ Successful |
| ⚙️ GitHub Actions CI pipeline | ✅ Successful |
| 🖥️ Self-hosted runner | ✅ Successful |
| ☸️ Minikube deployment | ✅ Successful |
| 🚀 Kubernetes replicas | ✅ 2/2 Ready |
| 🟢 Application Pods | ✅ 2 Running |
| ❤️ Application health endpoint | ✅ Healthy |
| 🔖 Version endpoint | ✅ Successful |

### 🏆 GitHub Actions Pipeline Results

All three pipeline jobs completed successfully:

1. 🧪 Run Python Tests — **Passed**
2. 🐳 Build and Push Docker Image — **Passed**
3. ☸️ Deploy to Local Minikube — **Passed**

⏱️ Total execution time for the successful workflow run: approximately **1 minute and 17 seconds**.

## 📸 Project Screenshots

Project screenshots are collected separately as implementation evidence.

Recommended screenshots:

1. 📂 GitHub repository overview.
2. ⚙️ GitHub Actions successful pipeline.
3. 🧪 Python automated test results.
4. 🐳 Docker image build and push.
5. 📦 Docker Hub image tags.
6. ☸️ Kubernetes deployment and Pods.
7. 🌐 Kubernetes Service.
8. 🔍 Application endpoint testing.

## 🔗 Repository Information

🐙 **GitHub Repository:**

https://github.com/ruchi1792/github-actions-docker-cicd-Elevate--labs

🐳 **Docker Hub Repository:**

https://hub.docker.com/r/ruchiamey3117/cicd-app

## 🎓 Conclusion

This project demonstrates a complete automated CI/CD pipeline using GitHub Actions, Docker, Docker Hub, and Kubernetes.

It automates application testing, Docker image creation, image publishing, and deployment to a local Minikube cluster using a self-hosted GitHub Actions runner.

The project demonstrates practical experience with:

- ⚙️ CI/CD automation
- 🐳 Docker containerization
- ☸️ Kubernetes orchestration
- 🔄 Automated deployment
- 🖥️ Self-hosted GitHub Actions runners
- 🧪 Software testing
- 🐧 Linux and WSL environments

🚀 **Project Status: Successfully Completed**

---

⭐ If you find this project useful, feel free to explore the repository and learn from the implementation!
