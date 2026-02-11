output "dynamodb_table_name" {
  value = aws_dynamodb_table.visitor_counter.name
}

output "api_invoke_url" {
  value = aws_apigatewayv2_stage.prod.invoke_url
}
