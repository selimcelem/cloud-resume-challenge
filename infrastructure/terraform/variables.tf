variable "aws_region" {
  type    = string
  default = "eu-west-1"
}

variable "project_name" {
  type    = string
  default = "cloud-resume"
}

variable "dynamodb_table_name" {
  type    = string
  default = "visitor-counter"
}

variable "lambda_function_name" {
  type    = string
  default = "visitorCounter"
}
