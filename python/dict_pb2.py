# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dict.proto

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
  name='dict.proto',
  package='protobuf',
  syntax='proto2',
  serialized_pb=_b('\n\ndict.proto\x12\x08protobuf\"\xd9\x02\n\x04\x44ict\x12>\n\x10\x66\x65\x61tureid2sortid\x18\x01 \x03(\x0b\x32$.protobuf.Dict.Featureid2sortidEntry\x12\x36\n\x0c\x66ield2missid\x18\x02 \x03(\x0b\x32 .protobuf.Dict.Field2missidEntry\x12\x36\n\x0c\x66ield2feanum\x18\x03 \x03(\x0b\x32 .protobuf.Dict.Field2feanumEntry\x1a\x37\n\x15\x46\x65\x61tureid2sortidEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x33\n\x11\x46ield2missidEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x33\n\x11\x46ield2feanumEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01')
)




_DICT_FEATUREID2SORTIDENTRY = _descriptor.Descriptor(
  name='Featureid2sortidEntry',
  full_name='protobuf.Dict.Featureid2sortidEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protobuf.Dict.Featureid2sortidEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protobuf.Dict.Featureid2sortidEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=264,
)

_DICT_FIELD2MISSIDENTRY = _descriptor.Descriptor(
  name='Field2missidEntry',
  full_name='protobuf.Dict.Field2missidEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protobuf.Dict.Field2missidEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protobuf.Dict.Field2missidEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=317,
)

_DICT_FIELD2FEANUMENTRY = _descriptor.Descriptor(
  name='Field2feanumEntry',
  full_name='protobuf.Dict.Field2feanumEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protobuf.Dict.Field2feanumEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protobuf.Dict.Field2feanumEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=370,
)

_DICT = _descriptor.Descriptor(
  name='Dict',
  full_name='protobuf.Dict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureid2sortid', full_name='protobuf.Dict.featureid2sortid', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field2missid', full_name='protobuf.Dict.field2missid', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field2feanum', full_name='protobuf.Dict.field2feanum', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DICT_FEATUREID2SORTIDENTRY, _DICT_FIELD2MISSIDENTRY, _DICT_FIELD2FEANUMENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=370,
)

_DICT_FEATUREID2SORTIDENTRY.containing_type = _DICT
_DICT_FIELD2MISSIDENTRY.containing_type = _DICT
_DICT_FIELD2FEANUMENTRY.containing_type = _DICT
_DICT.fields_by_name['featureid2sortid'].message_type = _DICT_FEATUREID2SORTIDENTRY
_DICT.fields_by_name['field2missid'].message_type = _DICT_FIELD2MISSIDENTRY
_DICT.fields_by_name['field2feanum'].message_type = _DICT_FIELD2FEANUMENTRY
DESCRIPTOR.message_types_by_name['Dict'] = _DICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), dict(

  Featureid2sortidEntry = _reflection.GeneratedProtocolMessageType('Featureid2sortidEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_FEATUREID2SORTIDENTRY,
    __module__ = 'dict_pb2'
    # @@protoc_insertion_point(class_scope:protobuf.Dict.Featureid2sortidEntry)
    ))
  ,

  Field2missidEntry = _reflection.GeneratedProtocolMessageType('Field2missidEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_FIELD2MISSIDENTRY,
    __module__ = 'dict_pb2'
    # @@protoc_insertion_point(class_scope:protobuf.Dict.Field2missidEntry)
    ))
  ,

  Field2feanumEntry = _reflection.GeneratedProtocolMessageType('Field2feanumEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_FIELD2FEANUMENTRY,
    __module__ = 'dict_pb2'
    # @@protoc_insertion_point(class_scope:protobuf.Dict.Field2feanumEntry)
    ))
  ,
  DESCRIPTOR = _DICT,
  __module__ = 'dict_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Dict)
  ))
_sym_db.RegisterMessage(Dict)
_sym_db.RegisterMessage(Dict.Featureid2sortidEntry)
_sym_db.RegisterMessage(Dict.Field2missidEntry)
_sym_db.RegisterMessage(Dict.Field2feanumEntry)


_DICT_FEATUREID2SORTIDENTRY.has_options = True
_DICT_FEATUREID2SORTIDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DICT_FIELD2MISSIDENTRY.has_options = True
_DICT_FIELD2MISSIDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DICT_FIELD2FEANUMENTRY.has_options = True
_DICT_FIELD2FEANUMENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
