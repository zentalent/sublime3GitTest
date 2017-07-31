# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Gacha.proto

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


import Struct_pb2 as Struct__pb2
import Role_pb2 as Role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Gacha.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bGacha.proto\x1a\x0cStruct.proto\x1a\nRole.proto\"5\n\x08\x43S_Gacha\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x1d\n\tgachaType\x18\x02 \x02(\x0e\x32\n.GachaType\"A\n\x0f\x43S_GetGachaData\x12\x0e\n\x02id\x18\x01 \x01(\x05:\x02-1\x12\x1e\n\ngachaTypes\x18\x02 \x03(\x0e\x32\n.GachaType\"!\n\x11\x43S_GachaCommander\x12\x0c\n\x04type\x18\x01 \x02(\x05\",\n\x18\x43S_GetGachaCommanderData\x12\x10\n\x04type\x18\x01 \x01(\x05:\x02-1\"Q\n\x08SC_Gacha\x12\x1d\n\x07rewards\x18\x01 \x03(\x0b\x32\x0c.VO_Supplies\x12&\n\x0eupdateRoleInfo\x18\x02 \x02(\x0b\x32\x0e.VO_RoleUpdate\"Q\n\x0fSC_GetGachaData\x12\x1c\n\x05infos\x18\x01 \x03(\x0b\x32\r.VO_GachaData\x12 \n\x07soulBox\x18\x02 \x01(\x0b\x32\x0f.VO_SoulBoxData\"T\n\x0cVO_GachaData\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x11\n\x05\x63ount\x18\x02 \x01(\x05:\x02-1\x12\x0e\n\x02\x63\x64\x18\x03 \x01(\x05:\x02-1\x12\x13\n\x07spTimes\x18\x04 \x01(\x05:\x02-1\"C\n\x0eVO_SoulBoxData\x12\x0e\n\x06mainId\x18\x01 \x02(\x05\x12\x10\n\x08tankName\x18\x02 \x02(\t\x12\x0f\n\x07hotspot\x18\x03 \x03(\x05*@\n\tGachaType\x12\r\n\tGT_Supply\x10\x01\x12\x14\n\x10GT_SupportWeapon\x10\x02\x12\x0e\n\nGT_SoulBox\x10\x03\x42\x33\n$com.fanxing.server.io.proto.protocolB\x0bGachaProtos')
  ,
  dependencies=[Struct__pb2.DESCRIPTOR,Role__pb2.DESCRIPTOR,])

_GACHATYPE = _descriptor.EnumDescriptor(
  name='GachaType',
  full_name='GachaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GT_Supply', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GT_SupportWeapon', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GT_SoulBox', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=565,
  serialized_end=629,
)
_sym_db.RegisterEnumDescriptor(_GACHATYPE)

GachaType = enum_type_wrapper.EnumTypeWrapper(_GACHATYPE)
GT_Supply = 1
GT_SupportWeapon = 2
GT_SoulBox = 3



_CS_GACHA = _descriptor.Descriptor(
  name='CS_Gacha',
  full_name='CS_Gacha',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CS_Gacha.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gachaType', full_name='CS_Gacha.gachaType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=41,
  serialized_end=94,
)


_CS_GETGACHADATA = _descriptor.Descriptor(
  name='CS_GetGachaData',
  full_name='CS_GetGachaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CS_GetGachaData.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gachaTypes', full_name='CS_GetGachaData.gachaTypes', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  serialized_start=96,
  serialized_end=161,
)


_CS_GACHACOMMANDER = _descriptor.Descriptor(
  name='CS_GachaCommander',
  full_name='CS_GachaCommander',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CS_GachaCommander.type', index=0,
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
  serialized_start=163,
  serialized_end=196,
)


_CS_GETGACHACOMMANDERDATA = _descriptor.Descriptor(
  name='CS_GetGachaCommanderData',
  full_name='CS_GetGachaCommanderData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CS_GetGachaCommanderData.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
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
  serialized_start=198,
  serialized_end=242,
)


_SC_GACHA = _descriptor.Descriptor(
  name='SC_Gacha',
  full_name='SC_Gacha',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='SC_Gacha.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updateRoleInfo', full_name='SC_Gacha.updateRoleInfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=244,
  serialized_end=325,
)


_SC_GETGACHADATA = _descriptor.Descriptor(
  name='SC_GetGachaData',
  full_name='SC_GetGachaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infos', full_name='SC_GetGachaData.infos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soulBox', full_name='SC_GetGachaData.soulBox', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=327,
  serialized_end=408,
)


