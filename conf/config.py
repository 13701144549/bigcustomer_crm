# coding:utf-8

import os
from webconfig import *

# 服务地址
HOST = '0.0.0.0'

# 服务端口
PORT = 6000

DEBUG = False

# 日志文件配置
# LOGFILE = os.path.join(HOME, '../log/project.log')
LOGFILE = 'stdout'

# 数据库配置
DATABASE = {
    'qf_bcm': {
        'engine': 'pymysql',
        'db': 'qf_bcm',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_core': {
        'engine': 'pymysql',
        'db': 'qf_core',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_user': {
        'engine': 'pymysql',
        'db': 'qf_user',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
}

# cookie配置
COOKIE_CONFIG = {
    'max_age': 86400,
    'domain': None,
}

# 生成id
# SPRING_SERVERS = [{'addr': ('172.100.101.106', 4590), 'timeout': 20000}, ]
SPRING_SERVERS = [{'addr': ('172.100.101.110', 7110), 'timeout': 20000}, ]

# apollo 服务
APOLLO_SERVERS = [{'addr': ('127.0.0.1', 6900), 'timeout': 2000}, ]

# 商户相关操作
MCHNT_THRIFT_SERVERS = [{'addr': ('127.0.0.1', 6800), 'timeout': 60000}]

# redis配置
REDIS_CONF = {
    'host' : '172.100.101.107',
    # 'host': '172.100.101.106',
    'port': 6379,
    'password': '',
    # 'default_expire' : 2 * 24 * 60 * 60
}







