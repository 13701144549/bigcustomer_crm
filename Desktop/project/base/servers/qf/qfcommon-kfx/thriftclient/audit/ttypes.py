#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class AuditException(TException):
  """
  Attributes:
   - respcd
   - respmsg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'respcd', None, None, ), # 1
    (2, TType.STRING, 'respmsg', None, None, ), # 2
  )

  def __init__(self, respcd=None, respmsg=None,):
    self.respcd = respcd
    self.respmsg = respmsg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.respcd = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.respmsg = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AuditException')
    if self.respcd is not None:
      oprot.writeFieldBegin('respcd', TType.STRING, 1)
      oprot.writeString(self.respcd)
      oprot.writeFieldEnd()
    if self.respmsg is not None:
      oprot.writeFieldBegin('respmsg', TType.STRING, 2)
      oprot.writeString(self.respmsg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.respcd)
    value = (value * 31) ^ hash(self.respmsg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Audit:
  """
  Attributes:
   - audit_type
   - userid
   - groupid
   - info
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'audit_type', None, None, ), # 1
    (2, TType.I64, 'userid', None, 0, ), # 2
    (3, TType.I64, 'groupid', None, 0, ), # 3
    (4, TType.STRING, 'info', None, None, ), # 4
  )

  def __init__(self, audit_type=None, userid=thrift_spec[2][4], groupid=thrift_spec[3][4], info=None,):
    self.audit_type = audit_type
    self.userid = userid
    self.groupid = groupid
    self.info = info

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.audit_type = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.userid = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.groupid = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.info = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Audit')
    if self.audit_type is not None:
      oprot.writeFieldBegin('audit_type', TType.STRING, 1)
      oprot.writeString(self.audit_type)
      oprot.writeFieldEnd()
    if self.userid is not None:
      oprot.writeFieldBegin('userid', TType.I64, 2)
      oprot.writeI64(self.userid)
      oprot.writeFieldEnd()
    if self.groupid is not None:
      oprot.writeFieldBegin('groupid', TType.I64, 3)
      oprot.writeI64(self.groupid)
      oprot.writeFieldEnd()
    if self.info is not None:
      oprot.writeFieldBegin('info', TType.STRING, 4)
      oprot.writeString(self.info)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.audit_type is None:
      raise TProtocol.TProtocolException(message='Required field audit_type is unset!')
    if self.userid is None:
      raise TProtocol.TProtocolException(message='Required field userid is unset!')
    if self.groupid is None:
      raise TProtocol.TProtocolException(message='Required field groupid is unset!')
    if self.info is None:
      raise TProtocol.TProtocolException(message='Required field info is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.audit_type)
    value = (value * 31) ^ hash(self.userid)
    value = (value * 31) ^ hash(self.groupid)
    value = (value * 31) ^ hash(self.info)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AppInfo:
  """
  Attributes:
   - appid
   - jsapipath
   - pay_appid
   - uid
   - cid
   - state
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'appid', None, None, ), # 1
    (2, TType.LIST, 'jsapipath', (TType.STRING,None), None, ), # 2
    (3, TType.STRING, 'pay_appid', None, "", ), # 3
    (4, TType.I64, 'uid', None, None, ), # 4
    (5, TType.STRING, 'cid', None, None, ), # 5
    (6, TType.I64, 'state', None, None, ), # 6
  )

  def __init__(self, appid=None, jsapipath=None, pay_appid=thrift_spec[3][4], uid=None, cid=None, state=None,):
    self.appid = appid
    self.jsapipath = jsapipath
    self.pay_appid = pay_appid
    self.uid = uid
    self.cid = cid
    self.state = state

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.appid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.jsapipath = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString()
            self.jsapipath.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.pay_appid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.uid = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.cid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.state = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AppInfo')
    if self.appid is not None:
      oprot.writeFieldBegin('appid', TType.STRING, 1)
      oprot.writeString(self.appid)
      oprot.writeFieldEnd()
    if self.jsapipath is not None:
      oprot.writeFieldBegin('jsapipath', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.jsapipath))
      for iter6 in self.jsapipath:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.pay_appid is not None:
      oprot.writeFieldBegin('pay_appid', TType.STRING, 3)
      oprot.writeString(self.pay_appid)
      oprot.writeFieldEnd()
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.I64, 4)
      oprot.writeI64(self.uid)
      oprot.writeFieldEnd()
    if self.cid is not None:
      oprot.writeFieldBegin('cid', TType.STRING, 5)
      oprot.writeString(self.cid)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I64, 6)
      oprot.writeI64(self.state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.appid is None:
      raise TProtocol.TProtocolException(message='Required field appid is unset!')
    if self.jsapipath is None:
      raise TProtocol.TProtocolException(message='Required field jsapipath is unset!')
    if self.pay_appid is None:
      raise TProtocol.TProtocolException(message='Required field pay_appid is unset!')
    if self.uid is None:
      raise TProtocol.TProtocolException(message='Required field uid is unset!')
    if self.cid is None:
      raise TProtocol.TProtocolException(message='Required field cid is unset!')
    if self.state is None:
      raise TProtocol.TProtocolException(message='Required field state is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appid)
    value = (value * 31) ^ hash(self.jsapipath)
    value = (value * 31) ^ hash(self.pay_appid)
    value = (value * 31) ^ hash(self.uid)
    value = (value * 31) ^ hash(self.cid)
    value = (value * 31) ^ hash(self.state)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)