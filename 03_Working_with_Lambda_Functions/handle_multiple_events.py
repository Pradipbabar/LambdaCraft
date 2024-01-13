# handle_multiple_events.py

def lambda_handler(event, context):
    """
    Lambda function handler for handling multiple types of events.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.

    Returns:
    A dictionary containing the response.
    """
    # Determine the event type and call the corresponding handler
    if 'Records' in event and 's3' in event['Records'][0]:
        return handle_s3_event(event)
    elif 'httpMethod' in event and 'resource' in event:
        return handle_api_gateway_event(event)
    else:
        return {
            'statusCode': 400,
            'body': 'Unsupported event type'
        }

def handle_s3_event(event):
    """
    Handler for S3 events.

    Parameters:
    - event: The S3 event data.

    Returns:
    A dictionary containing the S3 event response.
    """
    # Extract relevant information from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Add your custom S3 event handling logic here
    response_message = f"S3 event triggered. Bucket: {bucket_name}, Object: {object_key}"

    return {
        'statusCode': 200,
        'body': response_message
    }

def handle_api_gateway_event(event):
    """
    Handler for API Gateway events.

    Parameters:
    - event: The API Gateway event data.

    Returns:
    A dictionary containing the API Gateway event response.
    """
    # Extract relevant information from the API Gateway event
    http_method = event['httpMethod']
    resource_path = event['resource']

    # Add your custom API Gateway event handling logic here
    response_message = f"API Gateway event triggered. Method: {http_method}, Resource: {resource_path}"

    return {
        'statusCode': 200,
        'body': response_message
    }

if __name__ == "__main__":
    # For local testing or execution outside AWS Lambda
    test_s3_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "test-bucket"},
                    "object": {"key": "test-object.txt"}
                }
            }
        ]
    }

    test_api_gateway_event = {
        "httpMethod": "GET",
        "resource": "/test-resource"
    }

    test_context = None

    s3_result = lambda_handler(test_s3_event, test_context)
    api_gateway_result = lambda_handler(test_api_gateway_event, test_context)

    print("S3 Event Result:", s3_result)
    print("API Gateway Event Result:", api_gateway_result)
