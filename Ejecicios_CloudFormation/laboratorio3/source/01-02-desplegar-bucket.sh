#   Crear el bucket S3
aws cloudformation create-stack --stack-name S3BucketLambdaColdStart --template-body file://01-01-s3-bucket-lambda-deployments.json

#   Actualizar bucket
aws cloudformation update-stack --stack-name S3BucketLambdaColdStart --template-body file://01-01-s3-bucket-lambda-deployments.json

#   Comprimir carpeta lambda
tar -a -c -f lambda_cold_start_v2.zip app.py

#   Subir el código
aws s3 cp lambda_cold_start_v2.zip s3://test-laboratorio3-lambda-deployments-us-east-1/