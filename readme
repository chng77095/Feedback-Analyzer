Markdown
# Feedback Analyzer Microservice

A containerized Python web service that performs sentiment analysis on user feedback. The application is built with Flask, packaged into a Docker container, hosted on Amazon Elastic Container Registry (ECR), and deployed on an AWS EC2 instance.

---

## Architecture Overview

```text
[ Client / Terminal ] 
        │ (POST /analyze)
        ▼
[ AWS EC2 Instance ] ── Port 8080
        │
        ▼
[ Docker Container ] ── (Python / Flask API)
API Framework: Flask (Python)

Containerization: Docker

Container Registry: AWS ECR (us-east-1)

Cloud Infrastructure: AWS EC2 (Amazon Linux 2023, us-east-2)

Project Structure
Plaintext
feedback-analyzer/
├── .gitignore                    # Prevents sensitive files (.pem) from entering source control
├── Dockerfile                    # Container configuration file
├── README.md                     # Project documentation
├── app.py                        # Main Flask application logic
└── requirements.txt              # Python dependencies
Getting Started Locally
Prerequisites
Python 3.9+

Docker Installed and running

Running the App Locally
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd feedback-analyzer
Build the Docker image:

Bash
docker build -t feedback-analyzer .
Run the container:

Bash
docker run -d -p 8080:8080 --name analyzer feedback-analyzer
Test the API endpoint:

Bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"feedback": "This service is great!"}'
AWS Deployment Architecture
1. Push Image to Amazon ECR
Authenticate Docker with your ECR registry and push the image:

Bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
docker tag feedback-analyzer:latest <ACCOUNT_ID>[.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest](https://.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest)
docker push <ACCOUNT_ID>[.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest](https://.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest)
2. AWS EC2 Configuration
Security Group Inbound Rules:

Port 22 (SSH): Accessible from operator IP.

Port 8080 (Custom TCP): Public access (0.0.0.0/0) for incoming API requests.

IAM Role: Attached AmazonEC2ContainerRegistryReadOnly policy to allow the EC2 instance to pull images directly from Amazon ECR without embedding permanent credentials.

3. Running on EC2
Inside the EC2 SSH terminal:

Bash
# Pull and execute container from ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
docker run -d -p 8080:8080 --restart unless-stopped --name analyzer <ACCOUNT_ID>[.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest](https://.dkr.ecr.us-east-1.amazonaws.com/feedback-analyzer:latest)
API Usage
POST /analyze
Analyzes the sentiment of a given text string.

Request Body:

JSON
{
  "feedback": "This service is great!"
}
Response (200 OK):

JSON
{
  "feedback": "This service is great!",
  "sentiment": "POSITIVE"
}
