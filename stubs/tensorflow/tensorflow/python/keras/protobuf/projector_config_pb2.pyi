"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
This file is a copy of the TensorBoard ProjectorConfig proto.
Keep this file in sync with the source proto definition at
https://github.com/tensorflow/tensorboard/blob/master/tensorboard/plugins/projector/projector_config.proto
"""
import builtins
import collections.abc
import typing as typing_extensions

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SpriteMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_PATH_FIELD_NUMBER: builtins.int
    SINGLE_IMAGE_DIM_FIELD_NUMBER: builtins.int
    image_path: builtins.str
    @property
    def single_image_dim(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """[width, height] of a single image in the sprite."""
    def __init__(
        self,
        *,
        image_path: builtins.str | None = ...,
        single_image_dim: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_path", b"image_path", "single_image_dim", b"single_image_dim"]) -> None: ...

global___SpriteMetadata = SpriteMetadata

@typing_extensions.final
class EmbeddingInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_NAME_FIELD_NUMBER: builtins.int
    METADATA_PATH_FIELD_NUMBER: builtins.int
    BOOKMARKS_PATH_FIELD_NUMBER: builtins.int
    TENSOR_SHAPE_FIELD_NUMBER: builtins.int
    SPRITE_FIELD_NUMBER: builtins.int
    TENSOR_PATH_FIELD_NUMBER: builtins.int
    tensor_name: builtins.str
    metadata_path: builtins.str
    bookmarks_path: builtins.str
    @property
    def tensor_shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Shape of the 2D tensor [N x D]. If missing, it will be inferred from the
        model checkpoint.
        """
    @property
    def sprite(self) -> global___SpriteMetadata: ...
    tensor_path: builtins.str
    """Path to the TSV file holding the tensor values. If missing, the tensor
    is assumed to be stored in the model checkpoint.
    """
    def __init__(
        self,
        *,
        tensor_name: builtins.str | None = ...,
        metadata_path: builtins.str | None = ...,
        bookmarks_path: builtins.str | None = ...,
        tensor_shape: collections.abc.Iterable[builtins.int] | None = ...,
        sprite: global___SpriteMetadata | None = ...,
        tensor_path: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sprite", b"sprite"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bookmarks_path", b"bookmarks_path", "metadata_path", b"metadata_path", "sprite", b"sprite", "tensor_name", b"tensor_name", "tensor_path", b"tensor_path", "tensor_shape", b"tensor_shape"]) -> None: ...

global___EmbeddingInfo = EmbeddingInfo

@typing_extensions.final
class ProjectorConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_CHECKPOINT_PATH_FIELD_NUMBER: builtins.int
    EMBEDDINGS_FIELD_NUMBER: builtins.int
    MODEL_CHECKPOINT_DIR_FIELD_NUMBER: builtins.int
    model_checkpoint_path: builtins.str
    """Path to the checkpoint file. Use either this or model_checkpoint_dir."""
    @property
    def embeddings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EmbeddingInfo]: ...
    model_checkpoint_dir: builtins.str
    """Path to the checkpoint directory. The directory will be scanned for the
    latest checkpoint file.
    """
    def __init__(
        self,
        *,
        model_checkpoint_path: builtins.str | None = ...,
        embeddings: collections.abc.Iterable[global___EmbeddingInfo] | None = ...,
        model_checkpoint_dir: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["embeddings", b"embeddings", "model_checkpoint_dir", b"model_checkpoint_dir", "model_checkpoint_path", b"model_checkpoint_path"]) -> None: ...

global___ProjectorConfig = ProjectorConfig
