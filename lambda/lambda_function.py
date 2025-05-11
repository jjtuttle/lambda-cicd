import json


def lambda_function(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from our CICD github actions workflow in Cursor!!!')
    }
