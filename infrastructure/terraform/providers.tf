terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
   backend "s3" {
    bucket         = "selimcelem-cloud-resume-tfstate"
    key            = "cloud-resume-challenge/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
   }
}

provider "aws" {
  region = var.aws_region
}
