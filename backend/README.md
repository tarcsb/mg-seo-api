
# SEO Analysis Backend Service - MVP

This backend service provides various SEO analysis endpoints, including content optimization, technical SEO audits, local SEO enhancement, competitor comparison, and more using the Perplexity API. The MVP focuses on showcasing the communication between SEO analysis and Perplexity, including examples of SEO routes.

## Table of Contents

- [SEO Analysis Backend Service - MVP](#seo-analysis-backend-service---mvp)
  - [Prerequisites](#prerequisites)
  - [Setup and Running the Application](#setup-and-running-the-application)
    - [macOS](#macos)
    - [Windows (WSL2)](#windows-wsl2)
    - [Linux](#linux)
    - [Docker](#docker)
  - [Deploying the Application](#deploying-the-application)
    - [Deploying to Heroku](#deploying-to-heroku)
    - [Deploying to Render](#deploying-to-render)
    - [Deploying to AWS](#deploying-to-aws)
  - [Using ngrok](#using-ngrok)
  - [Using the API](#using-the-api)
    - [1. Basic Perplexity Analysis](#1-basic-perplexity-analysis)
    - [2. Content Optimization Analysis](#2-content-optimization-analysis)
    - [3. Technical SEO Audit](#3-technical-seo-audit)
    - [4. Local SEO Enhancement](#4-local-seo-enhancement)
    - [5. Competitor Comparison](#5-competitor-comparison)
    - [6. Ecommerce SEO Optimization](#6-ecommerce-seo-optimization)
    - [7. Content Gap Analysis](#7-content-gap-analysis)
    - [8. Backlink Strategy](#8-backlink-strategy)
  - [Testing](#testing)
    - [Test Types](#test-types)
    - [Running Tests](#running-tests)
  - [Running with Docker](#running-with-docker)
  - [Running with Docker Compose](#running-with-docker-compose)
  - [Development Notes](#development-notes)
  - [TODO - Future Features](#todo---future-features)
  - [License](#license)

## Prerequisites

- **Python 3.11 or Higher**: Required to run the application. Install it from [here](https://www.python.org/downloads/).
- **A Code Editor**: A code editor like [VS Code](https://code.visualstudio.com/) is recommended.
- **A Perplexity API Key**: Sign up and get your API key from Perplexity.

## Setup and Running the Application

### macOS

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.11**:
   ```bash
   brew install python@3.11
   ```

3. **Clone the Repository and Navigate to the Project Directory**:
   ```bash
   git clone https://github.com/your-repo/seo-analysis-tool-backend.git
   cd seo-analysis-tool-backend
   ```

4. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Create a `.env` File**:
   ```bash
   touch .env
   ```

   Add the following to `.env`:
   ```
   PERPLEXITY_API_KEY=your_perplexity_api_key
   ```

7. **Run the Application**:
   ```bash
   flask run
   ```

### Windows (WSL2)

1. **Install WSL2**:
   Follow the official guide to install WSL2: [WSL Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install).

2. **Install a Linux Distribution** (e.g., Ubuntu) from the Microsoft Store.

3. **Set Up Python 3.11 in WSL2**:
   ```bash
   sudo apt update
   sudo apt install python3.11 python3.11-venv
   ```

4. **Clone the Repository and Navigate to the Project Directory**:
   ```bash
   git clone https://github.com/your-repo/seo-analysis-tool-backend.git
   cd seo-analysis-tool-backend
   ```

5. **Set Up a Virtual Environment**:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

6. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

7. **Create a `.env` File**:
   ```bash
   touch .env
   ```

   Add the following to `.env`:
   ```
   PERPLEXITY_API_KEY=your_perplexity_api_key
   ```

8. **Run the Application**:
   ```bash
   flask run
   ```

### Linux

1. **Install Python 3.11**:
   ```bash
   sudo apt update
   sudo apt install python3.11 python3.11-venv
   ```

2. **Clone the Repository and Navigate to the Project Directory**:
   ```bash
   git clone https://github.com/your-repo/seo-analysis-tool-backend.git
   cd seo-analysis-tool-backend
   ```

3. **Set Up a Virtual Environment**:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` File**:
   ```bash
   touch .env
   ```

   Add the following to `.env`:
   ```
   PERPLEXITY_API_KEY=your_perplexity_api_key
   ```

6. **Run the Application**:
   ```bash
   flask run
   ```

### Docker

1. **Install Docker**:
   Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) for your operating system.

2. **Create a `Dockerfile` in the Project Root**:

   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app

   COPY . .

   RUN pip install -r requirements.txt

   ENV FLASK_APP=run.py
   ENV PERPLEXITY_API_KEY=your_perplexity_api_key

   EXPOSE 5000

   CMD ["flask", "run", "--host=0.0.0.0"]
   ```

3. **Build the Docker Image**:
   ```bash
   docker build -t seo-analysis-backend .
   ```

4. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 seo-analysis-backend
   ```

## Deploying the Application

### Deploying to Heroku

1. **Login to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a New Heroku App**:
   ```bash
   heroku create your-app-name
   ```

3. **Set Environment Variables on Heroku**:
   ```bash
   heroku config:set PERPLEXITY_API_KEY=your_perplexity_api_key
   ```

4. **Deploy to Heroku**:
   ```bash
   git push heroku main
   ```

### Deploying to Render

1. **Create an Account on Render**: Sign up at [Render.com](https://render.com/).

2. **Create a New Web Service**: Connect your GitHub repository to Render.

3. **Set Environment Variables**: In the Render dashboard, set the `PERPLEXITY_API_KEY` environment variable.

4. **Deploy the Application**: Render will automatically deploy your application upon pushing changes to the connected GitHub repository.

### Deploying to AWS

1. **Create an AWS Account**: Sign up at [AWS](https://aws.amazon.com/).

2. **Set Up AWS Elastic Beanstalk**: Install the Elastic Beanstalk CLI and initialize your Elastic Beanstalk application.

3. **Set Environment Variables**: Use the AWS Management Console to set `PERPLEXITY_API_KEY` in the Elastic Beanstalk environment settings.

## Using ngrok

1. **Install ngrok**: Download ngrok from [here](https://ngrok.com/download) and follow the installation instructions.

2. **Expose Your Local Server**: Start your Flask server and run ngrok:
   ```bash
   flask run
   ngrok http 5000
   ```

   ngrok will provide a public URL that you can use for external testing.

## Using the API

Now that your server is running, you can start making requests to the API. Below are examples of how to use each endpoint with `curl`.

### 1. Basic Perplexity Analysis

```bash
curl -X POST http://localhost:5000/analyze/perplexity \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "keyword": "example_keyword"
}'
```

### 2. Content Optimization Analysis

```bash


curl -X POST http://localhost:5000/analyze/content-optimization \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "keyword": "example_keyword"
}'
```

### 3. Technical SEO Audit

```bash
curl -X POST http://localhost:5000/analyze/technical-seo \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com"
}'
```

### 4. Local SEO Enhancement

```bash
curl -X POST http://localhost:5000/analyze/local-seo \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "location": "New York"
}'
```

### 5. Competitor Comparison

```bash
curl -X POST http://localhost:5000/analyze/competitor-comparison \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "competitor_url": "https://competitor.com"
}'
```

### 6. Ecommerce SEO Optimization

```bash
curl -X POST http://localhost:5000/analyze/ecommerce-seo \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "product_name": "Product Name"
}'
```

### 7. Content Gap Analysis

```bash
curl -X POST http://localhost:5000/analyze/content-gap \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "related_keywords": ["keyword1", "keyword2"]
}'
```

### 8. Backlink Strategy

```bash
curl -X POST http://localhost:5000/analyze/backlink-strategy \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com"
}'
```

## Testing

### Test Types

- **Unit Tests**: Test individual functions and services in isolation.
- **API Unit Tests**: Test API routes without actual service integrations.
- **Integration Tests**: Full end-to-end tests that include external services like Perplexity.

### Running Tests

To run tests, use the `run_tests.py` script:

1. **Run Unit Tests**:
   ```bash
   python run_tests.py unit
   ```

2. **Run API Unit Tests**:
   ```bash
   python run_tests.py api-unit
   ```

3. **Run Integration Tests (with ngrok)**:
   ```bash
   python run_tests.py integration
   ```

4. **Run All Tests**:
   ```bash
   python run_tests.py
   ```

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t seo-analysis-api .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 5000:5000 --name seo-analysis-api seo-analysis-api
   ```

## Running with Docker Compose

1. **Create a `docker-compose.yml` file**:
   ```yaml
   version: '3.8'
   services:
     seo-api:
       build: .
       ports:
         - "5000:5000"
       environment:
         - FLASK_ENV=production
         - PERPLEXITY_API_KEY=your_api_key_here
   ```

2. **Run the services**:
   ```bash
   docker-compose up --build
   ```

3. Access the API at `http://localhost:5000`.

## Development Notes

- **No Database**: This MVP does not use a database. It demonstrates communication and prompts between SEO analysis and Perplexity.
- **ngrok for Integration Tests**: Use ngrok for public access to the local API during integration testing.

## TODO - Future Features

1. **Rate Limiting/Throttle**: Add rate limiting to control API usage.
2. **Model Selection**: Allow users to select different models for SEO analysis (e.g., GPT, BERT).
3. **Database Integration**: Extend the project with database integration (local, cloud-based, or even Airtable, Zapier, Excel).
4. **RBAC (Role-Based Access Control)**: Implement RBAC for securing different levels of API access.
5. **Service Provider Independence**: Make the service database-agnostic, supporting multiple backends like Google Cloud, Airtable, or local storage.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
