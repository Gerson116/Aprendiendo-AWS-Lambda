
# paso 1: Crear una política para acceder al s3
aws iam create-policy \
    --policy-name LambdaS3AccessPolicy \
    --policy-document file://AmazonS3ReadOnlyAccess.json

# paso 2 - Se debe crear un rol para los lambdas

# paso 3 crear un lambda con AWS CLI
aws lambda create-function \
    --function-name hola_mundo \
    --runtime python3.13 \
    --role
    --handler app.lambda_handler \
    --zip-file fileb://app.zip