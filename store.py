# Leader module

import urllib.request
import helper

store = {}

def application(environ, start_response):
    global store

    ctype = 'text/plain'
    status = '200 OK'

    if environ['PATH_INFO'] == '/store':
      response_body = ",".join([x + "=" + y for x, y in store.items()])
    elif environ['PATH_INFO'].startswith('/store/'):
      kvpair = environ['PATH_INFO'][7:]
      k, v = kvpair.split("=")
      store[k] = v
      response_body = "Key {:s} added with value {:s}.".format(k, v)
    else:
      response_body = "Error: invalid request."
      status = '599 LOST'
    response_body = response_body.encode('utf-8')

    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
    return [response_body]
