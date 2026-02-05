# Step 6 – Custom Domain (Namecheap + ACM + CloudFront)

## Goal
Serve the resume website on a personal domain over HTTPS.

## What I did
- Purchased domain: selimcelem.com via Namecheap
- Requested ACM certificate in us-east-1 for:
  - selimcelem.com
  - www.selimcelem.com
- Added ACM DNS validation CNAME records in Namecheap
- Configured DNS records to point to CloudFront:
  - @   → dsnxfcve3qr2l.cloudfront.net
  - www → dsnxfcve3qr2l.cloudfront.net
- Attached the ACM certificate to the CloudFront distribution
- Added alternate domain names in CloudFront

## Result
Website is now accessible at:
https://selimcelem.com
