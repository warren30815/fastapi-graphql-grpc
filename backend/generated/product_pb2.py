# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: generated/product.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'generated/product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17generated/product.proto\x12\x07product\"{\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\r\n\x05stock\x18\x05 \x01(\x05\x12\x11\n\tis_active\x18\x06 \x01(\x08\x12\x10\n\x08\x63\x61tegory\x18\x07 \x01(\t\"\x1f\n\x11GetProductRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"i\n\x14\x43reateProductRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\r\n\x05stock\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\"u\n\x14UpdateProductRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\r\n\x05stock\x18\x05 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\"\"\n\x14\x44\x65leteProductRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"E\n\x12GetProductsRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\"9\n\x13GetProductsResponse\x12\"\n\x08products\x18\x01 \x03(\x0b\x32\x10.product.Product\"9\n\x15\x44\x65leteProductResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xea\x02\n\x0eProductService\x12:\n\nGetProduct\x12\x1a.product.GetProductRequest\x1a\x10.product.Product\x12@\n\rCreateProduct\x12\x1d.product.CreateProductRequest\x1a\x10.product.Product\x12H\n\x0bGetProducts\x12\x1b.product.GetProductsRequest\x1a\x1c.product.GetProductsResponse\x12@\n\rUpdateProduct\x12\x1d.product.UpdateProductRequest\x1a\x10.product.Product\x12N\n\rDeleteProduct\x12\x1d.product.DeleteProductRequest\x1a\x1e.product.DeleteProductResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generated.product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PRODUCT']._serialized_start=36
  _globals['_PRODUCT']._serialized_end=159
  _globals['_GETPRODUCTREQUEST']._serialized_start=161
  _globals['_GETPRODUCTREQUEST']._serialized_end=192
  _globals['_CREATEPRODUCTREQUEST']._serialized_start=194
  _globals['_CREATEPRODUCTREQUEST']._serialized_end=299
  _globals['_UPDATEPRODUCTREQUEST']._serialized_start=301
  _globals['_UPDATEPRODUCTREQUEST']._serialized_end=418
  _globals['_DELETEPRODUCTREQUEST']._serialized_start=420
  _globals['_DELETEPRODUCTREQUEST']._serialized_end=454
  _globals['_GETPRODUCTSREQUEST']._serialized_start=456
  _globals['_GETPRODUCTSREQUEST']._serialized_end=525
  _globals['_GETPRODUCTSRESPONSE']._serialized_start=527
  _globals['_GETPRODUCTSRESPONSE']._serialized_end=584
  _globals['_DELETEPRODUCTRESPONSE']._serialized_start=586
  _globals['_DELETEPRODUCTRESPONSE']._serialized_end=643
  _globals['_PRODUCTSERVICE']._serialized_start=646
  _globals['_PRODUCTSERVICE']._serialized_end=1008
# @@protoc_insertion_point(module_scope)
