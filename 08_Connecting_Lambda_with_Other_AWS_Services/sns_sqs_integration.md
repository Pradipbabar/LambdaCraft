# Integrating Lambda Functions with Amazon SNS and SQS

Discover how to seamlessly integrate AWS Lambda functions with Amazon Simple Notification Service (SNS) and Simple Queue Service (SQS) for handling notifications and managing message queues effectively. This guide, outlined in the "sns_sqs_integration.md" file, will walk you through setting up event sources, processing notifications, and managing message queues in a serverless architecture.

## Why SNS and SQS Integration?

Integrating Lambda functions with Amazon SNS and SQS enables you to build scalable and decoupled systems. SNS allows you to send messages to multiple subscribers, while SQS serves as a reliable message queue for asynchronous processing, ensuring that messages are not lost even if a subscriber is temporarily unavailable.

## Setting Up SNS and SQS Integration:

1. **Create an SNS Topic:**
   - In the AWS SNS console, create a new topic that will serve as the source for notifications.

2. **Subscribe Lambda Function to SNS Topic:**
   - Subscribe your Lambda function to the SNS topic to receive notifications.
   - Configure the Lambda function to handle the SNS message payload.

3. **Create an SQS Queue:**
   - In the AWS SQS console, create a new queue that will serve as a message buffer for your Lambda function.

4. **Subscribe SQS Queue to SNS Topic:**
   - Subscribe the SQS queue to the SNS topic to receive notifications.
   - Configure the SQS queue as the endpoint for SNS messages.

5. **Configure Lambda Function for SQS Trigger:**
   - Set up an SQS trigger for your Lambda function, specifying the SQS queue as the event source.
   - Adjust batch size and visibility timeout based on your processing requirements.

6. **Testing:**
   - Test the integration by publishing a message to the SNS topic.
   - Monitor the SQS queue and Lambda function logs to observe the message processing flow.

## Lambda Function Code:

Here's a simple example of a Python Lambda function code that processes SNS messages from an SQS queue:

```python
import json

def lambda_handler(event, context):
    for record in event['Records']:
        # Process the incoming SNS message
        sns_message = json.loads(record['body'])
        print(f"Received SNS message: {sns_message}")
        
        # Add your custom processing logic here
