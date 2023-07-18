import boto3

import json
from uuid import uuid4


def get_db_table():
    dynamodb_resource = boto3.resource("dynamodb")

    return dynamodb_resource.Table("academia")


def handler(event, context):
    ddb_table = get_db_table()

    print(event['body'])

    inventory_id = str(uuid4())

    response = ddb_table.put_item(
        Item={
            "PK": inventory_id,
            "name": "",
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
