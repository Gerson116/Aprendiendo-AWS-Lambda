#   Crear el bucket S3
aws cloudformation create-stack --stack-name s3-lambda-cold-start --template-body file://01-01-s3-bucket-lambda-deployments.json

#   Actualizar bucket
aws cloudformation update-stack --stack-name s3-lambda-cold-start --template-body file://01-01-s3-bucket-lambda-deployments.json

#   Comprimir carpeta lambda
tar -a -c -f lambda_cold_start_v3.zip app.py

#   Subir el código
aws s3 cp lambda_cold_start_v3.zip s3://s3-lambda-cold-start-lambda-deployments-us-east-1-356818563518/