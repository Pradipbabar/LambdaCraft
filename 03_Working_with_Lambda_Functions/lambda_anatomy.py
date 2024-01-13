# lambda_anatomy.py

def lambda_handler(event, context):
    """
    Lambda function handler.

    Parameters:
    - event: The event data passed to the Lambda function.
    - context: The runtime information provided by AWS Lambda.

    Returns:
    A dictionary containing the response.
    """
    # 1. Event Input
    print("Received event:", event)

    # 2. Lambda Function Logic
    # Add your custom business logic here
    response_message = process_event(event)

    # 3. Context Information
    print("Remaining time (ms):", context.get_remaining_time_in_millis())

    # 4. Return Response
    return {
        'statusCode': 200,
        'body': response_message
    }

def process_event(event):
    """
    Custom function to process the Lambda event.

    Parameters:
    - event: The event data passed to the Lambda function.

    Returns:
    A string containing the processed message.
    """
    # Example: Process the event and generate a response
    processed_message = f"Processed event with ID: {event.get('id')}"
    return processed_message

if __name__ == "__main__":
    # For local testing or execution outside AWS Lambda
    test_event = {'id': '123', 'data': 'example'}
    test_context = None

    result = lambda_handler(test_event, test_context)
    print("Lambda function result:", result)
