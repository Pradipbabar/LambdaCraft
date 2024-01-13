#!/bin/bash

# AWS CLI Deployment Script
# Deploy a Lambda function using the AWS Command Line Interface (CLI)

# Define variables
LAMBDA_FUNCTION_NAME="your_lambda_function_name"
ZIP_FILE_PATH="path/to/your/lambda_function_code.zip"
HANDLER_FUNCTION="your_lambda_function_handler"
RUNTIME="python3.8"
ROLE_ARN="arn:aws:iam::your-account-id:role/your-iam-role"

# Create a deployment package (ZIP file) from the Lambda function code
zip -r $ZIP_FILE_PATH your_lambda_function_code/*

# Deploy the Lambda function using AWS CLI
aws lambda create-function \
    --function-name $LAMBDA_FUNCTION_NAME \
    --runtime $RUNTIME \
    --role $ROLE_ARN \
    --handler $HANDLER_FUNCTION \
    --zip-file fileb://$ZIP_FILE_PATH \
    --region your-preferred-region

# Clean up: Remove the deployment package after deployment
rm $ZIP_FILE_PATH

echo "Lambda function deployed successfully!"
