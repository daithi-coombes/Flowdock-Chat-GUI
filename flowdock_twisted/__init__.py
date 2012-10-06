import urllib2
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent,  HTTPConnectionPool

class IgnoreBody(Protocol):
    def __init__(self, deferred):
        self.deferred = deferred

    def dataReceived(self, bytes):
        pass

    def connectionLost(self, reason):
        self.deferred.callback(None)


def cbRequest(response):
    print 'Response code:', response.code
    print response.content
    print response.text
    print response.json
    finished = Deferred()
    response.deliverBody(IgnoreBody(finished))
    return finished

#variables
URL_STREAM = "https://stream.flowdock.com/flows/?filter=web-eire/main"
USER = "webeire@gmail.com"
PASS = "chanman77"
pool = HTTPConnectionPool(reactor)
agent = Agent(reactor, pool=pool)
d = agent.request('GET', URL_STREAM)
d.addCallback(cbRequest)

def requestGet(url):
    d = agent.request('GET', URL_STREAM)
    d.addCallback(cbRequest)
    return d

# Two requests to the same host:
d = requestGet('http://localhost:8080/foo').addCallback(
    lambda ign: requestGet("http://localhost:8080/bar"))
def cbShutdown(ignored):
    reactor.stop()
d.addCallback(cbShutdown)

reactor.run()

print "runs in background"
