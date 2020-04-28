# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/target/target.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.openconfig.gnmi.proto.gnmi import gnmi_pb2 as github_dot_com_dot_openconfig_dot_gnmi_dot_proto_dot_gnmi_dot_gnmi__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/target/target.proto',
  package='target',
  syntax='proto3',
  serialized_options=b'Z\'github.com/openconfig/gnmi/proto/target',
  serialized_pb=b'\n\x19proto/target/target.proto\x12\x06target\x1a\x30github.com/openconfig/gnmi/proto/gnmi/gnmi.proto\"\xa9\x02\n\rConfiguration\x12\x33\n\x07request\x18\x01 \x03(\x0b\x32\".target.Configuration.RequestEntry\x12\x31\n\x06target\x18\x02 \x03(\x0b\x32!.target.Configuration.TargetEntry\x12\x13\n\x0binstance_id\x18\x03 \x01(\t\x12\x14\n\x08revision\x18\xff\xff\xff\xff\x01 \x01(\x03\x1a\x46\n\x0cRequestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.gnmi.SubscribeRequest:\x02\x38\x01\x1a=\n\x0bTargetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.target.Target:\x02\x38\x01\"\xab\x01\n\x06Target\x12\x11\n\taddresses\x18\x01 \x03(\t\x12(\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x13.target.Credentials\x12\x0f\n\x07request\x18\x03 \x01(\t\x12&\n\x04meta\x18\x04 \x03(\x0b\x32\x18.target.Target.MetaEntry\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0bpassword_id\x18\x03 \x01(\tB)Z\'github.com/openconfig/gnmi/proto/targetb\x06proto3'
  ,
  dependencies=[github_dot_com_dot_openconfig_dot_gnmi_dot_proto_dot_gnmi_dot_gnmi__pb2.DESCRIPTOR,])




_CONFIGURATION_REQUESTENTRY = _descriptor.Descriptor(
  name='RequestEntry',
  full_name='target.Configuration.RequestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='target.Configuration.RequestEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='target.Configuration.RequestEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=322,
)

_CONFIGURATION_TARGETENTRY = _descriptor.Descriptor(
  name='TargetEntry',
  full_name='target.Configuration.TargetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='target.Configuration.TargetEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='target.Configuration.TargetEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=385,
)

_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='target.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='target.Configuration.request', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='target.Configuration.target', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='target.Configuration.instance_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='target.Configuration.revision', index=3,
      number=536870911, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGURATION_REQUESTENTRY, _CONFIGURATION_TARGETENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=385,
)


_TARGET_METAENTRY = _descriptor.Descriptor(
  name='MetaEntry',
  full_name='target.Target.MetaEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='target.Target.MetaEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='target.Target.MetaEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=559,
)

_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='target.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='target.Target.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credentials', full_name='target.Target.credentials', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='target.Target.request', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='target.Target.meta', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TARGET_METAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=559,
)


_CREDENTIALS = _descriptor.Descriptor(
  name='Credentials',
  full_name='target.Credentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='target.Credentials.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='target.Credentials.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password_id', full_name='target.Credentials.password_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=631,
)

_CONFIGURATION_REQUESTENTRY.fields_by_name['value'].message_type = github_dot_com_dot_openconfig_dot_gnmi_dot_proto_dot_gnmi_dot_gnmi__pb2._SUBSCRIBEREQUEST
_CONFIGURATION_REQUESTENTRY.containing_type = _CONFIGURATION
_CONFIGURATION_TARGETENTRY.fields_by_name['value'].message_type = _TARGET
_CONFIGURATION_TARGETENTRY.containing_type = _CONFIGURATION
_CONFIGURATION.fields_by_name['request'].message_type = _CONFIGURATION_REQUESTENTRY
_CONFIGURATION.fields_by_name['target'].message_type = _CONFIGURATION_TARGETENTRY
_TARGET_METAENTRY.containing_type = _TARGET
_TARGET.fields_by_name['credentials'].message_type = _CREDENTIALS
_TARGET.fields_by_name['meta'].message_type = _TARGET_METAENTRY
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['Credentials'] = _CREDENTIALS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {

  'RequestEntry' : _reflection.GeneratedProtocolMessageType('RequestEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_REQUESTENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Configuration.RequestEntry)
    })
  ,

  'TargetEntry' : _reflection.GeneratedProtocolMessageType('TargetEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_TARGETENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Configuration.TargetEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Configuration)
  })
_sym_db.RegisterMessage(Configuration)
_sym_db.RegisterMessage(Configuration.RequestEntry)
_sym_db.RegisterMessage(Configuration.TargetEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

  'MetaEntry' : _reflection.GeneratedProtocolMessageType('MetaEntry', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_METAENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Target.MetaEntry)
    })
  ,
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Target)
  })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.MetaEntry)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Credentials)
  })
_sym_db.RegisterMessage(Credentials)


DESCRIPTOR._options = None
_CONFIGURATION_REQUESTENTRY._options = None
_CONFIGURATION_TARGETENTRY._options = None
_TARGET_METAENTRY._options = None
# @@protoc_insertion_point(module_scope)
