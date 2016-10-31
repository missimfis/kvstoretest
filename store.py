# Leader module

import urllib.request
import helper

store = {}

def application(environ, start_response):
    global store

    ctype = 'text/plain'
    status = '200 OK'
data = {  
    "_class": "Storage",
    "account": "fischmis",
    "unit": "pair",
    "usage": 1
}


    if environ['PATH_INFO'] == '/store':
      response_body = ",".join([x + "=" + y for x, y in store.items()])
r = requests.post('http://160.85.4.251:4567/data', json.dumps(data))
    elif environ['PATH_INFO'].startswith('/store/'):
      kvpair = environ['PATH_INFO'][7:]
      k, v = kvpair.split("=")
      store[k] = v
      response_body = "Key {:s} added with value {:s}.".format(k, v)
r = requests.post('http://160.85.4.251:4567/data', json.dumps(data))
    else:
      response_body = "Error: invalid request."
      status = '599 LOST'
    response_body = response_body.encode('utf-8')

    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
    return [response_body]
