import json
import hashlib
import hmac
from datetime import datetime, timedelta


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

    """Validar firma personalizada basada en timestamp + secret"""
    headers = event.get('headers', {})
    signature = headers.get('x-signature')
    timestamp = headers.get('x-timestamp')
    
    if not signature or not timestamp:
        return False
    
    # Verificar que el timestamp no sea muy viejo (5 minutos)
    try:
        req_time = datetime.fromtimestamp(int(timestamp))
        if datetime.now() - req_time > timedelta(minutes=5):
            return False
    except:
        return False
    
    # Generar firma esperada
    secret = 'tu-clave-secreta'
    body = event.get('body', '')
    message = f"{timestamp}{body}"
    expected_signature = hmac.new(
        secret.encode(), 
        message.encode(), 
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)