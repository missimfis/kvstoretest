# URL to an instance which hosts the authorative registry
bootstrapnode = "http://kvstore-kvstorefischmis.44fs.preview.openshiftapps.com/"

# URL to this instance
# TODO: find a way to query this from OpenShift Online (v2: was OPENSHIFT_APP_DNS)
#selfnode = "http://kvstore-kvstorefischmis.44fs.preview.openshiftapps.com/"
#selfnode = "http://localhost:8080"
try:
  f = open(".selfnode", "r")
  selfnode = f.readline().strip()
except:
  import os
  selfnode = os.getenv("APP_DNS")
  if not selfnode:
    selfnode = bootstrapnode
