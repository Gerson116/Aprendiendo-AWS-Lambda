#Paso 1: Crearlo
aws cloudformation create-stack --stack-name LambdaTestLaboratorio3Stack --template-body file://02-01-lambda-test-laboratorio-3.json --capabilities CAPABILITY_NAMED_IAM



# Paso 2: Actualizarlo
aws cloudformation update-stack --stack-name LambdaTestLaboratorio3Stack --template-body file://02-01-lambda-test-laboratorio-3.json --capabilities CAPABILITY_NAMED_IAM