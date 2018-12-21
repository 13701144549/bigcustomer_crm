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



class CustomerError(TException):
  """
  Attributes:
   - code
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'code', None, None, ), # 1
    (2, TType.STRING, 'msg', None, None, ), # 2
  )

  def __init__(self, code=None, msg=None,):
    self.code = code
    self.msg = msg

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
          self.code = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.msg = iprot.readString()
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
    oprot.writeStructBegin('CustomerError')
    if self.code is not None:
      oprot.writeFieldBegin('code', TType.STRING, 1)
      oprot.writeString(self.code)
      oprot.writeFieldEnd()
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 2)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.code)
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Profile:
  """
  Attributes:
   - user_id
   - nickname
   - avatar
   - signature
   - bgimageurl
   - gender
   - birthday
   - country
   - province
   - city
   - mobile
   - unionid
   - mark
   - create_time
   - update_time
   - openid
   - follow_time
   - follow_source
   - cname
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'user_id', None, None, ), # 1
    (2, TType.STRING, 'nickname', None, None, ), # 2
    (3, TType.STRING, 'avatar', None, None, ), # 3
    (4, TType.STRING, 'signature', None, None, ), # 4
    (5, TType.STRING, 'bgimageurl', None, None, ), # 5
    (6, TType.BYTE, 'gender', None, None, ), # 6
    (7, TType.STRING, 'birthday', None, None, ), # 7
    (8, TType.STRING, 'country', None, None, ), # 8
    (9, TType.STRING, 'province', None, None, ), # 9
    (10, TType.STRING, 'city', None, None, ), # 10
    (11, TType.STRING, 'mobile', None, None, ), # 11
    (12, TType.STRING, 'unionid', None, None, ), # 12
    (13, TType.BYTE, 'mark', None, None, ), # 13
    (14, TType.STRING, 'create_time', None, None, ), # 14
    (15, TType.STRING, 'update_time', None, None, ), # 15
    (16, TType.STRING, 'openid', None, None, ), # 16
    (17, TType.STRING, 'follow_time', None, None, ), # 17
    (18, TType.STRING, 'follow_source', None, None, ), # 18
    (19, TType.STRING, 'cname', None, None, ), # 19
  )

  def __init__(self, user_id=None, nickname=None, avatar=None, signature=None, bgimageurl=None, gender=None, birthday=None, country=None, province=None, city=None, mobile=None, unionid=None, mark=None, create_time=None, update_time=None, openid=None, follow_time=None, follow_source=None, cname=None,):
    self.user_id = user_id
    self.nickname = nickname
    self.avatar = avatar
    self.signature = signature
    self.bgimageurl = bgimageurl
    self.gender = gender
    self.birthday = birthday
    self.country = country
    self.province = province
    self.city = city
    self.mobile = mobile
    self.unionid = unionid
    self.mark = mark
    self.create_time = create_time
    self.update_time = update_time
    self.openid = openid
    self.follow_time = follow_time
    self.follow_source = follow_source
    self.cname = cname

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
        if ftype == TType.I32:
          self.user_id = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.nickname = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.avatar = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.signature = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.bgimageurl = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BYTE:
          self.gender = iprot.readByte()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.birthday = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.country = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.province = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.city = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.mobile = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.STRING:
          self.unionid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.BYTE:
          self.mark = iprot.readByte()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.create_time = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.STRING:
          self.update_time = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.STRING:
          self.openid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.follow_time = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 18:
        if ftype == TType.STRING:
          self.follow_source = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 19:
        if ftype == TType.STRING:
          self.cname = iprot.readString()
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
    oprot.writeStructBegin('Profile')
    if self.user_id is not None:
      oprot.writeFieldBegin('user_id', TType.I32, 1)
      oprot.writeI32(self.user_id)
      oprot.writeFieldEnd()
    if self.nickname is not None:
      oprot.writeFieldBegin('nickname', TType.STRING, 2)
      oprot.writeString(self.nickname)
      oprot.writeFieldEnd()
    if self.avatar is not None:
      oprot.writeFieldBegin('avatar', TType.STRING, 3)
      oprot.writeString(self.avatar)
      oprot.writeFieldEnd()
    if self.signature is not None:
      oprot.writeFieldBegin('signature', TType.STRING, 4)
      oprot.writeString(self.signature)
      oprot.writeFieldEnd()
    if self.bgimageurl is not None:
      oprot.writeFieldBegin('bgimageurl', TType.STRING, 5)
      oprot.writeString(self.bgimageurl)
      oprot.writeFieldEnd()
    if self.gender is not None:
      oprot.writeFieldBegin('gender', TType.BYTE, 6)
      oprot.writeByte(self.gender)
      oprot.writeFieldEnd()
    if self.birthday is not None:
      oprot.writeFieldBegin('birthday', TType.STRING, 7)
      oprot.writeString(self.birthday)
      oprot.writeFieldEnd()
    if self.country is not None:
      oprot.writeFieldBegin('country', TType.STRING, 8)
      oprot.writeString(self.country)
      oprot.writeFieldEnd()
    if self.province is not None:
      oprot.writeFieldBegin('province', TType.STRING, 9)
      oprot.writeString(self.province)
      oprot.writeFieldEnd()
    if self.city is not None:
      oprot.writeFieldBegin('city', TType.STRING, 10)
      oprot.writeString(self.city)
      oprot.writeFieldEnd()
    if self.mobile is not None:
      oprot.writeFieldBegin('mobile', TType.STRING, 11)
      oprot.writeString(self.mobile)
      oprot.writeFieldEnd()
    if self.unionid is not None:
      oprot.writeFieldBegin('unionid', TType.STRING, 12)
      oprot.writeString(self.unionid)
      oprot.writeFieldEnd()
    if self.mark is not None:
      oprot.writeFieldBegin('mark', TType.BYTE, 13)
      oprot.writeByte(self.mark)
      oprot.writeFieldEnd()
    if self.create_time is not None:
      oprot.writeFieldBegin('create_time', TType.STRING, 14)
      oprot.writeString(self.create_time)
      oprot.writeFieldEnd()
    if self.update_time is not None:
      oprot.writeFieldBegin('update_time', TType.STRING, 15)
      oprot.writeString(self.update_time)
      oprot.writeFieldEnd()
    if self.openid is not None:
      oprot.writeFieldBegin('openid', TType.STRING, 16)
      oprot.writeString(self.openid)
      oprot.writeFieldEnd()
    if self.follow_time is not None:
      oprot.writeFieldBegin('follow_time', TType.STRING, 17)
      oprot.writeString(self.follow_time)
      oprot.writeFieldEnd()
    if self.follow_source is not None:
      oprot.writeFieldBegin('follow_source', TType.STRING, 18)
      oprot.writeString(self.follow_source)
      oprot.writeFieldEnd()
    if self.cname is not None:
      oprot.writeFieldBegin('cname', TType.STRING, 19)
      oprot.writeString(self.cname)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.follow_time is None:
      raise TProtocol.TProtocolException(message='Required field follow_time is unset!')
    if self.follow_source is None:
      raise TProtocol.TProtocolException(message='Required field follow_source is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.user_id)
    value = (value * 31) ^ hash(self.nickname)
    value = (value * 31) ^ hash(self.avatar)
    value = (value * 31) ^ hash(self.signature)
    value = (value * 31) ^ hash(self.bgimageurl)
    value = (value * 31) ^ hash(self.gender)
    value = (value * 31) ^ hash(self.birthday)
    value = (value * 31) ^ hash(self.country)
    value = (value * 31) ^ hash(self.province)
    value = (value * 31) ^ hash(self.city)
    value = (value * 31) ^ hash(self.mobile)
    value = (value * 31) ^ hash(self.unionid)
    value = (value * 31) ^ hash(self.mark)
    value = (value * 31) ^ hash(self.create_time)
    value = (value * 31) ^ hash(self.update_time)
    value = (value * 31) ^ hash(self.openid)
    value = (value * 31) ^ hash(self.follow_time)
    value = (value * 31) ^ hash(self.follow_source)
    value = (value * 31) ^ hash(self.cname)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LoginRecord:
  """
  Attributes:
   - ip
   - user_agent
   - longitude
   - latitude
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'ip', None, None, ), # 1
    (2, TType.STRING, 'user_agent', None, None, ), # 2
    (3, TType.DOUBLE, 'longitude', None, None, ), # 3
    (4, TType.DOUBLE, 'latitude', None, None, ), # 4
  )

  def __init__(self, ip=None, user_agent=None, longitude=None, latitude=None,):
    self.ip = ip
    self.user_agent = user_agent
    self.longitude = longitude
    self.latitude = latitude

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
          self.ip = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.user_agent = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.longitude = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.latitude = iprot.readDouble()
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
    oprot.writeStructBegin('LoginRecord')
    if self.ip is not None:
      oprot.writeFieldBegin('ip', TType.STRING, 1)
      oprot.writeString(self.ip)
      oprot.writeFieldEnd()
    if self.user_agent is not None:
      oprot.writeFieldBegin('user_agent', TType.STRING, 2)
      oprot.writeString(self.user_agent)
      oprot.writeFieldEnd()
    if self.longitude is not None:
      oprot.writeFieldBegin('longitude', TType.DOUBLE, 3)
      oprot.writeDouble(self.longitude)
      oprot.writeFieldEnd()
    if self.latitude is not None:
      oprot.writeFieldBegin('latitude', TType.DOUBLE, 4)
      oprot.writeDouble(self.latitude)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ip)
    value = (value * 31) ^ hash(self.user_agent)
    value = (value * 31) ^ hash(self.longitude)
    value = (value * 31) ^ hash(self.latitude)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LoginResult:
  """
  Attributes:
   - error_code
   - profile
   - app_local_newly_registered
   - global_newly_registered
  """

  thrift_spec = (
    None, # 0
    (1, TType.BYTE, 'error_code', None, None, ), # 1
    (2, TType.STRUCT, 'profile', (Profile, Profile.thrift_spec), None, ), # 2
    (3, TType.BOOL, 'app_local_newly_registered', None, None, ), # 3
    (4, TType.BOOL, 'global_newly_registered', None, None, ), # 4
  )

  def __init__(self, error_code=None, profile=None, app_local_newly_registered=None, global_newly_registered=None,):
    self.error_code = error_code
    self.profile = profile
    self.app_local_newly_registered = app_local_newly_registered
    self.global_newly_registered = global_newly_registered

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
        if ftype == TType.BYTE:
          self.error_code = iprot.readByte()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.profile = Profile()
          self.profile.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.app_local_newly_registered = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.global_newly_registered = iprot.readBool()
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
    oprot.writeStructBegin('LoginResult')
    if self.error_code is not None:
      oprot.writeFieldBegin('error_code', TType.BYTE, 1)
      oprot.writeByte(self.error_code)
      oprot.writeFieldEnd()
    if self.profile is not None:
      oprot.writeFieldBegin('profile', TType.STRUCT, 2)
      self.profile.write(oprot)
      oprot.writeFieldEnd()
    if self.app_local_newly_registered is not None:
      oprot.writeFieldBegin('app_local_newly_registered', TType.BOOL, 3)
      oprot.writeBool(self.app_local_newly_registered)
      oprot.writeFieldEnd()
    if self.global_newly_registered is not None:
      oprot.writeFieldBegin('global_newly_registered', TType.BOOL, 4)
      oprot.writeBool(self.global_newly_registered)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.error_code)
    value = (value * 31) ^ hash(self.profile)
    value = (value * 31) ^ hash(self.app_local_newly_registered)
    value = (value * 31) ^ hash(self.global_newly_registered)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class App:
  """
  Attributes:
   - appid
   - name
   - status
   - id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'appid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I16, 'status', None, None, ), # 3
    (4, TType.I64, 'id', None, None, ), # 4
  )

  def __init__(self, appid=None, name=None, status=None, id=None,):
    self.appid = appid
    self.name = name
    self.status = status
    self.id = id

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
        if ftype == TType.STRING:
          self.name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.status = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.id = iprot.readI64()
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
    oprot.writeStructBegin('App')
    if self.appid is not None:
      oprot.writeFieldBegin('appid', TType.STRING, 1)
      oprot.writeString(self.appid)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I16, 3)
      oprot.writeI16(self.status)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 4)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AppQuery:
  """
  Attributes:
   - id
   - appid
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.STRING, 'appid', None, None, ), # 2
  )

  def __init__(self, id=None, appid=None,):
    self.id = id
    self.appid = appid

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
        if ftype == TType.I32:
          self.id = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.appid = iprot.readString()
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
    oprot.writeStructBegin('AppQuery')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.appid is not None:
      oprot.writeFieldBegin('appid', TType.STRING, 2)
      oprot.writeString(self.appid)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.appid)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class WXCustomer:
  """
  Attributes:
   - appid
   - wx_appid
   - openid
   - follow_first_time
   - follow_source
   - follow_status
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'appid', None, None, ), # 1
    (2, TType.STRING, 'wx_appid', None, None, ), # 2
    (3, TType.STRING, 'openid', None, None, ), # 3
    (4, TType.STRING, 'follow_first_time', None, None, ), # 4
    (5, TType.STRING, 'follow_source', None, None, ), # 5
    (6, TType.STRING, 'follow_status', None, None, ), # 6
  )

  def __init__(self, appid=None, wx_appid=None, openid=None, follow_first_time=None, follow_source=None, follow_status=None,):
    self.appid = appid
    self.wx_appid = wx_appid
    self.openid = openid
    self.follow_first_time = follow_first_time
    self.follow_source = follow_source
    self.follow_status = follow_status

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
        if ftype == TType.I32:
          self.appid = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.wx_appid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.openid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.follow_first_time = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.follow_source = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.follow_status = iprot.readString()
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
    oprot.writeStructBegin('WXCustomer')
    if self.appid is not None:
      oprot.writeFieldBegin('appid', TType.I32, 1)
      oprot.writeI32(self.appid)
      oprot.writeFieldEnd()
    if self.wx_appid is not None:
      oprot.writeFieldBegin('wx_appid', TType.STRING, 2)
      oprot.writeString(self.wx_appid)
      oprot.writeFieldEnd()
    if self.openid is not None:
      oprot.writeFieldBegin('openid', TType.STRING, 3)
      oprot.writeString(self.openid)
      oprot.writeFieldEnd()
    if self.follow_first_time is not None:
      oprot.writeFieldBegin('follow_first_time', TType.STRING, 4)
      oprot.writeString(self.follow_first_time)
      oprot.writeFieldEnd()
    if self.follow_source is not None:
      oprot.writeFieldBegin('follow_source', TType.STRING, 5)
      oprot.writeString(self.follow_source)
      oprot.writeFieldEnd()
    if self.follow_status is not None:
      oprot.writeFieldBegin('follow_status', TType.STRING, 6)
      oprot.writeString(self.follow_status)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appid)
    value = (value * 31) ^ hash(self.wx_appid)
    value = (value * 31) ^ hash(self.openid)
    value = (value * 31) ^ hash(self.follow_first_time)
    value = (value * 31) ^ hash(self.follow_source)
    value = (value * 31) ^ hash(self.follow_status)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
