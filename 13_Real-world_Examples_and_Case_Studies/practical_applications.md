
# Building Practical Applications with AWS Lambda

Discover hands-on examples of building practical applications with AWS Lambda. This guide, outlined in the "practical_applications.md" file, provides guidance on applying your serverless skills to real-world scenarios, ranging from web applications to data processing pipelines.

## Introduction:

AWS Lambda offers a versatile platform for building serverless applications, enabling developers to focus on writing code without managing servers. This guide explores practical applications that showcase the flexibility and power of AWS Lambda in various scenarios.

## 1. Web Application Backend:

### Scenario:
Build the backend for a web application using AWS Lambda, API Gateway, and DynamoDB.

### Steps:
1. Create Lambda functions for CRUD operations.
2. Set up an API Gateway to expose endpoints.
3. Use DynamoDB to store and retrieve data.

### Example Code:
```python
# Sample Lambda function for creating a resource in DynamoDB
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    response = table.put_item(Item=body)

    return {
        'statusCode': 200,
        'body': json.dumps('Resource created successfully!')
    }
```

## 2. Real-time Data Processing:

### Scenario:
Process real-time streaming data using AWS Lambda and Kinesis Data Streams.

### Steps:
1. Set up a Kinesis Data Stream to ingest data.
2. Create a Lambda function to process incoming data.
3. Configure the Lambda function to consume events from the Kinesis stream.

### Example Code:
```python
# Sample Lambda function for processing Kinesis Data Stream events
import json

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'])
        # Process the data as needed
        print(payload)

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully!')
    }
```

## 3. Image Processing Pipeline:

### Scenario:
Build an image processing pipeline using AWS Lambda and Amazon S3.

### Steps:
1. Configure an S3 bucket to trigger Lambda functions upon image uploads.
2. Create Lambda functions to resize or modify images.
3. Store processed images back in S3 or another storage solution.

### Example Code:
```python
# Sample Lambda function for resizing images on S3 upload
import json
import boto3
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Download the image
        image = Image.open('/tmp/input.jpg')

        # Resize the image
        resized_image = image.resize((300, 300))

        # Save the resized image
        resized_image.save('/tmp/output.jpg')

        # Upload the resized image back to S3
        s3.upload_file('/tmp/output.jpg', bucket, 'resized/' + key)

    return {
        'statusCode': 200,
        'body': json.dumps('Image processing complete!')
    }
```

## Conclusion:

These hands-on examples demonstrate the versatility of AWS Lambda in building practical applications across different domains. Whether you're developing web backends, processing real-time data, or creating image processing pipelines, AWS Lambda provides a scalable and cost-effective serverless solution.
