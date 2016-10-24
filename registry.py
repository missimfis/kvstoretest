# Registry module

import config

participants = {}

def application(environ, start_response):
    global participants

    ctype = 'text/plain'
    status = '200 OK'

    if environ['PATH_INFO'] == '/registry':
      p = ""
      for tenant in participants:
        if p:
          p += ","
        p += tenant + ":"
        p += ",".join(participants[tenant])
      response_body = "Participants: {:s}".format(p)
    elif environ['PATH_INFO'].startswith('/registry/'):
      addnode = environ['PATH_INFO'][10:]
      tenant = None
      for i, c in enumerate(addnode):
        if i > 0 and c == "/" and addnode[i+1] != "/" and addnode[i-1] != "/" and addnode[i-1] != ":":
          tenant = addnode[:i]
          addnode = addnode[i+1:]
          break
      if not tenant:
        tenant = addnode
        if tenant in participants:
          response_body = "Participants: {:s}".format(",".join(participants[tenant]))
        else:
          response_body = "No such tenant."
          status = "599 LOST"
      else:
        if addnode not in participants and not addnode.startswith(config.selfnode):
          if not tenant in participants:
            participants[tenant] = []
          participants[tenant].append(addnode)
          response_body = "Node {:s} added.".format(addnode)
          for node in participants[tenant]:
            if node == addnode or node == config.selfnode:
              msg = "Skipping {:s}.".format(node)
            else:
              success = True
              try:
                # TODO: proper encoding and decoding of addnode
                res = urllib.request.urlopen(node + "/registry/" + addnode)
              except:
                success = False
              msg = "Informing {:s} about new node (success: {:d}).".format(node, success)
            response_body += " " + msg
        else:
          response_body = "Not adding {:s}, it is already in the list or ineligible to enter.".format(addnode)
    response_body = response_body.encode('utf-8')

    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)
return [response_body]
