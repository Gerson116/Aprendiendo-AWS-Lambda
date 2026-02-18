# import os, sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lambdas.cliente.app import lambda_handler


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

