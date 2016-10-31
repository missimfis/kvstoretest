#!/usr/bin/env python3

port = 8080
host = 'localhost'

import urllib.request
import registry
import leader
import store
import config

def registerself():
    if config.selfnode != config.bootstrapnode:
        print("registering as", config.selfnode)
        try:
            res = urllib.request.urlopen(config.bootstrapnode + "/registry/" + config.selfnode)
            l = res.read()
        except Exception as e:
            print("warning:", e)
    else:
        print("registry node, not registering (create .selfnode to identify)")

registerself()

def application(environ, start_response):
    ctype = 'text/plain'
    status = '200 OK'

    if environ['PATH_INFO'].startswith("/registry"):
        return registry.application(environ, start_response)
    elif environ['PATH_INFO'].startswith("/store"):
        return store.application(environ, start_response)
    else:
        return leader.application(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server(host, port, application)
    while True:
        print("await connection...")
httpd.handle_request()
