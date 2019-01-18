# coding:utf-8

import json
import config
import logging
import traceback

from qfcommon.web import cache
from qfcommon.web.cache import CacheDict
from qfcommon.base.dbpool import get_connection, get_connection_exception

log = logging.getLogger()


# 获取角色下的权限(仅限org)
def get_perms(role_code, data):

    perms = []
    with get_connection('qf_user') as db:
        perms = db.select(
            table = 'permission_role_map',
            fields = 'permission_code',
            where = {'role_code': role_code}
        ) or []

    return perms

perm_cache = CacheDict(
    get_perms, getattr(config, 'PERMS_CACHE_TIME', 7*24*3600))

def get_role_name(role_code, data):

    info = {}
    with get_connection('qf_user') as db:
        info = db.select_one(
            table = 'permission_role',
            fields = 'name',
            where = {'code': role_code}
        ) or {}

    return info.get('name') or ''

role_name_cache = CacheDict(
    get_role_name, getattr(config, 'PERMS_CACHE_TIME', 7*24*3600))

def get_perm_name(perm_code, data):

    info = {}
    with get_connection('qf_user') as db:
        info = db.select_one(
            table = 'permission',
            fields = 'name',
            where = {'code': perm_code}
        ) or {}

    return info.get('name') or ''

perm_name_cache = CacheDict(
    get_perm_name, getattr(config, 'PERMS_CACHE_TIME', 7*24*3600))

def get_channel(chnlid, data):

    info = {}
    with get_connection('qf_core') as db:
        info = db.select_one(
            table = 'channel',
            where = {'code': chnlid}
        ) or {}

    return info

chnl_info_cache= CacheDict(
    get_channel, getattr(config, 'PERMS_CACHE_TIME', 7*24*3600))

def get_temp(temp_id, data):

    info = {}
    with get_connection('qf_org') as db:
        info = db.select_one(
            table = 'clearing_temp',
            where = {'id': temp_id}
        ) or {}

    return info

temp_info_cache= CacheDict(
    get_temp, getattr(config, 'PERMS_CACHE_TIME', 7*24*3600))

def get_mysql_constants(key, data):
    try:
        with get_connection_exception('qf_mchnt') as db:
            ret = db.select_one(
                'constants', where = {'key': key, 'status': 1},
                fields = 'value, type'
            )

            if ret:
                if ret['type'] == 1:
                    return ret['value']
                else:
                    return json.loads(ret['value'])
    except:
        log.warn(traceback.format_exc())

    return data

constants_cache = CacheDict(
    get_mysql_constants,
    getattr(config, 'MYSQL_CONSTANTS_CACHE', 72 * 3600)
)


## 店铺类型
def load_shop_cates(data=None):
    cates = None
    with get_connection('qf_mchnt') as db:
        cates = db.select(
            'shop_category',
            where = {
                'status' : 1,
                'create_time' : ('>=', '2016-05-18 06:59:59')
            },
            fields = 'id, parent_id, name, weight',
            other = 'order by weight desc'
        )

        cates = {i['id']:i for i in cates}

    return cates

cache.setvalue(
    'kuma_shop_cates', load_shop_cates,
    getattr(config, 'KUMA_SHOP_CATE_CACHE', 3600)
)
