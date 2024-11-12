# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Trd_ModifyOrder.proto

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
import Trd_Common_pb2 as Trd__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Trd_ModifyOrder.proto',
  package='Trd_ModifyOrder',
  syntax='proto2',
  serialized_pb=_b('\n\x15Trd_ModifyOrder.proto\x12\x0fTrd_ModifyOrder\x1a\x0c\x43ommon.proto\x1a\x10Trd_Common.proto\"\xc9\x02\n\x03\x43\x32S\x12\"\n\x08packetID\x18\x01 \x02(\x0b\x32\x10.Common.PacketID\x12%\n\x06header\x18\x02 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12\x0f\n\x07orderID\x18\x03 \x02(\x04\x12\x15\n\rmodifyOrderOp\x18\x04 \x02(\x05\x12\x0e\n\x06\x66orAll\x18\x05 \x01(\x08\x12\x11\n\ttrdMarket\x18\x06 \x01(\x05\x12\x0b\n\x03qty\x18\x08 \x01(\x01\x12\r\n\x05price\x18\t \x01(\x01\x12\x13\n\x0b\x61\x64justPrice\x18\n \x01(\x08\x12\x1a\n\x12\x61\x64justSideAndLimit\x18\x0b \x01(\x01\x12\x10\n\x08\x61uxPrice\x18\x0c \x01(\x01\x12\x11\n\ttrailType\x18\r \x01(\x05\x12\x12\n\ntrailValue\x18\x0e \x01(\x01\x12\x13\n\x0btrailSpread\x18\x0f \x01(\x01\x12\x11\n\torderIDEx\x18\x10 \x01(\t\"P\n\x03S2C\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12\x0f\n\x07orderID\x18\x02 \x02(\x04\x12\x11\n\torderIDEx\x18\x03 \x01(\t\",\n\x07Request\x12!\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x14.Trd_ModifyOrder.C2S\"e\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12!\n\x03s2c\x18\x04 \x01(\x0b\x32\x14.Trd_ModifyOrder.S2CBE\n\x13\x63om.futu.openapi.pbZ.github.com/futuopen/ftapi4go/pb/trdmodifyorder')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Trd__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Trd_ModifyOrder.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packetID', full_name='Trd_ModifyOrder.C2S.packetID', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_ModifyOrder.C2S.header', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderID', full_name='Trd_ModifyOrder.C2S.orderID', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifyOrderOp', full_name='Trd_ModifyOrder.C2S.modifyOrderOp', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forAll', full_name='Trd_ModifyOrder.C2S.forAll', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trdMarket', full_name='Trd_ModifyOrder.C2S.trdMarket', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qty', full_name='Trd_ModifyOrder.C2S.qty', index=6,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='Trd_ModifyOrder.C2S.price', index=7,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjustPrice', full_name='Trd_ModifyOrder.C2S.adjustPrice', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjustSideAndLimit', full_name='Trd_ModifyOrder.C2S.adjustSideAndLimit', index=9,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auxPrice', full_name='Trd_ModifyOrder.C2S.auxPrice', index=10,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trailType', full_name='Trd_ModifyOrder.C2S.trailType', index=11,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trailValue', full_name='Trd_ModifyOrder.C2S.trailValue', index=12,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trailSpread', full_name='Trd_ModifyOrder.C2S.trailSpread', index=13,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderIDEx', full_name='Trd_ModifyOrder.C2S.orderIDEx', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=75,
  serialized_end=404,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Trd_ModifyOrder.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_ModifyOrder.S2C.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderID', full_name='Trd_ModifyOrder.S2C.orderID', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderIDEx', full_name='Trd_ModifyOrder.S2C.orderIDEx', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=406,
  serialized_end=486,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Trd_ModifyOrder.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Trd_ModifyOrder.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=488,
  serialized_end=532,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Trd_ModifyOrder.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Trd_ModifyOrder.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Trd_ModifyOrder.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Trd_ModifyOrder.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Trd_ModifyOrder.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=534,
  serialized_end=635,
)

_C2S.fields_by_name['packetID'].message_type = Common__pb2._PACKETID
_C2S.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_S2C.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Trd_ModifyOrder_pb2'
  # @@protoc_insertion_point(class_scope:Trd_ModifyOrder.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Trd_ModifyOrder_pb2'
  # @@protoc_insertion_point(class_scope:Trd_ModifyOrder.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Trd_ModifyOrder_pb2'
  # @@protoc_insertion_point(class_scope:Trd_ModifyOrder.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Trd_ModifyOrder_pb2'
  # @@protoc_insertion_point(class_scope:Trd_ModifyOrder.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ.github.com/futuopen/ftapi4go/pb/trdmodifyorder'))
# @@protoc_insertion_point(module_scope)
