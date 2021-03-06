# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Rank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Rank.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nRank.proto\"U\n\x11VO_SimpleRoleInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ntotalPower\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x0f\n\x07imageId\x18\x04 \x01(\x05\"M\n\x07VO_Rank\x12\x0e\n\x06rankId\x18\x01 \x01(\x05\x12$\n\x08roleList\x18\x02 \x03(\x0b\x32\x12.VO_SimpleRoleInfo\x12\x0c\n\x04rank\x18\x03 \x01(\x05\"\r\n\x0b\x43S_RankList\")\n\x0bSC_RankList\x12\x1a\n\x08rankList\x18\x01 \x03(\x0b\x32\x08.VO_Rank**\n\x08RankType\x12\x0e\n\nPOWER_RANK\x10\x01\x12\x0e\n\nLEVEL_RANK\x10\x02*<\n\x0cRankTimeType\x12\r\n\tTIME_SLOT\x10\x01\x12\r\n\tTIME_WEEK\x10\x02\x12\x0e\n\nTIME_MONTH\x10\x03* \n\tRankState\x12\x08\n\x04OPEN\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\x42\x32\n$com.fanxing.server.io.proto.protocolB\nRankProtos')
)

_RANKTYPE = _descriptor.EnumDescriptor(
  name='RankType',
  full_name='RankType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POWER_RANK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_RANK', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=238,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_RANKTYPE)

RankType = enum_type_wrapper.EnumTypeWrapper(_RANKTYPE)
_RANKTIMETYPE = _descriptor.EnumDescriptor(
  name='RankTimeType',
  full_name='RankTimeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TIME_SLOT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_WEEK', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_MONTH', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=282,
  serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_RANKTIMETYPE)

RankTimeType = enum_type_wrapper.EnumTypeWrapper(_RANKTIMETYPE)
_RANKSTATE = _descriptor.EnumDescriptor(
  name='RankState',
  full_name='RankState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=344,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_RANKSTATE)

RankState = enum_type_wrapper.EnumTypeWrapper(_RANKSTATE)
POWER_RANK = 1
LEVEL_RANK = 2
TIME_SLOT = 1
TIME_WEEK = 2
TIME_MONTH = 3
OPEN = 1
CLOSE = 2



_VO_SIMPLEROLEINFO = _descriptor.Descriptor(
  name='VO_SimpleRoleInfo',
  full_name='VO_SimpleRoleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='VO_SimpleRoleInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalPower', full_name='VO_SimpleRoleInfo.totalPower', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='VO_SimpleRoleInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageId', full_name='VO_SimpleRoleInfo.imageId', index=3,
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
  serialized_start=14,
  serialized_end=99,
)


_VO_RANK = _descriptor.Descriptor(
  name='VO_Rank',
  full_name='VO_Rank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rankId', full_name='VO_Rank.rankId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleList', full_name='VO_Rank.roleList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='VO_Rank.rank', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=101,
  serialized_end=178,
)


_CS_RANKLIST = _descriptor.Descriptor(
  name='CS_RankList',
  full_name='CS_RankList',
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
  serialized_start=180,
  serialized_end=193,
)


_SC_RANKLIST = _descriptor.Descriptor(
  name='SC_RankList',
  full_name='SC_RankList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rankList', full_name='SC_RankList.rankList', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=195,
  serialized_end=236,
)

_VO_RANK.fields_by_name['roleList'].message_type = _VO_SIMPLEROLEINFO
_SC_RANKLIST.fields_by_name['rankList'].message_type = _VO_RANK
DESCRIPTOR.message_types_by_name['VO_SimpleRoleInfo'] = _VO_SIMPLEROLEINFO
DESCRIPTOR.message_types_by_name['VO_Rank'] = _VO_RANK
DESCRIPTOR.message_types_by_name['CS_RankList'] = _CS_RANKLIST
DESCRIPTOR.message_types_by_name['SC_RankList'] = _SC_RANKLIST
DESCRIPTOR.enum_types_by_name['RankType'] = _RANKTYPE
DESCRIPTOR.enum_types_by_name['RankTimeType'] = _RANKTIMETYPE
DESCRIPTOR.enum_types_by_name['RankState'] = _RANKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VO_SimpleRoleInfo = _reflection.GeneratedProtocolMessageType('VO_SimpleRoleInfo', (_message.Message,), dict(
  DESCRIPTOR = _VO_SIMPLEROLEINFO,
  __module__ = 'Rank_pb2'
  # @@protoc_insertion_point(class_scope:VO_SimpleRoleInfo)
  ))
_sym_db.RegisterMessage(VO_SimpleRoleInfo)

VO_Rank = _reflection.GeneratedProtocolMessageType('VO_Rank', (_message.Message,), dict(
  DESCRIPTOR = _VO_RANK,
  __module__ = 'Rank_pb2'
  # @@protoc_insertion_point(class_scope:VO_Rank)
  ))
_sym_db.RegisterMessage(VO_Rank)

CS_RankList = _reflection.GeneratedProtocolMessageType('CS_RankList', (_message.Message,), dict(
  DESCRIPTOR = _CS_RANKLIST,
  __module__ = 'Rank_pb2'
  # @@protoc_insertion_point(class_scope:CS_RankList)
  ))
_sym_db.RegisterMessage(CS_RankList)

SC_RankList = _reflection.GeneratedProtocolMessageType('SC_RankList', (_message.Message,), dict(
  DESCRIPTOR = _SC_RANKLIST,
  __module__ = 'Rank_pb2'
  # @@protoc_insertion_point(class_scope:SC_RankList)
  ))
_sym_db.RegisterMessage(SC_RankList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\nRankProtos'))
# @@protoc_insertion_point(module_scope)
