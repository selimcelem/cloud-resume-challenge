# Step 13 – Source Control

## Goal
Move backend infrastructure and application code into source control to enable version tracking and automated deployment.

## What was implemented
- Created a GitHub repository:
  - selimcelem/cloud-resume-challenge
- Committed:
  - Backend Python code
  - Terraform infrastructure code
  - Tests (pytest)
  - Documentation (docs/steps)
- Added .gitignore rules to exclude:
  - .venv/
  - .terraform/
  - terraform.tfstate*
  - .pytest_cache/
  - .vs/
  - Build artifacts

## Branch Strategy
- main branch is the deployment branch
- Infrastructure and backend changes are tracked through Git
- No manual AWS Console changes for Terraform-managed resources

## Result
- Full version control of backend infrastructure and application code
- Traceable commit history for all changes
- Foundation for CI/CD automation
- Manual deployments from local machine are no longer required

## Next Step
Set up CI/CD pipeline for automated backend testing and deployment.
