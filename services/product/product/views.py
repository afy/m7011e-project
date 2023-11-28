#from .models import Product
from ....shared.pikacomms.client import PikaClient
from ....shared.pikacomms.APIGatewayServer import ApiGatewayServer

api_gateway_server = ApiGatewayServer()
print(api_gateway_server)