# Cloud Resume Challenge (AWS)

This repository documents my implementation of the Cloud Resume Challenge on AWS.

## Goal
Build and deploy a cloud-hosted resume website with a visitor counter, infrastructure as code, and CI/CD.

## Architecture (high level)
- Static website: Amazon S3 + Amazon CloudFront
- DNS + TLS: Route 53 + ACM
- Visitor counter backend: API Gateway + AWS Lambda
- Database: DynamoDB
- Infrastructure as Code: Terraform (remote state + DynamoDB locking)
- CI/CD: GitHub Actions

## Related Repository

The frontend (static website hosted on S3 + CloudFront) lives in a separate repository:

https://github.com/selimcelem/cloud-resume-frontend

The frontend consumes the API Gateway endpoint defined in this repository to retrieve and increment the visitor counter.

## Repo structure
| Folder | Purpose |
|--------|---------|
| [backend](./backend) | AWS Lambda + API logic |
| [infrastructure](./infrastructure) | Terraform infrastructure definitions |
| [docs](./docs) | Step-by-step challenge documentation |

## Progress log (Cloud Resume Challenge – AWS)
- [x] 1. Certification (CLF-C02)
- [x] 2. HTML
- [x] 3. CSS
- [x] 4. Static Website (S3)
- [x] 5. HTTPS (CloudFront)
- [x] 6. DNS (Custom domain)
- [x] 7. JavaScript (visitor counter UI)
- [x] 8. Database (DynamoDB)
- [x] 9. API (API Gateway + Lambda)
- [x] 10. Python (boto3 in Lambda)
- [x] 11. Tests
- [x] 12. Infrastructure as Code (SAM or Terraform)
- [x] 13. Source Control (backend repo separation)
- [x] 14. CI/CD (Back end)
- [x] 15. CI/CD (Front end)


## Links
- Live site: https://selimcelem.com
- Challenge: https://cloudresumechallenge.dev/
- Frontend repo: https://github.com/selimcelem/cloud-resume-frontend

