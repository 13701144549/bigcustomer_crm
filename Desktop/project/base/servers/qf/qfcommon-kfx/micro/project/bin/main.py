# coding: utf-8
import os, sys
from qfcommon.micro import core
from qfcommon.thriftclient.payprocessor import PayProcessor
import logging

log = logging.getLogger()

class TestHandler (core.Handler):
    define = PayProcessor

    def ping(self):
        log.debug('ping')
    
    def _initial(self):
        log.debug('run in every proc ...')

