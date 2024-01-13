# Configure Environment Variables

## Introduction

Environment variables play a crucial role in configuring and managing settings for your AWS Lambda functions. This document outlines best practices for setting up and managing environment variables securely within your Lambda functions.

## Why Use Environment Variables?

1. **Dynamic Configuration:** Environment variables allow you to dynamically configure aspects of your Lambda function without modifying the code.

2. **Sensitive Information:** Use environment variables to store sensitive information, such as API keys and database credentials, securely.

3. **Version Control:** Separating configuration from code enables better version control. Environment variables can be updated without modifying the codebase.

## Setting Up Environment Variables in Lambda

### 1. AWS Lambda Console

1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Select your Lambda function.
3. Navigate to the "Configuration" tab.
4. In the "Function code" section, find the "Environment variables" section.
5. Add key-value pairs for your environment variables.

### 2. AWS CLI

Use the AWS CLI to update environment variables. Replace `your-function-name` and `key=value` with your actual values.

```bash
aws lambda update-function-configuration --function-name your-function-name --environment Variables={key=value}
