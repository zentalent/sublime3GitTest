# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Base.proto

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
  name='Base.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nBase.proto\x1a\x0cStruct.proto\x1a\nRole.proto\"*\n\x13\x43S_PrivilegeLevelup\x12\x13\n\x0bprivilegeId\x18\x01 \x02(\x05\"C\n\x13SC_PrivilegeLevelup\x12\x0c\n\x04rank\x18\x01 \x02(\x05\x12\x1e\n\x06update\x18\x02 \x01(\x0b\x32\x0e.VO_RoleUpdate\"\x17\n\x15\x43S_GetRankDailyReward\",\n\x14\x43S_WeaponPartLevelUp\x12\x14\n\x0cweaponPartId\x18\x01 \x02(\x05\"2\n\x17\x43S_WeaponSupportLevelUp\x12\x17\n\x0fweaponSupportId\x18\x01 \x02(\x05\"\x0f\n\rCS_WeaponList\"O\n\rSC_WeaponList\x12\x1f\n\x07weapons\x18\x01 \x03(\x0b\x32\x0e.VO_WeaponInfo\x12\x1d\n\x05parts\x18\x02 \x03(\x0b\x32\x0e.VO_WeaponInfo*4\n\rPrivilegeCate\x12\x12\n\x0e\x43\x61te_Exclusive\x10\x01\x12\x0f\n\x0b\x43\x61te_Normal\x10\x02*\xbc\x04\n\rPrivilegeType\x12\x1b\n\x17PTN_Campaign_Money_Incr\x10\x01\x12\x1a\n\x16PTN_Oil_Buy_Times_Incr\x10\x02\x12\x1c\n\x18PTN_Money_Buy_Times_Incr\x10\x03\x12\x1d\n\x19PTN_Money_Buy_Result_Incr\x10\x04\x12\"\n\x1ePTN_Gacha_Money_FreeTimes_Incr\x10\x05\x12\x1c\n\x18PTN_LTDJ_DailyTimes_Incr\x10\x06\x12\x1b\n\x17PTN_Help_OilReward_Incr\x10\x07\x12\x16\n\x12PTE_Campaign_Sweep\x10\x65\x12\x1f\n\x1bPTE_Gacha_Diamond_HalfPrice\x10\x66\x12\x12\n\x0ePTE_LTDJ_Sweep\x10g\x12!\n\x1dPTE_Campaign_Elite_Times_Incr\x10h\x12$\n PTE_Alamein_ExpBattle_Times_Incr\x10i\x12&\n\"PTE_Alamein_MoneyBattle_Times_Incr\x10j\x12$\n PTE_NormalShop_Refresh_FirstFree\x10k\x12#\n\x1fPTE_ArenaShop_Refresh_FirstFree\x10l\x12#\n\x1fPTE_ZldzzShop_Refresh_FirstFree\x10m\x12(\n$PTE_MilitaryAction_DelegateTime_Decr\x10nB2\n$com.fanxing.server.io.proto.protocolB\nBaseProtos')
  ,
  dependencies=[Struct__pb2.DESCRIPTOR,Role__pb2.DESCRIPTOR,])

_PRIVILEGECATE = _descriptor.EnumDescriptor(
  name='PrivilegeCate',
  full_name='PrivilegeCate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Cate_Exclusive', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Cate_Normal', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=374,
  serialized_end=426,
)
_sym_db.RegisterEnumDescriptor(_PRIVILEGECATE)

