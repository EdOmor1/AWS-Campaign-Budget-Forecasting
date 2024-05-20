# AWS-Campaign-Budget-Forecasting

## Overview
This project implements a forecasting tool to predict future campaign budget needs based on historical data using AWS services.

## Architecture
![Architecture Diagram](diagrams/architecture_diagram.png)

## AWS Services Used
- Amazon Forecast
- AWS Lambda
- Amazon S3
- Amazon DynamoDB

## Features
- Automated budget forecasting using machine learning models.
- Integration with historical data stored in Amazon S3.
- Scalable and cost-effective forecasting solution.

## Prerequisites
- AWS account
- Historical campaign data in CSV format

## Setup

### Step 1: Deploy Infrastructure
1. Deploy the CloudFormation stack using `infrastructure/cloudformation_template.yaml`.

### Step 2: Configure Lambda Functions
1. Update `src/forecast_model.py` with any necessary configurations.
2. Deploy the Lambda functions using the AWS Lambda console or AWS CLI.

## Usage
1. Upload historical campaign data to the designated S3 bucket.
2. The Lambda function `forecast_model.py` processes the data and generates budget forecasts.

