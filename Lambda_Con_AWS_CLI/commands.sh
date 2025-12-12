
# paso 1: Crear una política para acceder al s3
aws iam create-policy \
    --policy-name LambdaS3AccessPolicy \
    --policy-document file://Lambda_Con_AWS_CLI/AmazonS3ReadOnlyAccess.json

# paso 2 - Se debe crear un rol para los lambdas
aws iam create-role \
    --role-name LambdaS3ExecutionRole \
    --assume-role-policy-document file://Lambda_Con_AWS_CLI/trust-policy.json

# paso 3 crear un lambda con AWS CLI
aws lambda create-function \
    --function-name hola_mundo \
    --runtime python3.13 \
    --role arn:aws:iam::356818563518:role/LambdaS3ExecutionRole \
    --handler app.lambda_handler \
    --zip-file fileb://Lambda_Con_AWS_CLI/hola_mundo/app.zip