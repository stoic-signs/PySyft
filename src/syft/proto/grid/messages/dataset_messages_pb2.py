# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/dataset_messages.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/grid/messages/dataset_messages.proto",
    package="syft.grid.messages",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n*proto/grid/messages/dataset_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\x8e\x01\n\x14\x43reateDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"w\n\x15\x43reateDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8b\x01\n\x11GetDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"t\n\x12GetDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8e\x01\n\x14GetAllDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"w\n\x15GetAllDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8e\x01\n\x14SearchDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"w\n\x15SearchDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8e\x01\n\x14UpdateDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"w\n\x15UpdateDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_CREATEDATASETMESSAGE = _descriptor.Descriptor(
    name="CreateDatasetMessage",
    full_name="syft.grid.messages.CreateDatasetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.CreateDatasetMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.CreateDatasetMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="reply_to",
            full_name="syft.grid.messages.CreateDatasetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=135,
    serialized_end=277,
)


_CREATEDATASETRESPONSE = _descriptor.Descriptor(
    name="CreateDatasetResponse",
    full_name="syft.grid.messages.CreateDatasetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.CreateDatasetResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.CreateDatasetResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="success",
            full_name="syft.grid.messages.CreateDatasetResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=279,
    serialized_end=398,
)


_GETDATASETMESSAGE = _descriptor.Descriptor(
    name="GetDatasetMessage",
    full_name="syft.grid.messages.GetDatasetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetDatasetMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.GetDatasetMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="reply_to",
            full_name="syft.grid.messages.GetDatasetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=401,
    serialized_end=540,
)


_GETDATASETRESPONSE = _descriptor.Descriptor(
    name="GetDatasetResponse",
    full_name="syft.grid.messages.GetDatasetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetDatasetResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.GetDatasetResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="success",
            full_name="syft.grid.messages.GetDatasetResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=542,
    serialized_end=658,
)


_GETALLDATASETMESSAGE = _descriptor.Descriptor(
    name="GetAllDatasetMessage",
    full_name="syft.grid.messages.GetAllDatasetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetAllDatasetMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.GetAllDatasetMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="reply_to",
            full_name="syft.grid.messages.GetAllDatasetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=661,
    serialized_end=803,
)


_GETALLDATASETRESPONSE = _descriptor.Descriptor(
    name="GetAllDatasetResponse",
    full_name="syft.grid.messages.GetAllDatasetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetAllDatasetResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.GetAllDatasetResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="success",
            full_name="syft.grid.messages.GetAllDatasetResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=805,
    serialized_end=924,
)


_SEARCHDATASETMESSAGE = _descriptor.Descriptor(
    name="SearchDatasetMessage",
    full_name="syft.grid.messages.SearchDatasetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.SearchDatasetMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.SearchDatasetMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="reply_to",
            full_name="syft.grid.messages.SearchDatasetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=927,
    serialized_end=1069,
)


_SEARCHDATASETRESPONSE = _descriptor.Descriptor(
    name="SearchDatasetResponse",
    full_name="syft.grid.messages.SearchDatasetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.SearchDatasetResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.SearchDatasetResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="success",
            full_name="syft.grid.messages.SearchDatasetResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=1071,
    serialized_end=1190,
)


_UPDATEDATASETMESSAGE = _descriptor.Descriptor(
    name="UpdateDatasetMessage",
    full_name="syft.grid.messages.UpdateDatasetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.UpdateDatasetMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.UpdateDatasetMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="reply_to",
            full_name="syft.grid.messages.UpdateDatasetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=1193,
    serialized_end=1335,
)


_UPDATEDATASETRESPONSE = _descriptor.Descriptor(
    name="UpdateDatasetResponse",
    full_name="syft.grid.messages.UpdateDatasetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.UpdateDatasetResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="address",
            full_name="syft.grid.messages.UpdateDatasetResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="success",
            full_name="syft.grid.messages.UpdateDatasetResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=1337,
    serialized_end=1456,
)

_CREATEDATASETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEDATASETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEDATASETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEDATASETRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEDATASETRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLDATASETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLDATASETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLDATASETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLDATASETRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLDATASETRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHDATASETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SEARCHDATASETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHDATASETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHDATASETRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SEARCHDATASETRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEDATASETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_UPDATEDATASETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEDATASETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEDATASETRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_UPDATEDATASETRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["CreateDatasetMessage"] = _CREATEDATASETMESSAGE
DESCRIPTOR.message_types_by_name["CreateDatasetResponse"] = _CREATEDATASETRESPONSE
DESCRIPTOR.message_types_by_name["GetDatasetMessage"] = _GETDATASETMESSAGE
DESCRIPTOR.message_types_by_name["GetDatasetResponse"] = _GETDATASETRESPONSE
DESCRIPTOR.message_types_by_name["GetAllDatasetMessage"] = _GETALLDATASETMESSAGE
DESCRIPTOR.message_types_by_name["GetAllDatasetResponse"] = _GETALLDATASETRESPONSE
DESCRIPTOR.message_types_by_name["SearchDatasetMessage"] = _SEARCHDATASETMESSAGE
DESCRIPTOR.message_types_by_name["SearchDatasetResponse"] = _SEARCHDATASETRESPONSE
DESCRIPTOR.message_types_by_name["UpdateDatasetMessage"] = _UPDATEDATASETMESSAGE
DESCRIPTOR.message_types_by_name["UpdateDatasetResponse"] = _UPDATEDATASETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDatasetMessage = _reflection.GeneratedProtocolMessageType(
    "CreateDatasetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEDATASETMESSAGE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateDatasetMessage)
    },
)
_sym_db.RegisterMessage(CreateDatasetMessage)

CreateDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "CreateDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEDATASETRESPONSE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateDatasetResponse)
    },
)
_sym_db.RegisterMessage(CreateDatasetResponse)

GetDatasetMessage = _reflection.GeneratedProtocolMessageType(
    "GetDatasetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETDATASETMESSAGE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetMessage)
    },
)
_sym_db.RegisterMessage(GetDatasetMessage)

GetDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "GetDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETDATASETRESPONSE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetResponse)
    },
)
_sym_db.RegisterMessage(GetDatasetResponse)

GetAllDatasetMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllDatasetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLDATASETMESSAGE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllDatasetMessage)
    },
)
_sym_db.RegisterMessage(GetAllDatasetMessage)

GetAllDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "GetAllDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLDATASETRESPONSE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllDatasetResponse)
    },
)
_sym_db.RegisterMessage(GetAllDatasetResponse)

SearchDatasetMessage = _reflection.GeneratedProtocolMessageType(
    "SearchDatasetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHDATASETMESSAGE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchDatasetMessage)
    },
)
_sym_db.RegisterMessage(SearchDatasetMessage)

SearchDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "SearchDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHDATASETRESPONSE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchDatasetResponse)
    },
)
_sym_db.RegisterMessage(SearchDatasetResponse)

UpdateDatasetMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateDatasetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEDATASETMESSAGE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateDatasetMessage)
    },
)
_sym_db.RegisterMessage(UpdateDatasetMessage)

UpdateDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEDATASETRESPONSE,
        "__module__": "proto.grid.messages.dataset_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateDatasetResponse)
    },
)
_sym_db.RegisterMessage(UpdateDatasetResponse)


# @@protoc_insertion_point(module_scope)
