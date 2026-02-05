# Step 5 – HTTPS with CloudFront

## Goal
Serve my S3-hosted resume over HTTPS using CloudFront.

## What I did
- Created a CloudFront distribution with S3 origin
- Enabled Origin Access Control (OAC) so S3 can be private
- Set viewer protocol policy to redirect HTTP → HTTPS
- Set default root object to `index.html`
- Updated S3 bucket policy to allow CloudFront access only

## Result
https://dsnxfcve3qr2l.cloudfront.net/