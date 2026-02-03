# Cloud Resume Challenge (AWS)

This repository documents my implementation of the Cloud Resume Challenge on AWS.

## Goal
Build and deploy a cloud-hosted resume website with a visitor counter, infrastructure as code, and CI/CD.

## Architecture (high level)
- Static website: Amazon S3 + Amazon CloudFront
- DNS + TLS: Route 53 + ACM
- Visitor counter backend: API Gateway + AWS Lambda
- Database: DynamoDB
- Infrastructure as Code: (Terraform or CloudFormation)
- CI/CD: GitHub Actions

## Repo structure (planned)
- `frontend/` - HTML/CSS/JS resume site
- `backend/` - Lambda + API logic
- `infrastructure/` - IaC (Terraform/CloudFormation) + diagrams
- `docs/` - notes, decisions, troubleshooting, screenshots

## Progress log
- [ ] Step 1: Repo created + README scaffold
- [ ] Step 2: Frontend resume page (local)
- [ ] Step 3: S3 static hosting
- [ ] Step 4: CloudFront + HTTPS (ACM)
- [ ] Step 5: Route 53 custom domain
- [ ] Step 6: DynamoDB table + Lambda counter
- [ ] Step 7: API Gateway integration
- [ ] Step 8: CI/CD pipeline (GitHub Actions)
- [ ] Step 9: IaC implementation
- [ ] Step 10: Tests + polish

## Links
- Live site: (coming soon)
- Challenge: https://cloudresumechallenge.dev/
