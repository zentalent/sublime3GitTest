# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SignIn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Struct_pb2 as Struct__pb2
import Role_pb2 as Role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SignIn.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0cSignIn.proto\x1a\x0c\x43ommon.proto\x1a\x0cStruct.proto\x1a\nRole.proto\"S\n\nVO_BoxInfo\x12\x10\n\x08rewardId\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ys\x18\x02 \x02(\x05\x12\x13\n\x0bisGetReward\x18\x03 \x02(\x08\x12\x10\n\x08imageKey\x18\x04 \x01(\x05\"i\n\x0fVO_SignInReward\x12\x1d\n\x07rewards\x18\x01 \x02(\x0b\x32\x0c.VO_Supplies\x12\x1a\n\x0e\x64\x65mandVipLevel\x18\x02 \x01(\x05:\x02-1\x12\x1b\n\x10VIPMultipleTimes\x18\x03 \x01(\x05:\x01\x32\"f\n\x0eVO_LoginReward\x12\x10\n\x08rewardId\x18\x01 \x02(\x05\x12\x10\n\x08obtainId\x18\x02 \x02(\x05\x12\x0f\n\x07\x63\x65\x61seId\x18\x03 \x02(\x05\x12\x10\n\x08itemName\x18\x04 \x02(\t\x12\r\n\x05picId\x18\x05 \x01(\x05\"\x12\n\x10\x43S_GetSignInInfo\"%\n\tCS_SignIn\x12\x18\n\x10\x61\x63\x63umulativeDays\x18\x01 \x02(\x05\"\x17\n\x15\x43S_GetLoginRewardInfo\"*\n\x0e\x43S_LoginReward\x12\x18\n\x10\x61\x63\x63umulativeDays\x18\x01 \x02(\x05\"\x15\n\x13\x43S_GetLoginStarInfo\"(\n\x0c\x43S_LoginStar\x12\x18\n\x10\x61\x63\x63umulativeDays\x18\x01 \x02(\x05\"(\n\x0c\x43S_BoxReward\x12\x18\n\x10\x61\x63\x63umulativeDays\x18\x01 \x02(\x05\"\x9c\x01\n\x10SC_GetSignInInfo\x12\r\n\x05month\x18\x01 \x02(\x05\x12\x15\n\risTodaySigned\x18\x02 \x02(\x08\x12\x18\n\x10\x61\x63\x63umuSignedDays\x18\x03 \x02(\x05\x12!\n\x0c\x62oxInfoLists\x18\x04 \x03(\x0b\x32\x0b.VO_BoxInfo\x12%\n\x0brewardLists\x18\x05 \x03(\x0b\x32\x10.VO_SignInReward\"n\n\x15SC_GetLoginRewardInfo\x12\x15\n\risTodaySigned\x18\x01 \x02(\x08\x12\x18\n\x10\x61\x63\x63umuSignedDays\x18\x02 \x02(\x05\x12$\n\x0brewardLists\x18\x03 \x03(\x0b\x32\x0f.VO_LoginReward\"F\n\x13SC_GetLoginStarInfo\x12\x15\n\risTodaySigned\x18\x01 \x02(\x08\x12\x18\n\x10\x61\x63\x63umuSignedDays\x18\x02 \x02(\x05\x42\x34\n$com.fanxing.server.io.proto.protocolB\x0cSignInProtos')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Struct__pb2.DESCRIPTOR,Role__pb2.DESCRIPTOR,])




_VO_BOXINFO = _descriptor.Descriptor(
  name='VO_BoxInfo',
  full_name='VO_BoxInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardId', full_name='VO_BoxInfo.rewardId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days', full_name='VO_BoxInfo.days', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isGetReward', full_name='VO_BoxInfo.isGetReward', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageKey', full_name='VO_BoxInfo.imageKey', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=139,
)


_VO_SIGNINREWARD = _descriptor.Descriptor(
  name='VO_SignInReward',
  full_name='VO_SignInReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='VO_SignInReward.rewards', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demandVipLevel', full_name='VO_SignInReward.demandVipLevel', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='VIPMultipleTimes', full_name='VO_SignInReward.VIPMultipleTimes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=246,
)


_VO_LOGINREWARD = _descriptor.Descriptor(
  name='VO_LoginReward',
  full_name='VO_LoginReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewardId', full_name='VO_LoginReward.rewardId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obtainId', full_name='VO_LoginReward.obtainId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ceaseId', full_name='VO_LoginReward.ceaseId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemName', full_name='VO_LoginReward.itemName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='picId', full_name='VO_LoginReward.picId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=350,
)


