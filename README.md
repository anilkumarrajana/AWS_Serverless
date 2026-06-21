# AWS_Serverless
This Repository is to explore and practice serveeless services in AWS Lambda and BOTO3.

## Project 1: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

### Objective: 
  Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.

### Task: Automatically tag any newly launched EC2 instance with the current date and a custom tag.

Instructions:

1. EC2 Setup:
   - Ensure you have the capability to launch EC2 instances.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role.
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice
     4. Print a confirmation message for logging purposes.
4. CloudWatch Events:
   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
   - Attach the Lambda function as the target.
5. Testing:
   - Launch a new EC2 instance.
   - After a short delay, confirm that the instance is automatically tagged as specified.

## Project 2: Automated Instance Management Using AWS Lambda and Boto3

### Objective: 
  In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

### Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:

1. Setup:
   - Create two EC2 instances.
   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
3. Coding:
   - Using Boto3 in the Lambda function:
     - Detect all EC2 instances with the `Auto-Stop` tag and stop them.
     - Detect all EC2 instances with the `Auto-Start` tag and start them.

4. Testing:
   - Manually invoke the Lambda function.
   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.
Instructions:
1. EC2 Setup:
   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).
   - Tag the first instance with a key `Action` and value `Auto-Stop`.
   - Tag the second instance with a key `Action` and value `Auto-Start`.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

## Project 3: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

### Objective: 
  To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

### Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:
1. S3 Setup:
   - Navigate to the S3 dashboard and create a new bucket.
   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.
  
## Project 4: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS

### Objective: 
  Automate the process to receive an alert whenever an item in a DynamoDB table gets updated.

### Task: Set up a Lambda function that gets triggered when an item in a DynamoDB table is updated and sends an alert via SNS.

Instructions:
1. DynamoDB Setup:
   - Navigate to the DynamoDB dashboard and create a table.
   - Add a few items to the table.
2. SNS Setup:
   - Navigate to the SNS dashboard and create a new topic.
   - Subscribe your email to this topic.
3. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach policies that allow Lambda to read DynamoDB Streams and send SNS notifications.
4. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:

## Project 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

### Objective: 
  Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.

### Task: Automatically tag any newly launched EC2 instance with the current date and a custom tag.

Instructions:
1. EC2 Setup:
   - Ensure you have the capability to launch EC2 instances.
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role.
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.

     4. Print a confirmation message for logging purposes.

4. CloudWatch Events:

   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.

   - Attach the Lambda function as the target.

5. Testing:

   - Launch a new EC2 instance.

   - After a short delay, confirm that the instance is automatically tagged as specified.
     1. Extract the modified DynamoDB item from the event.

     2. Send an SNS notification detailing the change.

     3. Log messages for tracking.

5. DynamoDB Stream:

   - Enable DynamoDB Streams on your table and set the view type to "New and old images".

   - Attach the Lambda function to the DynamoDB Stream.

6. Testing:

   - Update an item in your DynamoDB table.

   - Confirm that you receive an SNS alert detailing the change.

Submission:

- Provide the Python code used in the Lambda function.

- Document the steps followed.

- Share screenshots of the SNS alert and Lambda logs.
