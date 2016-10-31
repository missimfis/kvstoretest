#!/usr/bin/env python3
import json;
import requests;

data = {  
    "_class": "Storage",
    "account": "fischmis",
    "unit": "pair",
    "usage": 1
}
r = requests.post('http://160.85.4.251:4567/data', json.dumps(data))

