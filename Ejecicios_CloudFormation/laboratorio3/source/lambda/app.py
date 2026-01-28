import json

ingreso = 0

def contador_ingreso():
    global ingreso
    ingreso += 1

contador_ingreso()

def lambda_handler(event, context):
    global ingreso
    
    # Incrementar el contador en cada invocación
    contador_ingreso()
    
    # Mensaje para cold start (primera vez que se ejecuta)
    if ingreso == 1:
        mensaje = "Está haciendo frío, ¿no? (Cold Start detectado)"
    else:
        mensaje = f"Contador actual: {ingreso} (Lambda caliente)"

    print(f"Invocación número: {ingreso}")
    print(mensaje)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'mensaje': mensaje,
            'contador': ingreso,
            'cold_start': ingreso == 1
        })
    }