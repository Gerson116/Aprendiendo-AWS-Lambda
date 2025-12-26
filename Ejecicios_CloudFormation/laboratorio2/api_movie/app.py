def lambda_handler(event, context):
    movies = [
        {'title': 'Inception', 'year': 2010},
        {'title': 'The Matrix', 'year': 1999},
        {'title': 'Interstellar', 'year': 2014}
    ]
    return {
        'statusCode': 200,
        'body': movies
    }