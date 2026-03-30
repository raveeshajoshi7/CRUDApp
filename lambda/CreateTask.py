import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    task_id = str(uuid.uuid4())
    
    item = {
        'taskId': task_id,
        'task': body['task'],
        'status': 'pending'
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task created', 'taskId': task_id})
    }