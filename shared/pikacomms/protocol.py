import json

# Todo: Integrate template in parsing
template = {
    "params": {},
    "routing-key": "",
    "function": "",
    "reply": {
        "corr-id": "",
        "reply-to": ""
    }
}


def parseToNet(data : dict) -> bytes:
    return json.dumps(data).encode('utf-8')

def parseFromNet(data : bytes) -> dict:
    return json.loads(data.decode('utf-8'))