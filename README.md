# 🚀 Feedback Analyzer Microservice

A **containerized AI-powered REST API** that analyzes customer feedback and classifies its sentiment. The application is built with **Python and Flask**, containerized with **Docker**, stored in **Amazon Elastic Container Registry (ECR)**, and deployed to **AWS EC2**.

This project demonstrates an end-to-end workflow for taking an AI/ML application from **local development to a cloud-hosted production-style service**.

---

## 📌 Project Overview

Customer feedback can provide valuable insight into user satisfaction, but manually analyzing large volumes of text is inefficient.

The Feedback Analyzer provides an API that accepts user feedback and returns a sentiment classification such as **POSITIVE** or **NEGATIVE**.

### Example

**Input**

```json
{
  "feedback": "This service is great!"
}
```

**Output**

```json
{
  "feedback": "This service is great!",
  "sentiment": "POSITIVE"
}
```

---

## ☁️ Architecture

```text
                    Client
                      │
                      │ POST /analyze
                      ▼
              ┌─────────────────┐
              │     AWS EC2     │
              │    Port 8080    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Docker Container│
              │                 │
              │ Python + Flask  │
              │ Sentiment Model │
              └────────┬────────┘
                       ▲
                       │ Pull Docker Image
                       │
              ┌────────┴────────┐
              │     AWS ECR     │
              │ Docker Registry │
              └─────────────────┘
```

### Deployment Flow

```text
Develop
   ↓
Build Docker Image
   ↓
Push Image to AWS ECR
   ↓
EC2 Pulls Image
   ↓
Docker Runs Container
   ↓
REST API Available on Port 8080
```

---

## 🛠️ Technologies

| Category              | Technology          |
| --------------------- | ------------------- |
| Programming Language  | Python              |
| API Framework         | Flask               |
| AI / Machine Learning | Sentiment Analysis  |
| Containerization      | Docker              |
| Cloud Platform        | Amazon Web Services |
| Compute               | AWS EC2             |
| Container Registry    | AWS ECR             |
| Cloud Security        | AWS IAM             |
| Operating System      | Amazon Linux 2023   |
| API Format            | REST / JSON         |

---

## 💡 Key Features

* 🤖 AI-powered sentiment classification
* 🌐 REST API for real-time predictions
* 🐳 Fully containerized with Docker
* ☁️ Deployed to AWS EC2
* 📦 Docker image hosted in Amazon ECR
* 🔐 IAM-based authentication for ECR access
* 🔄 Automatic Docker container restart
* 📡 JSON-based API requests and responses
* 🧩 Simple architecture that can be extended into a larger ML service

---

## 🧠 AI / Machine Learning Component

The application processes incoming text and generates a sentiment prediction.

Supported sentiment output includes:

```text
POSITIVE
NEGATIVE
```

The machine learning component is integrated directly into the Flask API, allowing predictions to be generated through an HTTP request rather than requiring users to interact with a notebook or local Python script.

This demonstrates how a machine learning model can be transformed into a **deployable cloud application**.

---

## 🐳 Docker Implementation

The application is packaged as a Docker image so that the same environment can be used across development and deployment.

### Build the Image

```bash
docker build -t feedback-analyzer .
```

### Run Locally

```bash
docker run -d \
  -p 8080:8080 \
  --name analyzer \
  feedback-analyzer
```

The API is then available at:

```text
http://localhost:8080
```

---

## 🧪 API Usage

### `POST /analyze`

Analyzes the sentiment of submitted feedback.

### Request

```json
{
  "feedback": "This service is great!"
}
```

### Response

```json
{
  "feedback": "This service is great!",
  "sentiment": "POSITIVE"
}
```

### Example cURL Request

```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"feedback": "This service is great!"}'
```

---

## ☁️ AWS Deployment

The application is deployed using an AWS-based container workflow.

### 1. Amazon ECR

The Docker image is pushed to **Amazon Elastic Container Registry**.

