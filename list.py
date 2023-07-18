import boto3

import json


def get_db_table():
    dynamodb_resource = boto3.resource("dynamodb")

    return dynamodb_resource.Table("academia")


def handler(event, context):
    ddb_table = get_db_table()

    response = ddb_table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
