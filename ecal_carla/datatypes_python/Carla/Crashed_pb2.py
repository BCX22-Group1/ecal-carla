# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Carla/Crashed.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
from SensorNearData import SensorStates_pb2 as SensorNearData_dot_SensorStates__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Carla/Crashed.proto',
  package='pb.Carla',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x13\x43\x61rla/Crashed.proto\x12\x08pb.Carla\x1a\x0cheader.proto\x1a!SensorNearData/SensorStates.proto\"\xa1\x02\n\x07\x43rashed\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12$\n\x04\x65rrs\x18\x03 \x01(\x0b\x32\x16.pb.Carla.Crashed.Errs\x12*\n\x07signals\x18\x04 \x01(\x0b\x32\x19.pb.Carla.Crashed.Signals\x12/\n\ntimestamps\x18\x06 \x01(\x0b\x32\x1b.pb.Carla.Crashed.Timestamp\x1a\x36\n\x04\x45rrs\x12.\n\x07\x63rashed\x18\x02 \x01(\x0e\x32\x10.pb.SensorStates:\x0bSTATE_FAULT\x1a!\n\x07Signals\x12\x16\n\x07\x63rashed\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a\x1c\n\tTimestamp\x12\x0f\n\x07\x63rashed\x18\x02 \x01(\x12'
  ,
  dependencies=[header__pb2.DESCRIPTOR,SensorNearData_dot_SensorStates__pb2.DESCRIPTOR,])




_CRASHED_ERRS = _descriptor.Descriptor(
  name='Errs',
  full_name='pb.Carla.Crashed.Errs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='crashed', full_name='pb.Carla.Crashed.Errs.crashed', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=307,
)

_CRASHED_SIGNALS = _descriptor.Descriptor(
  name='Signals',
  full_name='pb.Carla.Crashed.Signals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='crashed', full_name='pb.Carla.Crashed.Signals.crashed', index=0,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=342,
)

_CRASHED_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='pb.Carla.Crashed.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='crashed', full_name='pb.Carla.Crashed.Timestamp.crashed', index=0,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=372,
)

_CRASHED = _descriptor.Descriptor(
  name='Crashed',
  full_name='pb.Carla.Crashed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.Carla.Crashed.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errs', full_name='pb.Carla.Crashed.errs', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signals', full_name='pb.Carla.Crashed.signals', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamps', full_name='pb.Carla.Crashed.timestamps', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CRASHED_ERRS, _CRASHED_SIGNALS, _CRASHED_TIMESTAMP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=372,
)

_CRASHED_ERRS.fields_by_name['crashed'].enum_type = SensorNearData_dot_SensorStates__pb2._SENSORSTATES
_CRASHED_ERRS.containing_type = _CRASHED
_CRASHED_SIGNALS.containing_type = _CRASHED
_CRASHED_TIMESTAMP.containing_type = _CRASHED
_CRASHED.fields_by_name['header'].message_type = header__pb2._HEADER
_CRASHED.fields_by_name['errs'].message_type = _CRASHED_ERRS
_CRASHED.fields_by_name['signals'].message_type = _CRASHED_SIGNALS
_CRASHED.fields_by_name['timestamps'].message_type = _CRASHED_TIMESTAMP
DESCRIPTOR.message_types_by_name['Crashed'] = _CRASHED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Crashed = _reflection.GeneratedProtocolMessageType('Crashed', (_message.Message,), {

  'Errs' : _reflection.GeneratedProtocolMessageType('Errs', (_message.Message,), {
    'DESCRIPTOR' : _CRASHED_ERRS,
    '__module__' : 'Carla.Crashed_pb2'
    # @@protoc_insertion_point(class_scope:pb.Carla.Crashed.Errs)
    })
  ,

  'Signals' : _reflection.GeneratedProtocolMessageType('Signals', (_message.Message,), {
    'DESCRIPTOR' : _CRASHED_SIGNALS,
    '__module__' : 'Carla.Crashed_pb2'
    # @@protoc_insertion_point(class_scope:pb.Carla.Crashed.Signals)
    })
  ,

  'Timestamp' : _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
    'DESCRIPTOR' : _CRASHED_TIMESTAMP,
    '__module__' : 'Carla.Crashed_pb2'
    # @@protoc_insertion_point(class_scope:pb.Carla.Crashed.Timestamp)
    })
  ,
  'DESCRIPTOR' : _CRASHED,
  '__module__' : 'Carla.Crashed_pb2'
  # @@protoc_insertion_point(class_scope:pb.Carla.Crashed)
  })
_sym_db.RegisterMessage(Crashed)
_sym_db.RegisterMessage(Crashed.Errs)
_sym_db.RegisterMessage(Crashed.Signals)
_sym_db.RegisterMessage(Crashed.Timestamp)


# @@protoc_insertion_point(module_scope)