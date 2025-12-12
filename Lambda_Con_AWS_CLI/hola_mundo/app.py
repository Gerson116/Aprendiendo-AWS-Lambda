def lambda_handler(event, _):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }