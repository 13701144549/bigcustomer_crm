# coding:utf-8

from handler.index import index

urls = (
    # ping
    ('^/bcm/ping$', index.Ping),

)

