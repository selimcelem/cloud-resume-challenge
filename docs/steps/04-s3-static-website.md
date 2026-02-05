# Step 4 – Static Website Hosting on Amazon S3

## Goal

Deploy my HTML/CSS resume as a publicly accessible static website using Amazon S3.

## Actions Performed

1. Created an S3 bucket:
   - Bucket name: selimcelem-cloud-resume
   - Region: eu-central-1

2. Uploaded frontend files:
   - index.html
   - style.css

3. Enabled static website hosting:
   - Index document: index.html
   - Error document: index.html

4. Added public bucket policy to allow read access.

## Result

My resume is now publicly accessible at:

http://selimcelem-cloud-resume.s3-website.eu-central-1.amazonaws.com/

## What I Learned

- How to host static websites using Amazon S3
- How S3 bucket policies control public access
- How to deploy front-end content without a server
