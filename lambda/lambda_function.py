import json


def lambda_function(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello updated Lambda from cursor!')
    }
# test trigger
