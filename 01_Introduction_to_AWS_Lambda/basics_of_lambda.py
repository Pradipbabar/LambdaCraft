def lambda_handler(event, context):
    """
    Lambda function handler.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.

    Returns:
    A dictionary with a simple response.
    """
    print("Received event:", event)

    # Your custom logic can be added here.
    response = {
        "statusCode": 200,
        "body": "Hello from LambdaCraft: Pythonic Serverless Odyssey!",
    }

    return response
