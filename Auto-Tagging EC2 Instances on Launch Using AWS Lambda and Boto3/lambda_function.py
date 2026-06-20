import boto3
from datetime import datetime


ec2 = boto3.client('ec2')


def lambda_handler(event, context):
    print("Received event:", event)

    try:
        items = event['detail']['responseElements']['instancesSet']['items']
        instance_ids = [item['instanceId'] for item in items]

        current_date = datetime.utcnow().strftime('%Y-%m-%d')

        ec2.create_tags(
            Resources=instance_ids,
            Tags=[
                {'Key': 'LaunchDate', 'Value': current_date},
                {'Key': 'AutoTagged', 'Value': 'Yes'}
            ]
        )

        message = f"Successfully tagged instances: {instance_ids}"
        print(message)
        return {
            'statusCode': 200,
            'body': message
        }

    except KeyError as e:
        error_message = f"Expected key not found in event: {str(e)}"
        print(error_message)
        return {
            'statusCode': 400,
            'body': error_message
        }

    except Exception as e:
        error_message = f"Error tagging instance: {str(e)}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': error_message
        }