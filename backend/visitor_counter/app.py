import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("visitor-counter")

def lambda_handler(event, context):
    resp = table.update_item(
        Key={"id": "main"},
        UpdateExpression="SET #c = if_not_exists(#c, :zero) + :inc",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":inc": 1, ":zero": 0},
        ReturnValues="UPDATED_NEW",
    )

    count = int(resp["Attributes"]["count"])

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"count": count}),
    }
