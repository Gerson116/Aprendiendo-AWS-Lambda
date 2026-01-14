
ingreso = 0

def contador_ingreso():
    ingreso += 1

contador_ingreso()

def lambda_handler():
    
    mensaje = "Está haciendo frío, ¿no?"
    if ingreso > 0:
        mensaje = f"Está haciendo frío, ¿no? Esta es la vez número {ingreso} que alguien lo dice."

    print(mensaje)

    return {
        'statusCode': 200,
        'body': mensaje
    }