from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLOAT32: _ClassVar[DType]
FLOAT32: DType

class Image(_message.Message):
    __slots__ = ("height", "width", "channel", "dtype", "data")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    channel: int
    dtype: DType
    data: bytes
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., channel: _Optional[int] = ..., dtype: _Optional[_Union[DType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("min_cell_area", "remove_out_of_bound", "scaling", "nms_iou", "detection_threshold", "segmentation_threshold", "return_polygon")
    MIN_CELL_AREA_FIELD_NUMBER: _ClassVar[int]
    REMOVE_OUT_OF_BOUND_FIELD_NUMBER: _ClassVar[int]
    SCALING_FIELD_NUMBER: _ClassVar[int]
    NMS_IOU_FIELD_NUMBER: _ClassVar[int]
    DETECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SEGMENTATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RETURN_POLYGON_FIELD_NUMBER: _ClassVar[int]
    min_cell_area: float
    remove_out_of_bound: bool
    scaling: float
    nms_iou: float
    detection_threshold: float
    segmentation_threshold: float
    return_polygon: bool
    def __init__(self, min_cell_area: _Optional[float] = ..., remove_out_of_bound: bool = ..., scaling: _Optional[float] = ..., nms_iou: _Optional[float] = ..., detection_threshold: _Optional[float] = ..., segmentation_threshold: _Optional[float] = ..., return_polygon: bool = ...) -> None: ...

class Input(_message.Message):
    __slots__ = ("settings", "image")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    image: Image
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ..., image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ("height", "width", "data")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    data: bytes
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("score", "label")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    score: Label
    label: Label
    def __init__(self, score: _Optional[_Union[Label, _Mapping]] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Polygon(_message.Message):
    __slots__ = ("score", "points")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    score: float
    points: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, score: _Optional[float] = ..., points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class PolygonResult(_message.Message):
    __slots__ = ("polygons",)
    POLYGONS_FIELD_NUMBER: _ClassVar[int]
    polygons: _containers.RepeatedCompositeFieldContainer[Polygon]
    def __init__(self, polygons: _Optional[_Iterable[_Union[Polygon, _Mapping]]] = ...) -> None: ...
