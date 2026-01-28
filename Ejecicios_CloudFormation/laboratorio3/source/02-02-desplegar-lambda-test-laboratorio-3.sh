#   Crear Stack
aws cloudformation create-stack --stack-name LambdaTestLaboratorio3Stack --template-body file://02-01-lambda-test-laboratorio-3.json --capabilities CAPABILITY_NAMED_IAM

#   Actualizarlar Stack
aws cloudformation update-stack --stack-name LambdaTestLaboratorio3Stack --template-body file://02-01-lambda-test-laboratorio-3.json --capabilities CAPABILITY_NAMED_IAM

#   Eliminar Stack
aws cloudformation delete-stack --stack-name LambdaTestLaboratorio3Stack

#   Deploy
aws cloudformation deploy --template-file 02-01-lambda-test-laboratorio-3.json --stack-name LambdaTestLaboratorio3Stack --capabilities CAPABILITY_NAMED_IAM
