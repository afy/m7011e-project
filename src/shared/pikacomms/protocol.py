import json
import warnings

# Default template size: 91 bytes in size after json conversion
template = {
    "error": None,
    "params": {},
    "function": "",
    "user-validation": {
        "id": "",
        "groups": []
    }
}

not_implemented_response = {"error": "function not implemented", "params":{}, "function":None, "user-validation":None}
undefined_logic_response = {"error": "undefined logic", "params":{}, "function":None, "user-validation":None}

def parseToError(details:str):
    return json.dumps({"error": details, "params":{}, "function":None, "user-validation":None}).encode('utf-8')

# Sending 
def parseToNet(params:dict, function:str, userv:dict = None, error:str=None) -> bytes:
    data = {
        "params": params,
        "function": function,
        "user-validation":userv,
        "error":error
    }
    return json.dumps(data).encode('utf-8')


# Recieving
def parseFromNet(data : bytes) -> dict:
    data = json.loads(data.decode('utf-8'))
    if data.keys() == template.keys():
        return data
    warnings.warn(f"Parsed data keys does not match expected value: {data}")
    return data