
import json
# from consts.constants import METODOS_HTTP
class METODOS_HTTP(str):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


def lambda_handler(event, context):
    method = (
        event.get('httpMethod') or
        event.get('requestContext', {}).get('http', {}).get('method')
    )
    
    if method in METODOS_HTTP.GET:
        print("Se consulto un cliente con GET")
        return {"statusCode": 200, "body": "Se consulto un cliente con GET"}
    elif method in METODOS_HTTP.POST:
        print("Se agrego un cliente con POST")
        return {"statusCode": 200, "body": "Se agrego un cliente con POST"}
    elif method in METODOS_HTTP.PUT:
        print("Se actualizo todo un cliente con PUT")
        return {"statusCode": 200, "body": "Se actualizo todo un cliente con PUT"}
    elif method in METODOS_HTTP.PATCH:
        print("Se actualizaron datos especificos con PATCH")
        return {"statusCode": 200, "body": "Se actualizaron datos especificos con PATCH"}
    elif method in METODOS_HTTP.DELETE:
        print("Se elimino un cliente DELETE")
        return {"statusCode": 200, "body": "Se elimino un cliente DELETE"}
    
event = {
  "requestContext": {
    "http": {
      "method": "GET",
      "path": "/usuarios"
    }
  },
  "body": {"nombre": "gerson", "apellidos": "Santos Mateo"},
  "isBase64Encoded": False
}


_ = lambda_handler(event, None)