_CS_GETSIGNININFO = _descriptor.Descriptor(
  name='CS_GetSignInInfo',
  full_name='CS_GetSignInInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=370,
)


_CS_SIGNIN = _descriptor.Descriptor(
  name='CS_SignIn',
  full_name='CS_SignIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulativeDays', full_name='CS_SignIn.accumulativeDays', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=409,
)


_CS_GETLOGINREWARDINFO = _descriptor.Descriptor(
  name='CS_GetLoginRewardInfo',
  full_name='CS_GetLoginRewardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=434,
)


_CS_LOGINREWARD = _descriptor.Descriptor(
  name='CS_LoginReward',
  full_name='CS_LoginReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulativeDays', full_name='CS_LoginReward.accumulativeDays', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=478,
)


_CS_GETLOGINSTARINFO = _descriptor.Descriptor(
  name='CS_GetLoginStarInfo',
  full_name='CS_GetLoginStarInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=501,
)


_CS_LOGINSTAR = _descriptor.Descriptor(
  name='CS_LoginStar',
  full_name='CS_LoginStar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulativeDays', full_name='CS_LoginStar.accumulativeDays', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=543,
)


_CS_BOXREWARD = _descriptor.Descriptor(
  name='CS_BoxReward',
  full_name='CS_BoxReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulativeDays', full_name='CS_BoxReward.accumulativeDays', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=585,
)


_SC_GETSIGNININFO = _descriptor.Descriptor(
  name='SC_GetSignInInfo',
  full_name='SC_GetSignInInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='month', full_name='SC_GetSignInInfo.month', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isTodaySigned', full_name='SC_GetSignInInfo.isTodaySigned', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accumuSignedDays', full_name='SC_GetSignInInfo.accumuSignedDays', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boxInfoLists', full_name='SC_GetSignInInfo.boxInfoLists', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewardLists', full_name='SC_GetSignInInfo.rewardLists', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=744,
)


_SC_GETLOGINREWARDINFO = _descriptor.Descriptor(
  name='SC_GetLoginRewardInfo',
  full_name='SC_GetLoginRewardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isTodaySigned', full_name='SC_GetLoginRewardInfo.isTodaySigned', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accumuSignedDays', full_name='SC_GetLoginRewardInfo.accumuSignedDays', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewardLists', full_name='SC_GetLoginRewardInfo.rewardLists', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=746,
  serialized_end=856,
)


_SC_GETLOGINSTARINFO = _descriptor.Descriptor(
  name='SC_GetLoginStarInfo',
  full_name='SC_GetLoginStarInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isTodaySigned', full_name='SC_GetLoginStarInfo.isTodaySigned', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accumuSignedDays', full_name='SC_GetLoginStarInfo.accumuSignedDays', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=928,
)

_VO_SIGNINREWARD.fields_by_name['rewards'].message_type = Struct__pb2._VO_SUPPLIES
_SC_GETSIGNININFO.fields_by_name['boxInfoLists'].message_type = _VO_BOXINFO
_SC_GETSIGNININFO.fields_by_name['rewardLists'].message_type = _VO_SIGNINREWARD
_SC_GETLOGINREWARDINFO.fields_by_name['rewardLists'].message_type = _VO_LOGINREWARD
DESCRIPTOR.message_types_by_name['VO_BoxInfo'] = _VO_BOXINFO
DESCRIPTOR.message_types_by_name['VO_SignInReward'] = _VO_SIGNINREWARD
DESCRIPTOR.message_types_by_name['VO_LoginReward'] = _VO_LOGINREWARD
DESCRIPTOR.message_types_by_name['CS_GetSignInInfo'] = _CS_GETSIGNININFO
DESCRIPTOR.message_types_by_name['CS_SignIn'] = _CS_SIGNIN
DESCRIPTOR.message_types_by_name['CS_GetLoginRewardInfo'] = _CS_GETLOGINREWARDINFO
DESCRIPTOR.message_types_by_name['CS_LoginReward'] = _CS_LOGINREWARD
DESCRIPTOR.message_types_by_name['CS_GetLoginStarInfo'] = _CS_GETLOGINSTARINFO
DESCRIPTOR.message_types_by_name['CS_LoginStar'] = _CS_LOGINSTAR
DESCRIPTOR.message_types_by_name['CS_BoxReward'] = _CS_BOXREWARD
DESCRIPTOR.message_types_by_name['SC_GetSignInInfo'] = _SC_GETSIGNININFO
DESCRIPTOR.message_types_by_name['SC_GetLoginRewardInfo'] = _SC_GETLOGINREWARDINFO
DESCRIPTOR.message_types_by_name['SC_GetLoginStarInfo'] = _SC_GETLOGINSTARINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VO_BoxInfo = _reflection.GeneratedProtocolMessageType('VO_BoxInfo', (_message.Message,), dict(
  DESCRIPTOR = _VO_BOXINFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:VO_BoxInfo)
  ))
