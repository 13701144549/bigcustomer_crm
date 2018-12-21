# coding: utf-8
import os, sys
from qfcommon.server import thriftserver

class Handler:
    def ping(self):
        pass

def test():
    from qfcommon.base import logger
    logger.install('stdout')
    from qfcommon.thriftclient.payprocessor import PayProcessor

    class TestHandler (Handler):
        def trade(self, jsonstr):
            log.debug('recv:', jsonstr)
            
    server = thriftserver.ThriftServer(PayProcessor, TestHandler, ('127.0.0.1', 10000), 3)
    server.forever()


if __name__ == '__main__':
    test()


