#   Crear el bucket S3
aws cloudformation create-stack --stack-name s3-test-api-rest --template-body file://../aws_cloudformation_templates/01-s3.json

#   Subir el código
# aws s3 cp lambda_cold_start_v3.zip s3://s3-lambda-cold-start-test-api-rest-us-east-1-356818563518/