PrivilegeCate = enum_type_wrapper.EnumTypeWrapper(_PRIVILEGECATE)
_PRIVILEGETYPE = _descriptor.EnumDescriptor(
  name='PrivilegeType',
  full_name='PrivilegeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PTN_Campaign_Money_Incr', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_Oil_Buy_Times_Incr', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_Money_Buy_Times_Incr', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_Money_Buy_Result_Incr', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_Gacha_Money_FreeTimes_Incr', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_LTDJ_DailyTimes_Incr', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTN_Help_OilReward_Incr', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_Campaign_Sweep', index=7, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_Gacha_Diamond_HalfPrice', index=8, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_LTDJ_Sweep', index=9, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_Campaign_Elite_Times_Incr', index=10, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_Alamein_ExpBattle_Times_Incr', index=11, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_Alamein_MoneyBattle_Times_Incr', index=12, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_NormalShop_Refresh_FirstFree', index=13, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_ArenaShop_Refresh_FirstFree', index=14, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_ZldzzShop_Refresh_FirstFree', index=15, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PTE_MilitaryAction_DelegateTime_Decr', index=16, number=110,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=429,
  serialized_end=1001,
)
_sym_db.RegisterEnumDescriptor(_PRIVILEGETYPE)

PrivilegeType = enum_type_wrapper.EnumTypeWrapper(_PRIVILEGETYPE)
Cate_Exclusive = 1
Cate_Normal = 2
PTN_Campaign_Money_Incr = 1
PTN_Oil_Buy_Times_Incr = 2
PTN_Money_Buy_Times_Incr = 3
PTN_Money_Buy_Result_Incr = 4
PTN_Gacha_Money_FreeTimes_Incr = 5
PTN_LTDJ_DailyTimes_Incr = 6
PTN_Help_OilReward_Incr = 7
PTE_Campaign_Sweep = 101
PTE_Gacha_Diamond_HalfPrice = 102
PTE_LTDJ_Sweep = 103
PTE_Campaign_Elite_Times_Incr = 104
PTE_Alamein_ExpBattle_Times_Incr = 105
PTE_Alamein_MoneyBattle_Times_Incr = 106
PTE_NormalShop_Refresh_FirstFree = 107
PTE_ArenaShop_Refresh_FirstFree = 108
PTE_ZldzzShop_Refresh_FirstFree = 109
PTE_MilitaryAction_DelegateTime_Decr = 110



_CS_PRIVILEGELEVELUP = _descriptor.Descriptor(
  name='CS_PrivilegeLevelup',
  full_name='CS_PrivilegeLevelup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='privilegeId', full_name='CS_PrivilegeLevelup.privilegeId', index=0,
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
  serialized_start=40,
  serialized_end=82,
)


_SC_PRIVILEGELEVELUP = _descriptor.Descriptor(
  name='SC_PrivilegeLevelup',
  full_name='SC_PrivilegeLevelup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='SC_PrivilegeLevelup.rank', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update', full_name='SC_PrivilegeLevelup.update', index=1,
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
  serialized_start=84,
  serialized_end=151,
)


_CS_GETRANKDAILYREWARD = _descriptor.Descriptor(
  name='CS_GetRankDailyReward',
  full_name='CS_GetRankDailyReward',
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
  serialized_start=153,
  serialized_end=176,
)


_CS_WEAPONPARTLEVELUP = _descriptor.Descriptor(
  name='CS_WeaponPartLevelUp',
  full_name='CS_WeaponPartLevelUp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weaponPartId', full_name='CS_WeaponPartLevelUp.weaponPartId', index=0,
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
  serialized_start=178,
  serialized_end=222,
)


_CS_WEAPONSUPPORTLEVELUP = _descriptor.Descriptor(
  name='CS_WeaponSupportLevelUp',
  full_name='CS_WeaponSupportLevelUp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weaponSupportId', full_name='CS_WeaponSupportLevelUp.weaponSupportId', index=0,
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
  serialized_start=224,
  serialized_end=274,
)


_CS_WEAPONLIST = _descriptor.Descriptor(
  name='CS_WeaponList',
  full_name='CS_WeaponList',
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
  serialized_start=276,
  serialized_end=291,
)


_SC_WEAPONLIST = _descriptor.Descriptor(
  name='SC_WeaponList',
  full_name='SC_WeaponList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weapons', full_name='SC_WeaponList.weapons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parts', full_name='SC_WeaponList.parts', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=293,
  serialized_end=372,
)

