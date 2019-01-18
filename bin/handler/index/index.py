# coding:utf-8

import logging

from utils.base import BaseHandler

log = logging.getLogger()


class Ping(BaseHandler):

    def GET(self):
        return 'ok'

    POST = GET
