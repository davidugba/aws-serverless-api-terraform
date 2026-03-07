
# AWS Serverless API with Terraform

Production-style serverless API deployed with Terraform using AWS Lambda, API Gateway (HTTP API), DynamoDB, and IAM.

## Architecture

```mermaid
flowchart LR
    Client[Client / Browser] -->|GET /| APIGW[API Gateway HTTP API]
    APIGW --> Lambda[Lambda Function]
    Lambda --> DDB[DynamoDB Table]
    Lambda --> Logs[CloudWatch Logs]