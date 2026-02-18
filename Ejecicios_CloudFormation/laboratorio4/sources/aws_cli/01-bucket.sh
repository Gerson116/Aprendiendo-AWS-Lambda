#   Crear el bucket S3
aws cloudformation create-stack --stack-name s3-lambda-api-rest --template-body file://../aws_cloudformation_templates/01-s3.json

#   Subir lambda 1
aws s3 cp lambda_cliente.zip s3://s3-lambda-api-rest-rest-us-east-1-356818563518/

#   Subir lambda 2
aws s3 cp lambda_servicio.zip s3://s3-lambda-api-rest-rest-us-east-1-356818563518/

#   Subir lambda 3
aws s3 cp lambda_usuario.zip s3://s3-lambda-api-rest-rest-us-east-1-356818563518/