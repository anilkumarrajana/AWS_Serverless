import json
import boto3
from boto3.dynamodb.types import TypeDeserializer

sns = boto3.client('sns')
deserializer = TypeDeserializer()

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:996904209371:DynamoDBUpdateAlerts'


def deserialize_dynamodb_item(dynamo_item):
    return {k: deserializer.deserialize(v) for k, v in dynamo_item.items()}


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    for record in event.get('Records', []):
        event_name = record.get('eventName')

        if event_name != 'MODIFY':
            print(f"Skipping event type: {event_name}")
            continue

        dynamodb_data = record.get('dynamodb', {})
        keys = deserialize_dynamodb_item(dynamodb_data.get('Keys', {}))
        old_image = deserialize_dynamodb_item(dynamodb_data.get('OldImage', {}))
        new_image = deserialize_dynamodb_item(dynamodb_data.get('NewImage', {}))

        message = {
            'alert': 'DynamoDB item updated',
            'tableKeys': keys,
            'oldImage': old_image,
            'newImage': new_image
        }

        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='DynamoDB Item Update Alert',
            Message=json.dumps(message, indent=2, default=str)
        )

        print(f"SNS notification sent for item {keys}")
        print(f"SNS MessageId: {response['MessageId']}")

    return {
        'statusCode': 200,
        'body': 'Processed DynamoDB stream records successfully.'
    }