# Leader module

import random
import urllib.request
import helper
import config

def application(environ, start_response):
    ctype = 'text/plain'
    status = '200 OK'

    if environ['PATH_INFO'] == '/':
      response_body = "Triple-Microservice KV Store (identity: {:s}). Registry: /registry[/<tenant>] or /registry[/<tenant>]/<node-to-add>. Leader: /leader or /leader/vote. Store: /store or /store/<key>=<value>.".format(config.selfnode)
    elif environ['PATH_INFO'] == '/leader':
      response_body = "Our dear leader."
      participants = helper.getparticipants(config.bootstrapnode)
      for node in participants:
        if node == config.selfnode:
          continue
        response_body += " Perhaps {:s}?".format(node)
        try:
          res = urllib.request.urlopen(node + "/leader/vote", timeout=2)
          l = res.read().decode("utf-8")
          response_body += " => {:s}.".format(l)
        except:
          response_body += " => (not reached)."
    elif environ['PATH_INFO'] == '/leader/vote':
      vote = random.choice([True, False])
      response_body = str(vote)
    else:
      response_body = "Error: invalid request."
      status = '599 LOST'
    response_body = response_body.encode('utf-8')

    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
    return [response_body]
