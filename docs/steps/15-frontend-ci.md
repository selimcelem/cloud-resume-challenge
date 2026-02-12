# Step 15 – CI/CD (Frontend)

## Goal

Automate deployment of the static website to Amazon S3 and invalidate the CloudFront cache on every push to the main branch, using GitHub Actions with secure OIDC authentication (no stored AWS credentials).

## What was implemented

The frontend was moved to a separate GitHub repository:

- Repository: cloud-resume-frontend
- Static assets: index.html, style.css, script.js
- No AWS credentials stored in source control

### GitHub Actions Workflow

File:
.github/workflows/deploy.yml

The workflow triggers on push to main and performs:

1. OIDC authentication to AWS
2. Sync static files to S3 bucket
3. Invalidate CloudFront cache

Workflow configuration:

- Uses aws-actions/configure-aws-credentials
- Assumes IAM role via OIDC
- Region defined via repository variable
- No long-lived access keys used

### IAM Configuration

A dedicated IAM role was created:

- Role: github-actions-frontend
- Trust policy: allows GitHub OIDC provider
- Restricted to:
  - s3:ListBucket
  - s3:GetObject
  - s3:PutObject
  - s3:DeleteObject
  - cloudfront:CreateInvalidation

S3 bucket:
selimcelem-cloud-resume

CloudFront distribution:
E1PFP6NWS5J5PW

### Repository Variables (GitHub)

Configured under:
Settings → Secrets and Variables → Actions → Variables

- AWS_ROLE_ARN
- AWS_REGION
- S3_BUCKET
- CLOUDFRONT_DISTRIBUTION_ID

Important:
No AWS credentials were committed to source control. Authentication is handled via GitHub OIDC.

## Result

On every push to main:

- Static files are deployed to S3
- CloudFront cache is invalidated
- Website updates automatically
- Deployment is fully automated and secure

Frontend CI/CD is now production-grade and challenge-compliant.
