# Integration of Lambda Functions with API Gateway

Learn how to seamlessly integrate AWS Lambda functions with API Gateway for building scalable and secure APIs. This guide, outlined in the "api_gateway_integration.md" file, explores the configuration and deployment of Lambda-backed APIs, enabling you to create robust serverless applications.

## Why API Gateway Integration?

API Gateway serves as a central component for creating, deploying, and managing APIs at scale. Integrating Lambda functions with API Gateway allows you to expose serverless functions as HTTP endpoints, facilitating communication with clients, web applications, or other services.

## Configuring Lambda-backed APIs with API Gateway:

1. **Create a New API:**
   - In the API Gateway console, create a new API to serve as the entry point for your serverless functions.

2. **Create a Resource and Method:**
   - Define a resource and associated HTTP methods (e.g., GET, POST) for your API.
   - Configure the integration type to "Lambda Function" for the chosen method.

3. **Select Lambda Function:**
   - Associate the API Gateway method with the desired Lambda function.
   - Configure the mapping of input and output data between API Gateway and Lambda.

4. **Method Request and Integration Request:**
   - Define the method request to handle parameters in the request URL or headers.
   - Configure the integration request to transform and forward data to the Lambda function.

5. **Set Up CORS (Optional):**
   - If your API is accessed from a web browser, configure Cross-Origin Resource Sharing (CORS) settings to allow or restrict cross-origin requests.

6. **Deploy the API:**
   - Deploy the API to a stage, creating a publicly accessible endpoint.
   - API Gateway automatically manages the deployment of your Lambda-backed API.

## Lambda Function Code:

Here's a basic example of a Python Lambda function code that can be integrated with API Gateway:

```python
def lambda_handler(event, context):
    # Process the incoming event data from API Gateway
    name = event['queryStringParameters']['name']
    
    # Return a response
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
