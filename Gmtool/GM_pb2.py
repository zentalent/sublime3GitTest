# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GM.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GM.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x08GM.proto\",\n\nCS_SendCmd\x12\x0f\n\x07\x63mdType\x18\x01 \x02(\x05\x12\r\n\x05param\x18\x02 \x02(\t\"C\n\nSC_SendCmd\x12\x0f\n\x07\x63mdType\x18\x01 \x02(\x05\x12\x15\n\x06result\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05param\x18\x03 \x01(\tB0\n$com.fanxing.server.io.proto.protocolB\x08GMProtos')
)




_CS_SENDCMD = _descriptor.Descriptor(
  name='CS_SendCmd',
  full_name='CS_SendCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmdType', full_name='CS_SendCmd.cmdType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='CS_SendCmd.param', index=1,
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
  serialized_start=12,
  serialized_end=56,
)


_SC_SENDCMD = _descriptor.Descriptor(
  name='SC_SendCmd',
  full_name='SC_SendCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmdType', full_name='SC_SendCmd.cmdType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='SC_SendCmd.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='SC_SendCmd.param', index=2,
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
  serialized_start=58,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['CS_SendCmd'] = _CS_SENDCMD
DESCRIPTOR.message_types_by_name['SC_SendCmd'] = _SC_SENDCMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CS_SendCmd = _reflection.GeneratedProtocolMessageType('CS_SendCmd', (_message.Message,), dict(
  DESCRIPTOR = _CS_SENDCMD,
  __module__ = 'GM_pb2'
  # @@protoc_insertion_point(class_scope:CS_SendCmd)
  ))
_sym_db.RegisterMessage(CS_SendCmd)

SC_SendCmd = _reflection.GeneratedProtocolMessageType('SC_SendCmd', (_message.Message,), dict(
  DESCRIPTOR = _SC_SENDCMD,
  __module__ = 'GM_pb2'
  # @@protoc_insertion_point(class_scope:SC_SendCmd)
  ))
_sym_db.RegisterMessage(SC_SendCmd)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\010GMProtos'))
# @@protoc_insertion_point(module_scope)
