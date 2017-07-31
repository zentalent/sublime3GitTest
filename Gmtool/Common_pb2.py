# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Common.proto

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
import OperAct_pb2 as OperAct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Common.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x43ommon.proto\x1a\x0cStruct.proto\x1a\rOperAct.proto\"c\n\rVO_ServerInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x1c\n\x06status\x18\x04 \x01(\x0e\x32\x0c.ServerState\x12\r\n\x05index\x18\x05 \x01(\x05\"!\n\x12\x43S_AddAuthenticate\x12\x0b\n\x03url\x18\x01 \x02(\t\"A\n\x0eVO_FileVersion\x12\x10\n\x08\x66ileName\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\"`\n\x0f\x43S_CheckVersion\x12\x15\n\rclientVersion\x18\x01 \x02(\t\x12#\n\ndbVersions\x18\x02 \x03(\x0b\x32\x0f.VO_FileVersion\x12\x11\n\tchannelID\x18\x03 \x01(\t\"#\n\x0f\x43S_SelectServer\x12\x10\n\x08serverId\x18\x01 \x02(\x05\"\x1a\n\x18\x43S_GetSystemAnnouncement\"+\n\x0fSC_SelectServer\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x0b\n\x03key\x18\x02 \x02(\t\"]\n\x0fSC_CheckVersion\x12\x14\n\x0cupdateClient\x18\x01 \x02(\x08\x12!\n\x08updateDb\x18\x02 \x03(\x0b\x32\x0f.VO_FileVersion\x12\x11\n\tupdateUrl\x18\x03 \x01(\t*J\n\x0bServerState\x12\r\n\tStateNULL\x10\x00\x12\x08\n\x04\x46ull\x10\x01\x12\x08\n\x04\x42usy\x10\x02\x12\n\n\x06\x46luent\x10\x03\x12\x0c\n\x08Maintain\x10\x04\x42\x34\n$com.fanxing.server.io.proto.protocolB\x0c\x43ommonProtos')
  ,
  dependencies=[Struct__pb2.DESCRIPTOR,OperAct__pb2.DESCRIPTOR,])

_SERVERSTATE = _descriptor.EnumDescriptor(
  name='ServerState',
  full_name='ServerState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='StateNULL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Full', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Busy', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Fluent', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Maintain', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=551,
  serialized_end=625,
)
_sym_db.RegisterEnumDescriptor(_SERVERSTATE)

ServerState = enum_type_wrapper.EnumTypeWrapper(_SERVERSTATE)
StateNULL = 0
Full = 1
Busy = 2
Fluent = 3
Maintain = 4



_VO_SERVERINFO = _descriptor.Descriptor(
  name='VO_ServerInfo',
  full_name='VO_ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='VO_ServerInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='VO_ServerInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='VO_ServerInfo.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='VO_ServerInfo.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='VO_ServerInfo.index', index=4,
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
  serialized_start=45,
  serialized_end=144,
)


_CS_ADDAUTHENTICATE = _descriptor.Descriptor(
  name='CS_AddAuthenticate',
  full_name='CS_AddAuthenticate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='CS_AddAuthenticate.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=146,
  serialized_end=179,
)


_VO_FILEVERSION = _descriptor.Descriptor(
  name='VO_FileVersion',
  full_name='VO_FileVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='VO_FileVersion.fileName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='VO_FileVersion.version', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='VO_FileVersion.size', index=2,
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
  serialized_start=181,
  serialized_end=246,
)


_CS_CHECKVERSION = _descriptor.Descriptor(
  name='CS_CheckVersion',
  full_name='CS_CheckVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientVersion', full_name='CS_CheckVersion.clientVersion', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbVersions', full_name='CS_CheckVersion.dbVersions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channelID', full_name='CS_CheckVersion.channelID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=344,
)


_CS_SELECTSERVER = _descriptor.Descriptor(
  name='CS_SelectServer',
  full_name='CS_SelectServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serverId', full_name='CS_SelectServer.serverId', index=0,
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
  serialized_start=346,
  serialized_end=381,
)


_CS_GETSYSTEMANNOUNCEMENT = _descriptor.Descriptor(
  name='CS_GetSystemAnnouncement',
  full_name='CS_GetSystemAnnouncement',
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
  serialized_start=383,
  serialized_end=409,
)