_VO_GACHADATA = _descriptor.Descriptor(
  name='VO_GachaData',
  full_name='VO_GachaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='VO_GachaData.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='VO_GachaData.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cd', full_name='VO_GachaData.cd', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spTimes', full_name='VO_GachaData.spTimes', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
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
  serialized_start=410,
  serialized_end=494,
)


_VO_SOULBOXDATA = _descriptor.Descriptor(
  name='VO_SoulBoxData',
  full_name='VO_SoulBoxData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mainId', full_name='VO_SoulBoxData.mainId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tankName', full_name='VO_SoulBoxData.tankName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hotspot', full_name='VO_SoulBoxData.hotspot', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=496,
  serialized_end=563,
)

_CS_GACHA.fields_by_name['gachaType'].enum_type = _GACHATYPE
_CS_GETGACHADATA.fields_by_name['gachaTypes'].enum_type = _GACHATYPE
_SC_GACHA.fields_by_name['rewards'].message_type = Struct__pb2._VO_SUPPLIES
_SC_GACHA.fields_by_name['updateRoleInfo'].message_type = Role__pb2._VO_ROLEUPDATE
_SC_GETGACHADATA.fields_by_name['infos'].message_type = _VO_GACHADATA
_SC_GETGACHADATA.fields_by_name['soulBox'].message_type = _VO_SOULBOXDATA
DESCRIPTOR.message_types_by_name['CS_Gacha'] = _CS_GACHA
DESCRIPTOR.message_types_by_name['CS_GetGachaData'] = _CS_GETGACHADATA
DESCRIPTOR.message_types_by_name['CS_GachaCommander'] = _CS_GACHACOMMANDER
DESCRIPTOR.message_types_by_name['CS_GetGachaCommanderData'] = _CS_GETGACHACOMMANDERDATA
DESCRIPTOR.message_types_by_name['SC_Gacha'] = _SC_GACHA
DESCRIPTOR.message_types_by_name['SC_GetGachaData'] = _SC_GETGACHADATA
DESCRIPTOR.message_types_by_name['VO_GachaData'] = _VO_GACHADATA
DESCRIPTOR.message_types_by_name['VO_SoulBoxData'] = _VO_SOULBOXDATA
DESCRIPTOR.enum_types_by_name['GachaType'] = _GACHATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CS_Gacha = _reflection.GeneratedProtocolMessageType('CS_Gacha', (_message.Message,), dict(
  DESCRIPTOR = _CS_GACHA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:CS_Gacha)
  ))
_sym_db.RegisterMessage(CS_Gacha)

CS_GetGachaData = _reflection.GeneratedProtocolMessageType('CS_GetGachaData', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETGACHADATA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetGachaData)
  ))
_sym_db.RegisterMessage(CS_GetGachaData)

CS_GachaCommander = _reflection.GeneratedProtocolMessageType('CS_GachaCommander', (_message.Message,), dict(
  DESCRIPTOR = _CS_GACHACOMMANDER,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:CS_GachaCommander)
  ))
_sym_db.RegisterMessage(CS_GachaCommander)

CS_GetGachaCommanderData = _reflection.GeneratedProtocolMessageType('CS_GetGachaCommanderData', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETGACHACOMMANDERDATA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetGachaCommanderData)
  ))
_sym_db.RegisterMessage(CS_GetGachaCommanderData)

SC_Gacha = _reflection.GeneratedProtocolMessageType('SC_Gacha', (_message.Message,), dict(
  DESCRIPTOR = _SC_GACHA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:SC_Gacha)
  ))
_sym_db.RegisterMessage(SC_Gacha)

SC_GetGachaData = _reflection.GeneratedProtocolMessageType('SC_GetGachaData', (_message.Message,), dict(
  DESCRIPTOR = _SC_GETGACHADATA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:SC_GetGachaData)
  ))
_sym_db.RegisterMessage(SC_GetGachaData)

VO_GachaData = _reflection.GeneratedProtocolMessageType('VO_GachaData', (_message.Message,), dict(
  DESCRIPTOR = _VO_GACHADATA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:VO_GachaData)
  ))
_sym_db.RegisterMessage(VO_GachaData)

VO_SoulBoxData = _reflection.GeneratedProtocolMessageType('VO_SoulBoxData', (_message.Message,), dict(
  DESCRIPTOR = _VO_SOULBOXDATA,
  __module__ = 'Gacha_pb2'
  # @@protoc_insertion_point(class_scope:VO_SoulBoxData)
  ))
_sym_db.RegisterMessage(VO_SoulBoxData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\013GachaProtos'))
# @@protoc_insertion_point(module_scope)