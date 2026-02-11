# Step 11 – Tests (Python Unit Tests)

## Goal
Add automated tests for the Lambda function to ensure it works correctly without manually clicking in AWS.

## What was implemented

- Created a local Python testing setup using:
  - pytest
  - moto (to mock AWS services like DynamoDB)

- Structured backend code as an importable package:
  - Added `__init__.py` files
  - Created a proper folder structure for Lambda code and tests

## Test logic

The test verifies that:

- The Lambda function can increment the visitor counter
- DynamoDB interactions work as expected
- The response contains the correct incremented value

Example test:

- Start counter at 0  
- Invoke lambda  
- Expect response count to be 1  

## How to run tests locally

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
pip install -r backend/visitor_counter/requirements-dev.txt
pytest
