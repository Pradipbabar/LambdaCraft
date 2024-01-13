import boto3

def process_s3_event(event, context):
    """
    Lambda function handler for processing S3 events.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.
    """
    print("Processing S3 Event:", event)

    # Your custom logic for processing S3 events goes here.
    # For example, you can download the file, perform transformations, and upload the result.

def process_api_gateway_request(event, context):
    """
    Lambda function handler for processing API Gateway requests.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.
    """
    print("Processing API Gateway Request:", event)

    # Your custom logic for handling API Gateway requests goes here.
    # For example, you can validate input, perform business logic, and return a response.

def process_dynamodb_stream(event, context):
    """
    Lambda function handler for processing DynamoDB stream events.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.
    """
    print("Processing DynamoDB Stream Event:", event)

    # Your custom logic for handling DynamoDB stream events goes here.
    # For example, you can update related records, trigger additional processes, etc.

def invoke_another_lambda(event, context):
    """
    Lambda function handler for invoking another Lambda function.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.
    """
    print("Invoking Another Lambda Function:", event)

    # Your custom logic for invoking another Lambda function goes here.
    # For example, you can pass data to another Lambda function for further processing.

# Additional functions can be added to demonstrate various scenarios.

# Uncomment the following lines to test the functions locally.
# process_s3_event({"bucket": "example-bucket", "key": "example-file.txt"}, None)
# process_api_gateway_request({"httpMethod": "GET", "queryStringParameters": {"param1": "value1"}}, None)
# process_dynamodb_stream({"Records": [{"eventName": "INSERT"}]}, None)
# invoke_another_lambda({"data": "example_data"}, None)
