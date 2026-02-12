# Step 12 – Infrastructure as Code with Terraform

## Goal
Replace all manually created backend infrastructure with Terraform-managed resources.

## What was implemented

The following resources are now fully managed through Terraform:

### DynamoDB
- Table: visitor-counter
- Partition key: id (String)
- PAY_PER_REQUEST billing mode

### Lambda
- Function: visitorCounter
- Runtime: Python 3.12
- Environment variable:
  - TABLE_NAME = visitor-counter
- IAM role and policies created via Terraform

### API Gateway
- HTTP API with route:
  - GET /visitors
- CORS enabled for:
  - https://selimcelem.com
  - https://www.selimcelem.com
- Automatic deployment stage: prod

### Permissions
- IAM policies for DynamoDB access
- Lambda execution role
- API Gateway invoke permission for Lambda

## Workflow

Commands used:

terraform init
terraform plan
terraform apply

## Result

- Backend infrastructure is now fully reproducible via code
- No manual configuration needed in AWS Console
- Frontend now calls Terraform-managed API endpoint

Current API endpoint:

https://5jryt6hshh.execute-api.eu-west-1.amazonaws.com/prod/visitors


## Verification

terraform plan

Output: “No changes. Infrastructure matches configuration.”

## Drift Prevention Refactor

After completing the Terraform migration, the Lambda deployment source was aligned with the tested backend code to eliminate deployment/test drift.

Originally:

- Terraform deployed from `infrastructure/terraform/lambda_src/`
- Pytest validated code in `backend/visitor_counter/`

This created a risk where tests could pass while different code was being deployed.

To resolve this:

- Lambda source was moved to `backend/visitor_counter/src/`
- Terraform `archive_file.source_dir` was updated to `../../backend/visitor_counter/src`
- The deprecated `lambda_src/` directory was removed
- Tests were updated to import from the new module path

Result:

- Single source of truth for Lambda code
- Tested code equals deployed code
- CI/CD (Step 13) will validate the actual production artifact

## Next Step

Set up CI/CD pipelines for automated deployment.
