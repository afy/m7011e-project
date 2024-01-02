import json
import warnings

# Default template size: 91 bytes in size after json conversion
template = {
    "params": {},
    "routing-key": "",
    "function": "",
    "reply": {
        "corr-id": "",
        "reply-to": ""
    }
}

# Constants
NO_REPLY = None


# Sending 
def parseToNet(params: dict, routing_key: str, function: str = "", reply = NO_REPLY) -> bytes:
    data = {
        "params": params,
        "routing-key": routing_key,
        "function": function,
        "reply": reply
    }
    return json.dumps(data).encode('utf-8')


# Recieving
def parseFromNet(data : bytes) -> dict:
    data = json.loads(data.decode('utf-8'))
    if data.keys() == template.keys():
        return data
    warnings.warn(f"Parsed data keys do not match expected value: {data}")
    return data