import json
import jwt  # PyJWT library
import hashlib
import hmac
from datetime import datetime, timedelta


ingreso = 0

def contador_ingreso():
    ingreso += 1

contador_ingreso()

def lambda_handler(event, context):

    headers = event.get('headers', {})
    auth_header = headers.get('authorization', '') or headers.get('Authorization', '')

    if not is_authenticated(auth_header, event):
        return {
            'statusCode': 401,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'No autorizado',
                'message': 'Token inválido o expirado'
            })
        }
    
    mensaje = "Está haciendo frío, ¿no?"
    if ingreso > 0:
        mensaje = f"Está haciendo frío, ¿no? Esta es la vez número {ingreso} que alguien lo dice."

    print(mensaje)

    return {
        'statusCode': 200,
        'body': mensaje
    }

def is_authenticated(auth_header, event):
    """Diferentes métodos de autenticación"""
    
    # Opción 1: API Key simple
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.replace('Bearer ', '')
        return validate_api_key(token)
    
    # Opción 2: JWT Token
    if auth_header and auth_header.startswith('JWT '):
        token = auth_header.replace('JWT ', '')
        return validate_jwt_token(token)
    
    # Opción 3: Firma personalizada
    return validate_custom_signature(event)

def validate_api_key(token):
    """Validar API key contra lista permitida"""
    valid_keys = [
        'tu-api-key-secreta-1',
        'tu-api-key-secreta-2'
    ]
    return token in valid_keys

def validate_jwt_token(token):
    """Validar JWT token"""
    try:
        secret_key = 'tu-clave-secreta-jwt'
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        
        # Verificar expiración
        if payload.get('exp', 0) < datetime.utcnow().timestamp():
            return False
            
        return True
    except:
        return False
    
def validate_custom_signature(event):
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