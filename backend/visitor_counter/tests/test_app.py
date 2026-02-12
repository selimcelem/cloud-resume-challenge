import json
import os

import boto3
import pytest
from moto import mock_aws


@pytest.fixture
def aws_region():
    # moto needs a region set
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
    return "eu-west-1"


@mock_aws
def test_lambda_increments_counter(aws_region):
    # Create DynamoDB table + seed item
    dynamodb = boto3.resource("dynamodb", region_name=aws_region)
    table = dynamodb.create_table(
        TableName="visitor-counter",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    table.wait_until_exists()

    table.put_item(Item={"id": "main", "count": 0})

    # Import AFTER mock/table setup (because app.py creates boto3 resources at import time)
    os.environ["TABLE_NAME"] = "visitor-counter"
    from backend.visitor_counter.src.app import lambda_handler

    r1 = lambda_handler({}, None)
    body1 = json.loads(r1["body"])
    assert r1["statusCode"] == 200
    assert body1["count"] == 1

    r2 = lambda_handler({}, None)
    body2 = json.loads(r2["body"])
    assert body2["count"] == 2