```bash
aws ecr get-login-password --region us-east-1 | \
docker login \
--username AWS \
--password-stdin \
<ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

Tag the image:

```bash
docker tag feedback-analyzer:latest \
<ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest
```

Push the image:

```bash
docker push \
<ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest
```

---

### 2. AWS EC2

An **Amazon Linux 2023 EC2 instance** hosts the Docker container.

The EC2 security group is configured to allow:

```text
Port 22     → SSH administration
Port 8080   → API traffic
```

The container is launched with:

```bash
docker run -d \
  -p 8080:8080 \
  --restart unless-stopped \
  --name analyzer \
  <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest
```

The `--restart unless-stopped` option allows Docker to automatically restart the application if the container stops or the server reboots.

---

## 🔐 Cloud Security

The EC2 instance uses an **IAM role** with the:

```text
AmazonEC2ContainerRegistryReadOnly
```

policy.

This allows the EC2 instance to pull the Docker image from ECR without storing long-lived AWS access keys directly on the server.

### Security Configuration

```text
EC2
 │
 ├── IAM Role
 │     └── ECR Read-Only Access
 │
 └── Security Group
       ├── SSH : 22
       └── API : 8080
```

This approach demonstrates the use of **AWS identity and access management principles** rather than embedding permanent credentials into the application.

---

## 📂 Project Structure

```text
feedback-analyzer/
│
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
└── requirements.txt
```

### File Descriptions

| File               | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| `app.py`           | Flask API and sentiment-analysis logic                    |
| `Dockerfile`       | Defines the application container                         |
| `requirements.txt` | Python dependencies                                       |
| `.gitignore`       | Prevents sensitive/unnecessary files from being committed |
| `README.md`        | Project documentation                                     |

---

## 💻 Run Locally

### Prerequisites

* Python 3.9+
* Docker
* AWS CLI *(only required for AWS deployment)*

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd feedback-analyzer
```

### Build Docker Image

```bash
docker build -t feedback-analyzer .
```

### Start Container

```bash
docker run -d \
  -p 8080:8080 \
  --name analyzer \
  feedback-analyzer
```

### Test the API

```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"feedback": "This service is great!"}'
```

---

## 📊 Skills Demonstrated

### Cloud Engineering

* AWS EC2
* Amazon ECR
* AWS IAM
* Security Groups
* Cloud-based application deployment

### DevOps

* Docker containerization
* Container image management
* Application deployment workflow
* Automated container restart
* Linux server administration

### AI / Machine Learning

* Natural language processing
* Sentiment classification
* Model inference
* ML model integration into a REST API

### Software Engineering

* Python
* Flask
* REST APIs
* JSON
* Dependency management
* Environment isolation

---

## 🔮 Future Improvements

Potential next steps for the project include:

* [ ] Add HTTPS using an AWS Application Load Balancer
* [ ] Add CloudWatch monitoring and logging
* [ ] Add automated CI/CD with GitHub Actions
* [ ] Add unit and integration tests
* [ ] Add multiple sentiment categories
* [ ] Add batch feedback analysis
* [ ] Store analyzed feedback in a database
* [ ] Add authentication and API keys
* [ ] Deploy using AWS ECS instead of EC2
* [ ] Add model performance monitoring

---

## 🎯 What This Project Demonstrates

This project goes beyond developing a machine learning model in a notebook.

It demonstrates the ability to:

> **Build an AI application → package it with Docker → publish it to a container registry → configure cloud infrastructure → securely deploy it to AWS → expose the model through a REST API.**

This represents an end-to-end **AI/ML cloud deployment workflow** and provides practical experience across **cloud engineering, DevOps, machine learning, and backend development**.

---

Hopefully you get something like this:
<img width="1705" height="937" alt="Screenshot 2026-08-29 at 5 49 08 PM" src="https://github.com/user-attachments/assets/362b5bbf-9a4f-4f5c-9def-69ff0683d2b6" />

