# coding:utf-8

import config
import logging
import traceback

from excepts import ThirdError

from runtime import apcli

from qfcommon.server.client import ThriftClient
from qfcommon.base.tools import thrift_callex
from qfcommon.thriftclient.org import OrgServer
from qfcommon.thriftclient.org.ttypes import QudaoException
from qfcommon.thriftclient.apollo.ttypes import ApolloException
from qfcommon.thriftclient.finance import Finance
from qfcommon.thriftclient.finance.ttypes import ServerException
from qfcommon.thriftclient.mchnt_thrift import MchntThrift
from qfcommon.thriftclient.mchnt_thrift.ttypes import MTException
from qfcommon.thriftclient.account2 import Account2
from qfcommon.thriftclient.account2.ttypes import ServerError

log = logging.getLogger()


def org_client(func, *args, **kw):
    try:
        client = ThriftClient(config.ORG_API_SERVER, OrgServer, framed=True)
        return client.call(func, *args, **kw)
    except QudaoException as e:
        raise ThirdError(e.respmsg)
    except:
        log.warn(traceback.format_exc())
        raise ThirdError('第三方服务错误')


def account2_client(func, *args, **kw):
    try:
        return thrift_callex(
            config.ACCOUNT2_SERVER, Account2,
            func, *args, **kw
        )
    except ServerError as e:
        raise ThirdError(e.msg)
    except:
        log.warn(traceback.format_exc())
        raise ThirdError('第三方服务错误')


def ap_client(func, *args, **kw):
    try:
        return apcli(func, *args, **kw)
    except ApolloException as e:
        raise ThirdError(e.respmsg)
    except:
        log.warn(traceback.format_exc())
        raise ThirdError('第三方服务错误')

def mchnt_thrift_client(func, *args, **kw):
    try:
        return thrift_callex(
            config.MCHNT_THRIFT_SERVERS, MchntThrift,
            func, *args, **kw
        )
    except MTException, e:
        raise ThirdError(e.respmsg)
    except:
        raise ThirdError('第三方服务出错')


def finance_client(func, *args, **kw):
    try:
        client = ThriftClient(config.FINANCE_SERVER, Finance)
        return client.call(func, *args, **kw)
    except ServerException as e:
        raise ThirdError(e.error_msg)
    except:
        log.warn(traceback.format_exc())
        raise ThirdError('第三方服务错误')
