import json
import requests
from requests.exceptions import ConnectionError
import config
import logging

def get_price(symbol):
    payload = {"symbol": symbol}
    try:
        r = requests.get(config.BASE_URL + "/api/v3/ticker/price", params=payload)
    except Exception as e:
        raise ConnectionError("Something happen to connection")

    logging.debug("Status code: %d" % r.status_code)
    if r.status_code == 200:
        json_body = json.loads(r.text)
        logging.debug("GET %s " % json_body)
        return float(json_body.get('price', 0.0))
    elif r.status_code == 400:
        raise ValueError("Invalid Symbol")
    else:
        raise ValueError("I have no idea")
