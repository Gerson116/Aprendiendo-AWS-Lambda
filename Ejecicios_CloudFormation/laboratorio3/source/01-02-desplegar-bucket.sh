# paso 1: Crear el bucket S3
aws cloudformation create-stack --stack-name S3BucketLambdaDeployments --template-body file://01-01-s3-bucket-lambda-deployments.json


# paso 2: Subir el código
aws s3 cp lambda_cold_start.zip s3://test-laboratorio3-lambda-deployments-us-east-1/