
import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    item_id = "1"
    table.put_item(Item={"id": item_id, "message": "Hello from Lambda + DynamoDB!"})

    item = table.get_item(Key={"id": item_id}).get("Item", {})

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "ok": True,
            "message": "API is working",
            "item": item
        })
    }