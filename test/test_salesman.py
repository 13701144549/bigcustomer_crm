# coding=utf-8
# -*- coding:utf-8 -*-
# @Time         : 2018/12/20 11:41 AM
# @Description  : about test salesman

import json
import fire

from base import Base


class Sales(Base):

    def list(self, **kw):
        self._url = '/org/salesman/list'

        self._data = {
            # 'status' : 1,
            # 'slsm_uid': 333,
            # 'page' : 4,
            # 'page_size' : -1,
            # 'salesname': 'mer',
            # 'mobile': 'mer'
        }

        return self.get(with_sid=True)

    def info(self, **kw):
        self._url = '/org/salesman/info'

        self._data = {
            'userid': '21018168',
        }

        return self.get(with_sid=True)

    def edit(self, **kw):
        self._url = '/org/salesman/edit'

        self._data = {
            'userid': 21018168,
            # 'salesname': '测试业务员名称2',
            'mobile': 1580101540,
            # 'email' : 'emai11@139.com',
            # 'password' : 12345678,
            # 'confirm_password' : 12345678,
            # 'idnumber': 9999999,
            # 'idcardfront': 9999999,
            # 'status': 1,

        }

        return self.post(with_sid=True)

    def signup(self, **kw):
        self._url = '/org/salesman/signup'

        self._data = {
            "email": "emai14@139.com",
            "salesname": "测试业务员名称1",
            "mobile": 15801015594,
            "password": "12321",
            "confirm_password": "123456",
            "idnumber": 342123,
            "idcardfront": "f43f611b67d0521a97711da389d1b376.jpg",
        }

        return self.post()


if __name__ == '__main__':
    fire.Fire(Sales)
