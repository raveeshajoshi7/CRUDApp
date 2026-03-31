🚀 Serverless CRUD API using AWS
📌 Overview

This project is a serverless CRUD (Create, Read, Update, Delete) API built using AWS services. It demonstrates how to build and deploy RESTful APIs using AWS Lambda, API Gateway, and DynamoDB.

🛠️ Tech Stack
AWS Lambda (Backend logic)
Amazon API Gateway (API routing)
Amazon DynamoDB (Database)
Python (Lambda runtime)
Postman (API testing)

📂 Features
Create a task (POST)
Retrieve all tasks (GET)
Retrieve a single task by ID (GET)
Update a task (PUT)
Delete a task (DELETE)

🏗️ Architecture
API Gateway handles incoming HTTP requests
Requests are routed to AWS Lambda
Lambda performs CRUD operations
DynamoDB stores the data
Responses are returned via API Gateway
🔗 API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Get all tasks
GET	/tasks/{id}	Get a task by ID
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task

📥 Sample Request (POST)
POST /tasks
Content-Type: application/json

{
  "name": "My Task"
}
🔄 Sample Update Request (PUT)
PUT /tasks/{id}
Content-Type: application/json

{
  "name": "Updated Task"
}
⚙️ Setup Instructions
1. Create DynamoDB Table
Table name: Tasks
Primary key: id (String)
2. Create Lambda Function
Runtime: Python
Add necessary IAM permissions for DynamoDB access
3. Configure API Gateway
Create routes:
/tasks
/tasks/{id}
Integrate with Lambda
Enable Lambda proxy integration
4. Deploy API
Deploy to a stage (e.g., dev)
Copy the invoke URL
🧪 Testing

Use Postman or curl to test endpoints:

curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/dev/tasks

🚧 Known Issues / Limitations
PUT endpoint required additional API Gateway path parameter configuration during development
Basic error handling can be improved
No authentication implemented

📌 Future Improvements
Add authentication (Cognito / JWT)
Add input validation
Improve error handling and logging
Add CI/CD pipeline
Enhance monitoring with CloudWatch dashboards

👨‍💻 Author
Built as a learning project to understand AWS serverless architecture and REST API development.
