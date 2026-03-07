<img width="1827" height="1064" alt="mermaid-diagram-2026-02-10-151131" src="https://github.com/user-attachments/assets/dbdd59fc-e0c8-4d08-acfc-806f832dde60" />

# AWS Serverless API with Terraform

Production-style serverless API deployed with Terraform using AWS Lambda, API Gateway (HTTP API), DynamoDB, and IAM.

## Architecture

```mermaid
flowchart LR
    Client[Client / Browser] -->|GET /| APIGW[API Gateway HTTP API]
    APIGW --> Lambda[Lambda Function]
    Lambda --> DDB[DynamoDB Table]
    Lambda --> Logs[CloudWatch Logs]
