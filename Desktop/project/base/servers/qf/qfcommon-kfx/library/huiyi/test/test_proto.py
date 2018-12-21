# coding=utf-8
import unittest
import logging
import sys

from bin.handler.huiyi.huiyi_proto import HuiyiProto
from qfcommon.qfpay import defines

log = logging.getLogger()


class TestBuildHeader(unittest.TestCase):

    def test_valid(self):
        proto = HuiyiProto()
        header = proto._pack_header(1000, 1234)

        self.assertEqual(len(header), 46, 'header len must be 46.')

    def test_invalid_message_len_too_small(self):
        proto = HuiyiProto()

        self.assertRaises(ValueError, proto._pack_header, 45, 1234)

    def test_invalid_message_len_too_long(self):
        proto = HuiyiProto()

        self.assertRaises(ValueError, proto._pack_header, 1847, 1234)


# @unittest.skip('')
class TestQf2huiyi(unittest.TestCase):
    def test_qf2huiyi_valid(self):
        indata = {
            u'chcd': u'04012900', u'termreadability': u'5', u'cardpin': 24, u'regioncd': u'2900',
            u'localdt': u'0506135133', u'icccondcode': u'0', u'clisn': u'583005',
            u'syssn': u'160506583005', u'iccdata': 204, u'mchntid': u'601601044580032',
            u'txcurrcd': u'156', u'mcc': u'4458', u'posentrymode': u'051', u'txndir': u'Q',
            u'qfpay_items': {u'channel_flag': u'cardinfolink', u'send_time': 1462513893.823074},
            u'mchntnm': u'\u9ad8\u65b0\u533a\u6d2a\u5927\u738b\u9152\u884c',
            u'cardcd': u'622848*********0774', u'txdt': u'0506135133', u'cardseqnum': u'000',
            u'terminalid': u'00320000', u'busicd': u'300000', u'inscd': u'66800000',
            u'trackdata3': u'', u'trackdata2': 52
        }

        proto = HuiyiProto()
        # print 'to_huiyi_data: ', proto.qf2huiyi(indata)




@unittest.skip('')
class TestHuiyi2qf(unittest.TestCase):
    def test_huiyi2qfpay_valid(self):
        resp_data = '.\x01034299990000   88830000   0000000000000000000200\xf2<F\xc1\xa8\xe0\x9a\x10\x00\x00\x00\x00\x00\x00\x00A1662227699010777830000000000000010000506145403720113145403050623124111071001001208622029000866660000376222769901077783=2312206000009280000161271472011300000008622220241110000\xd6\xc7\xc4\xdc\xd6\xd5\xb6\xcb\xc8\xab\xd6\xa7\xb8\xb6                          156N\xed/\xe2c\xdf?\xeb2600000000000000164\x9f&\x08\xc1?\xef\xbb\xbd\xe0\x7fI\x9f\x10\x13\x07\x01\x17\x03\xa0\x00\x00\x01\n\x01\x00\x00\x00\x00\x00\x84\x9e\x93\xe7\x9f7\x04\xeb\x0e\xe0\n\x9f6\x02\x03\x83\x95\x05\x00\x00\x00\x00\x00\x9a\x03\x16\x05\x06\x9c\x01\x00\x9f\x02\x06\x00\x00\x00\x00\x10\x00_*\x02\x01V\x82\x02|\x00\x9f\x1a\x02\x01V\x9f3\x03\xe0\xf0\xc8\x9f5\x01"\x84\x08\xa0\x00\x00\x033\x01\x01\x02\x9f\t\x02\x00 \x9fc\x1003100000\x00\x00\x00\x00\x00\x00\x00\x00\x9f\x1e\x0850631111\x9f\x03\x06\x00\x00\x00\x00\x00\x00\x9f\'\x01\x80\x9fA\x04\x00\x00\x00\x00\x9f4\x03\x00\x00\x00020000006\x00003000000000001601000000  000336F956B7E0'

        proto = HuiyiProto()
        data = proto.huiyi2qf(
            {
                'busicd': defines.QF_BUSICD_BALANCE,
            },
            resp_data
        )

        # print data

if __name__ == '__main__':
    log.setLevel('DEBUG')
    log.addHandler(logging.StreamHandler(sys.stdout))

    unittest.main()
