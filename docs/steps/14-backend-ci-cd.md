# Step 14 – CI/CD (Back end)

## Goal
Automatically test and deploy backend changes using GitHub Actions, without storing AWS credentials in GitHub.

## What was implemented
- Added a GitHub Actions workflow:
  - .github/workflows/backend.yml
- Workflow triggers:
  - pull_request (runs tests + terraform plan)
  - push to main (runs tests + terraform apply)
- Python tests are executed before any deployment:
  - pytest backend/visitor_counter/tests
- Deployment is blocked if tests fail.
- AWS authentication uses GitHub OIDC:
  - No long-lived AWS access keys stored in GitHub
  - GitHub assumes an IAM role in AWS at runtime

## AWS Configuration
- Created GitHub OIDC provider:
  - token.actions.githubusercontent.com
- Created IAM role:
  - github-actions-terraform
- Trust policy restricted to:
  - repo: selimcelem/cloud-resume-challenge
  - branch: main
- Permissions allow Terraform to manage:
  - Lambda, API Gateway, DynamoDB, IAM, CloudWatch
  - S3 backend state + DynamoDB lock table

## Result
- Backend changes are automatically tested on every PR and push.
- Infrastructure is automatically deployed on push to main (only if tests pass).
- Terraform uses remote state (S3) with locking (DynamoDB).
- No manual deployment from local machine required.

## Next Step
Set up CI/CD pipeline for the front end to automatically deploy the website to S3 and invalidate CloudFront cache.