_SC_PRIVILEGELEVELUP.fields_by_name['update'].message_type = Role__pb2._VO_ROLEUPDATE
_SC_WEAPONLIST.fields_by_name['weapons'].message_type = Struct__pb2._VO_WEAPONINFO
_SC_WEAPONLIST.fields_by_name['parts'].message_type = Struct__pb2._VO_WEAPONINFO
DESCRIPTOR.message_types_by_name['CS_PrivilegeLevelup'] = _CS_PRIVILEGELEVELUP
DESCRIPTOR.message_types_by_name['SC_PrivilegeLevelup'] = _SC_PRIVILEGELEVELUP
DESCRIPTOR.message_types_by_name['CS_GetRankDailyReward'] = _CS_GETRANKDAILYREWARD
DESCRIPTOR.message_types_by_name['CS_WeaponPartLevelUp'] = _CS_WEAPONPARTLEVELUP
DESCRIPTOR.message_types_by_name['CS_WeaponSupportLevelUp'] = _CS_WEAPONSUPPORTLEVELUP
DESCRIPTOR.message_types_by_name['CS_WeaponList'] = _CS_WEAPONLIST
DESCRIPTOR.message_types_by_name['SC_WeaponList'] = _SC_WEAPONLIST
DESCRIPTOR.enum_types_by_name['PrivilegeCate'] = _PRIVILEGECATE
DESCRIPTOR.enum_types_by_name['PrivilegeType'] = _PRIVILEGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CS_PrivilegeLevelup = _reflection.GeneratedProtocolMessageType('CS_PrivilegeLevelup', (_message.Message,), dict(
  DESCRIPTOR = _CS_PRIVILEGELEVELUP,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:CS_PrivilegeLevelup)
  ))
_sym_db.RegisterMessage(CS_PrivilegeLevelup)

SC_PrivilegeLevelup = _reflection.GeneratedProtocolMessageType('SC_PrivilegeLevelup', (_message.Message,), dict(
  DESCRIPTOR = _SC_PRIVILEGELEVELUP,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:SC_PrivilegeLevelup)
  ))
_sym_db.RegisterMessage(SC_PrivilegeLevelup)

CS_GetRankDailyReward = _reflection.GeneratedProtocolMessageType('CS_GetRankDailyReward', (_message.Message,), dict(
  DESCRIPTOR = _CS_GETRANKDAILYREWARD,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:CS_GetRankDailyReward)
  ))
_sym_db.RegisterMessage(CS_GetRankDailyReward)

CS_WeaponPartLevelUp = _reflection.GeneratedProtocolMessageType('CS_WeaponPartLevelUp', (_message.Message,), dict(
  DESCRIPTOR = _CS_WEAPONPARTLEVELUP,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:CS_WeaponPartLevelUp)
  ))
_sym_db.RegisterMessage(CS_WeaponPartLevelUp)

CS_WeaponSupportLevelUp = _reflection.GeneratedProtocolMessageType('CS_WeaponSupportLevelUp', (_message.Message,), dict(
  DESCRIPTOR = _CS_WEAPONSUPPORTLEVELUP,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:CS_WeaponSupportLevelUp)
  ))
_sym_db.RegisterMessage(CS_WeaponSupportLevelUp)

CS_WeaponList = _reflection.GeneratedProtocolMessageType('CS_WeaponList', (_message.Message,), dict(
  DESCRIPTOR = _CS_WEAPONLIST,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:CS_WeaponList)
  ))
_sym_db.RegisterMessage(CS_WeaponList)

SC_WeaponList = _reflection.GeneratedProtocolMessageType('SC_WeaponList', (_message.Message,), dict(
  DESCRIPTOR = _SC_WEAPONLIST,
  __module__ = 'Base_pb2'
  # @@protoc_insertion_point(class_scope:SC_WeaponList)
  ))
_sym_db.RegisterMessage(SC_WeaponList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.fanxing.server.io.proto.protocolB\nBaseProtos'))
# @@protoc_insertion_point(module_scope)
