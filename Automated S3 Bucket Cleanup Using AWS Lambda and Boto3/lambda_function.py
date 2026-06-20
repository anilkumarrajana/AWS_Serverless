import boto3
from datetime import datetime, timezone, timedelta

# Configuration
BUCKET_NAME = "anil-s3-cleanup-demo"  # change to your bucket
DAYS_THRESHOLD = 30

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    now = datetime.now(timezone.utc)
    #cutoff_date = now - timedelta(days=DAYS_THRESHOLD)
    cutoff_date = now - timedelta(minutes=15) #For testing purpose

    deleted_objects = []

    paginator = s3_client.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(Bucket=BUCKET_NAME)

    for page in page_iterator:
        # If bucket is empty, 'Contents' may be missing
        if "Contents" not in page:
            continue

        for obj in page["Contents"]:
            key = obj["Key"]
            last_modified = obj["LastModified"]

            if last_modified < cutoff_date:
                # delete the object
                s3_client.delete_object(Bucket=BUCKET_NAME, Key=key)
                deleted_objects.append(key)

    if deleted_objects:
        print("Deleted objects:")
        for key in deleted_objects:
            print(f"- {key}")
    else:
        print("No objects older than threshold found.")

    return {
        "statusCode": 200,
        "body": f"Deleted {len(deleted_objects)} objects older than {DAYS_THRESHOLD} days."
    }