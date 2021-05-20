# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/sympy/expression.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/sympy/expression.proto",
    package="syft.lib.sympy",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n proto/lib/sympy/expression.proto\x12\x0esyft.lib.sympy"l\n\nExpression\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x1a.syft.lib.sympy.Expression\x12\t\n\x01p\x18\x04 \x01(\x03\x12\t\n\x01q\x18\x05 \x01(\x03\x62\x06proto3',
)


_EXPRESSION = _descriptor.Descriptor(
    name="Expression",
    full_name="syft.lib.sympy.Expression",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.lib.sympy.Expression.obj_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="syft.lib.sympy.Expression.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="args",
            full_name="syft.lib.sympy.Expression.args",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="p",
            full_name="syft.lib.sympy.Expression.p",
            index=3,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="q",
            full_name="syft.lib.sympy.Expression.q",
            index=4,
            number=5,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=52,
    serialized_end=160,
)

_EXPRESSION.fields_by_name["args"].message_type = _EXPRESSION
DESCRIPTOR.message_types_by_name["Expression"] = _EXPRESSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Expression = _reflection.GeneratedProtocolMessageType(
    "Expression",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXPRESSION,
        "__module__": "proto.lib.sympy.expression_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.sympy.Expression)
    },
)
_sym_db.RegisterMessage(Expression)


# @@protoc_insertion_point(module_scope)
