import os
import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")

ec2 = boto3.client("ec2", region_name=REGION)

def get_instances_by_tag(tag_key, tag_value, state=None):
    filters = [
        {"Name": f"tag:{tag_key}", "Values": [tag_value]},
    ]
    if state:
        filters.append({"Name": "instance-state-name", "Values": [state]})

    response = ec2.describe_instances(Filters=filters)
    instances = []
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            name = next(
                (tag["Value"] for tag in instance.get("Tags", []) if tag["Key"] == "Name"),
                instance["InstanceId"],
            )
            instances.append({"InstanceId": instance["InstanceId"], "Name": name})
    return instances

def start_tagged_instances():
    instances = get_instances_by_tag("Action", "Auto-Start", state="stopped")
    if not instances:
        print("No stopped instances found with tag Action=Auto-Start")
        return []

    instance_ids = [instance["InstanceId"] for instance in instances]
    print("Starting instances:", instance_ids)
    ec2.start_instances(InstanceIds=instance_ids)
    print("Start request sent.")
    return instances

def stop_tagged_instances():
    instances = get_instances_by_tag("Action", "Auto-Stop", state="running")
    if not instances:
        print("No running instances found with tag Action=Auto-Stop")
        return []

    instance_ids = [instance["InstanceId"] for instance in instances]
    print("Stopping instances:", instance_ids)
    ec2.stop_instances(InstanceIds=instance_ids)
    print("Stop request sent.")
    return instances

def lambda_handler(event, context):
    action = event.get("action", "both")
    result = {"status": "done", "action": action}

    if action == "start":
        started = start_tagged_instances()
        result["started_instances"] = [instance["Name"] for instance in started]
    elif action == "stop":
        stopped = stop_tagged_instances()
        result["stopped_instances"] = [instance["Name"] for instance in stopped]
    else:
        stopped = stop_tagged_instances()
        started = start_tagged_instances()
        result["stopped_instances"] = [instance["Name"] for instance in stopped]
        result["started_instances"] = [instance["Name"] for instance in started]

    return result