_SC_SELECTSERVER = _descriptor.Descriptor(
  name='SC_SelectServer',
  full_name='SC_SelectServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='SC_SelectServer.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='SC_SelectServer.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=411,
  serialized_end=454,
)


_SC_CHECKVERSION = _descriptor.Descriptor(
  name='SC_CheckVersion',
  full_name='SC_CheckVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updateClient', full_name='SC_CheckVersion.updateClient', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updateDb', full_name='SC_CheckVersion.updateDb', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updateUrl', full_name='SC_CheckVersion.updateUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=456,
  serialized_end=549,
)

_VO_SERVERINFO.fields_by_name['status'].enum_type = _SERVERSTATE
_CS_CHECKVERSION.fields_by_name['dbVersions'].message_type = _VO_FILEVERSION
_SC_CHECKVERSION.fields_by_name['updateDb'].message_type = _VO_FILEVERSION
DESCRIPTOR.message_types_by_name['VO_ServerInfo'] = _VO_SERVERINFO
DESCRIPTOR.message_types_by_name['CS_AddAuthenticate'] = _CS_ADDAUTHENTICATE
DESCRIPTOR.message_types_by_name['VO_FileVersion'] = _VO_FILEVERSION
DESCRIPTOR.message_types_by_name['CS_CheckVersion'] = _CS_CHECKVERSION
DESCRIPTOR.message_types_by_name['CS_SelectServer'] = _CS_SELECTSERVER
DESCRIPTOR.message_types_by_name['CS_GetSystemAnnouncement'] = _CS_GETSYSTEMANNOUNCEMENT
DESCRIPTOR.message_types_by_name['SC_SelectServer'] = _SC_SELECTSERVER
DESCRIPTOR.message_types_by_name['SC_CheckVersion'] = _SC_CHECKVERSION
DESCRIPTOR.enum_types_by_name['ServerState'] = _SERVERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VO_ServerInfo = _reflection.GeneratedProtocolMessageType('VO_ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _VO_SERVERINFO,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:VO_ServerInfo)
  ))
_sym_db.RegisterMessage(VO_ServerInfo)

CS_AddAuthenticate = _reflection.GeneratedProtocolMessageType('CS_AddAuthenticate', (_message.Message,), dict(
  DESCRIPTOR = _CS_ADDAUTHENTICATE,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:CS_AddAuthenticate)
  ))
_sym_db.RegisterMessage(CS_AddAuthenticate)

VO_FileVersion = _reflection.GeneratedProtocolMessageType('VO_FileVersion', (_message.Message,), dict(
  DESCRIPTOR = _VO_FILEVERSION,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:VO_FileVersion)
  ))
_sym_db.RegisterMessage(VO_FileVersion)

CS_CheckVersion = _reflection.GeneratedProtocolMessageType('CS_CheckVersion', (_message.Message,), dict(
  DESCRIPTOR = _CS_CHECKVERSION,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:CS_CheckVersion)
  ))
_sym_db.RegisterMessage(CS_CheckVersion)

CS_SelectServer = _reflection.GeneratedProtocolMessageType('CS_SelectServer', (_message.Message,), dict(
  DESCRIPTOR = _CS_SELECTSERVER,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:CS_SelectServer)
  ))
_sym_db.RegisterMessage(CS_SelectServer)

CS_GetSystemAnnouncement = _reflection.GeneratedProtocolMessageType('CS_GetSystemAnnouncement', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETSYSTEMANNOUNCEMENT,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetSystemAnnouncement)
  ))
_sym_db.RegisterMessage(CS_GetSystemAnnouncement)

SC_SelectServer = _reflection.GeneratedProtocolMessageType('SC_SelectServer', (_message.Message,), dict(
  DESCRIPTOR = _SC_SELECTSERVER,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:SC_SelectServer)
  ))
_sym_db.RegisterMessage(SC_SelectServer)

SC_CheckVersion = _reflection.GeneratedProtocolMessageType('SC_CheckVersion', (_message.Message,), dict(
  DESCRIPTOR = _SC_CHECKVERSION,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:SC_CheckVersion)
  ))
_sym_db.RegisterMessage(SC_CheckVersion)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\014CommonProtos'))
# @@protoc_insertion_point(module_scope)
