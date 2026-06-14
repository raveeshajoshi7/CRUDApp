# AWS Serverless Task API

## Overview

This project is a serverless REST API built using AWS services to understand cloud-native application development. The project uses Amazon API Gateway, AWS Lambda, and DynamoDB to perform task management operations.

The primary objective was to gain hands-on experience with serverless architecture, API integration, IAM permissions, and DynamoDB operations.

---

## Technologies Used

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB
* AWS IAM
* Amazon CloudWatch
* Python
* Postman

---

## Architecture

1. API Gateway receives HTTP requests.
2. Requests are routed to AWS Lambda functions.
3. Lambda functions interact with DynamoDB.
4. DynamoDB stores task information.
5. Responses are returned through API Gateway.

---

## Features

### Implemented

* Create new tasks using POST requests
* Update existing tasks using PUT requests
* DynamoDB data storage
* API Gateway and Lambda integration
* CloudWatch logging and monitoring

### Learning & Troubleshooting

* GET and DELETE operations were partially implemented during development.
* The project provided hands-on experience troubleshooting API Gateway routing, Lambda execution, IAM permissions, and DynamoDB integration.

---

## API Endpoints

| Method | Endpoint    | Status                  |
| ------ | ----------- | ----------------------- |
| POST   | /tasks      | Working                 |
| PUT    | /tasks/{id} | Working                 |
| GET    | /tasks      | Learning Implementation |
| GET    | /tasks/{id} | Learning Implementation |
| DELETE | /tasks/{id} | Learning Implementation |

---

## Sample Request

### Create Task

```json
{
  "name": "My Task"
}
```

### Update Task

```json
{
  "name": "Updated Task"
}
```

---

## What I Learned

* Building serverless applications on AWS
* Creating and configuring Lambda functions
* Working with DynamoDB tables
* Configuring API Gateway routes
* Managing IAM permissions
* Troubleshooting cloud service integrations
* Monitoring applications using CloudWatch

---

## Future Improvements

* Complete GET and DELETE functionality
* Add input validation
* Implement authentication using Amazon Cognito
* Improve error handling
* Create CI/CD pipeline using Jenkins and GitHub Actions
* Add CloudWatch dashboards and alerts

---

## Author

Raveesha Joshi

This project was developed as part of my AWS cloud learning journey to gain practical experience with serverless architecture, cloud infrastructure, and troubleshooting AWS services.
