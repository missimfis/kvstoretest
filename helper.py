import urllib.request

def getparticipants(bootstrapnode):
    # TODO: apparently a service cannot invoke itself even with another method
    import config
    if config.selfnode == bootstrapnode:
        return []

    try:
        res = urllib.request.urlopen(bootstrapnode + "/registry")
        # TODO: read actual participants only upon return code 200
        l = res.read().decode("utf-8")
        l = l.replace("Participants: ", "")
        queriedparticipants = l.split(",")
    except:
        queriedparticipants = []
    return queriedparticipants
