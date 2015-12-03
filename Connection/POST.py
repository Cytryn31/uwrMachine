import http.client
import urllib
import re

def send(url, request, params, data):
    h = http.client.HTTPConnection(url,)
    h.add_credentials('admin', 'admin')
    # specify we're sending parameters that are url encoded
    headers = { 'Content-Type' : ' application/json' }
    # url encode the parameters
    url_params = urllib.parse.urlencode(params)
    # send out the POST request
    h.request('POST', request, url_params, headers, body=urllib.parse.urlencode(data))

    # get the response
    r = h.getresponse()

    # analyse the response
    if re.search("Error", r.read.decode()):
        print("Not found")
    else:
        print("Probably found")

    h.close()