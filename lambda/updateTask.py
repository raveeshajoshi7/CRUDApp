import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    
    table.update_item(
        Key={'taskId': task_id},
        UpdateExpression='SET #t = :t, #s = :s',
        ExpressionAttributeNames={
            '#t': 'task',
            '#s': 'status'
        },
        ExpressionAttributeValues={
            ':t': body['task'],
            ':s': body['status']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Task updated')
    }