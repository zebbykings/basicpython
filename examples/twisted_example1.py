#!/usr/bin/env python
from twisted.internet import protocol, reactor, endpoints


class Echo (protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()

endpoints.serverFromSTring(reactor,"tcp:1234").listen(EchoFactory())
