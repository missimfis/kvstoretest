#!/usr/bin/env python3
import requests;
import json;

data = {
"_class": "GenerateUDR",
"broadcast": 'true',
"from": 0,
"to": 1514764799
}  
r = requests.post('http://160.85.4.251:4567/command', json.dumps(data))


data ={
"_class": "BillRequest",
"account": "fischmis",
"from": 0,
"to": 1514764799
} 
r = requests.post('http://160.85.4.251:4567/command', json.dumps(data))
