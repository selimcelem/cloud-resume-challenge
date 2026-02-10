# Steps 7–10 – Visitor Counter (JS + DynamoDB + API Gateway + Lambda/Python)

## Goal
Add a real-time visitor counter using a serverless backend.

## Challenge mapping
- Step 7: JavaScript (frontend calls API)
- Step 8: Database (DynamoDB stores count)
- Step 9: API (API Gateway + Lambda)
- Step 10: Python (Lambda uses boto3)

## Architecture
Frontend (JavaScript) → API Gateway → AWS Lambda → DynamoDB

## What was implemented

### DynamoDB
- Created table: `visitor-counter`
- Partition key: `id` (String)
- Initial item:
  - id: "main"
  - count: 0

### Lambda Function
- Created function: `visitorCounter`
- Runtime: Python 3.12
- Permissions: access to DynamoDB
- Logic:
  - Increment `count` in DynamoDB on every request
  - Return updated value as JSON

### API Gateway
- HTTP API created
- Route: `GET /visitors`
- Integrated with Lambda function
- CORS enabled for domain:
  - https://selimcelem.com

### Frontend
- Added `script.js` to call the API endpoint
- Display visitor count in footer
- Connected using:

Endpoint:
https://9kj7akjnf2.execute-api.eu-west-1.amazonaws.com/prod/visitors

## Result
The website now displays a working visitor counter that increases on every page load:

https://selimcelem.com

## Notes
- CloudFront invalidation was required after updating JavaScript
- CORS configured to allow requests from the website domain

## Resources (for reference)
- DynamoDB table: `visitor-counter`
- Lambda function: `visitorCounter`
- API route: `GET /visitors`
- API endpoint: https://9kj7akjnf2.execute-api.eu-west-1.amazonaws.com/prod/visitors
- Site: https://selimcelem.com