_sym_db.RegisterMessage(VO_BoxInfo)

VO_SignInReward = _reflection.GeneratedProtocolMessageType('VO_SignInReward', (_message.Message,), dict(
  DESCRIPTOR = _VO_SIGNINREWARD,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:VO_SignInReward)
  ))
_sym_db.RegisterMessage(VO_SignInReward)

VO_LoginReward = _reflection.GeneratedProtocolMessageType('VO_LoginReward', (_message.Message,), dict(
  DESCRIPTOR = _VO_LOGINREWARD,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:VO_LoginReward)
  ))
_sym_db.RegisterMessage(VO_LoginReward)

CS_GetSignInInfo = _reflection.GeneratedProtocolMessageType('CS_GetSignInInfo', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETSIGNININFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetSignInInfo)
  ))
_sym_db.RegisterMessage(CS_GetSignInInfo)

CS_SignIn = _reflection.GeneratedProtocolMessageType('CS_SignIn', (_message.Message,), dict(
  DESCRIPTOR = _CS_SIGNIN,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_SignIn)
  ))
_sym_db.RegisterMessage(CS_SignIn)

CS_GetLoginRewardInfo = _reflection.GeneratedProtocolMessageType('CS_GetLoginRewardInfo', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETLOGINREWARDINFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetLoginRewardInfo)
  ))
_sym_db.RegisterMessage(CS_GetLoginRewardInfo)

CS_LoginReward = _reflection.GeneratedProtocolMessageType('CS_LoginReward', (_message.Message,), dict(
  DESCRIPTOR = _CS_LOGINREWARD,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_LoginReward)
  ))
_sym_db.RegisterMessage(CS_LoginReward)

CS_GetLoginStarInfo = _reflection.GeneratedProtocolMessageType('CS_GetLoginStarInfo', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETLOGINSTARINFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetLoginStarInfo)
  ))
_sym_db.RegisterMessage(CS_GetLoginStarInfo)

CS_LoginStar = _reflection.GeneratedProtocolMessageType('CS_LoginStar', (_message.Message,), dict(
  DESCRIPTOR = _CS_LOGINSTAR,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_LoginStar)
  ))
_sym_db.RegisterMessage(CS_LoginStar)

CS_BoxReward = _reflection.GeneratedProtocolMessageType('CS_BoxReward', (_message.Message,), dict(
  DESCRIPTOR = _CS_BOXREWARD,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:CS_BoxReward)
  ))
_sym_db.RegisterMessage(CS_BoxReward)

SC_GetSignInInfo = _reflection.GeneratedProtocolMessageType('SC_GetSignInInfo', (_message.Message,), dict(
  DESCRIPTOR = _SC_GETSIGNININFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:SC_GetSignInInfo)
  ))
_sym_db.RegisterMessage(SC_GetSignInInfo)

SC_GetLoginRewardInfo = _reflection.GeneratedProtocolMessageType('SC_GetLoginRewardInfo', (_message.Message,), dict(
  DESCRIPTOR = _SC_GETLOGINREWARDINFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:SC_GetLoginRewardInfo)
  ))
_sym_db.RegisterMessage(SC_GetLoginRewardInfo)

SC_GetLoginStarInfo = _reflection.GeneratedProtocolMessageType('SC_GetLoginStarInfo', (_message.Message,), dict(
  DESCRIPTOR = _SC_GETLOGINSTARINFO,
  __module__ = 'SignIn_pb2'
  # @@protoc_insertion_point(class_scope:SC_GetLoginStarInfo)
  ))
_sym_db.RegisterMessage(SC_GetLoginStarInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\014SignInProtos'))
# @@protoc_insertion_point(module_scope)