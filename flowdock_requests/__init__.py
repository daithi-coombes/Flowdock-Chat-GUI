#http://docs.python-requests.org/en/latest/index.html
import requests
import json
import sys

URL_STREAM = "https://stream.flowdock.com/flows/?filter=web-eire/main"
USER = "webeire@gmail.com"
PASS = "chanman77"
my_config = {'verbose': sys.stderr}

client = requests.session()
r = client.get( URL_STREAM,
    data={'track': 'requests'}, auth=( USER ,  PASS ),  config=my_config)
print "request sent"
print r.status_code
print r.headers
for line in r.iter_content():
    if line: # filter out keep-alive new lines
        print json.loads(line)
        sys.stdout.flush()
