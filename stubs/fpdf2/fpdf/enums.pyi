from enum import Enum, Flag, IntEnum, IntFlag
from typing import Literal
from typing_extensions import Self

class SignatureFlag(IntEnum):
    SIGNATURES_EXIST = 1
    APPEND_ONLY = 2

class CoerciveEnum(Enum):
    @classmethod
    def coerce(cls, value: Self | str) -> Self: ...

class CoerciveIntEnum(IntEnum):
    @classmethod
    def coerce(cls, value: Self | str | int) -> Self: ...

class CoerciveIntFlag(IntFlag):
    @classmethod
    def coerce(cls, value: Self | str | int) -> Self: ...

class WrapMode(CoerciveEnum):
    WORD = ...
    CHAR = ...

class CharVPos(CoerciveEnum):
    SUP = ...
    SUB = ...
    NOM = ...
    DENOM = ...
    LINE = ...

class Align(CoerciveEnum):
    C = ...
    X = ...
    L = ...
    R = ...
    J = ...

class VAlign(CoerciveEnum):
    M = ...
    T = ...
    B = ...

class TextEmphasis(CoerciveIntFlag):
    B = ...
    I = ...
    U = ...

    @property
    def style(self) -> str: ...

class MethodReturnValue(CoerciveIntFlag):
    PAGE_BREAK = ...
    LINES = ...
    HEIGHT = ...

class TableBordersLayout(CoerciveEnum):
    ALL = ...
    NONE = ...
    INTERNAL = ...
    MINIMAL = ...
    HORIZONTAL_LINES = ...
    NO_HORIZONTAL_LINES = ...
    SINGLE_TOP_LINE = ...

class TableCellFillMode(CoerciveEnum):
    NONE = ...
    ALL = ...
    ROWS = ...
    COLUMNS = ...

    def should_fill_cell(self, i: int, j: int) -> bool: ...

class TableSpan(CoerciveEnum):
    ROW: Literal["ROW"]
    COL: Literal["COL"]

class RenderStyle(CoerciveEnum):
    D = ...
    F = ...
    DF = ...
    @property
    def operator(self) -> str: ...
    @property
    def is_draw(self) -> bool: ...
    @property
    def is_fill(self) -> bool: ...

class TextMode(CoerciveIntEnum):
    FILL = ...
    STROKE = ...
    FILL_STROKE = ...
    INVISIBLE = ...
    FILL_CLIP = ...
    STROKE_CLIP = ...
    FILL_STROKE_CLIP = ...
    CLIP = ...

class XPos(CoerciveEnum):
    LEFT = ...
    RIGHT = ...
    START = ...
    END = ...
    WCONT = ...
    CENTER = ...
    LMARGIN = ...
    RMARGIN = ...

class YPos(CoerciveEnum):
    TOP = ...
    LAST = ...
    NEXT = ...
    TMARGIN = ...
    BMARGIN = ...

class Angle(CoerciveIntEnum):
    NORTH = ...
    EAST = ...
    SOUTH = ...
    WEST = ...
    NORTHEAST = ...
    SOUTHEAST = ...
    SOUTHWEST = ...
    NORTHWEST = ...

class PageLayout(CoerciveEnum):
    SINGLE_PAGE = ...
    ONE_COLUMN = ...
    TWO_COLUMN_LEFT = ...
    TWO_COLUMN_RIGHT = ...
    TWO_PAGE_LEFT = ...
    TWO_PAGE_RIGHT = ...

class PageMode(CoerciveEnum):
    USE_NONE = ...
    USE_OUTLINES = ...
    USE_THUMBS = ...
    FULL_SCREEN = ...
    USE_OC = ...
    USE_ATTACHMENTS = ...

class TextMarkupType(CoerciveEnum):
    HIGHLIGHT = ...
    UNDERLINE = ...
    SQUIGGLY = ...
    STRIKE_OUT = ...

class BlendMode(CoerciveEnum):
    NORMAL = ...
    MULTIPLY = ...
    SCREEN = ...
    OVERLAY = ...
    DARKEN = ...
    LIGHTEN = ...
    COLOR_DODGE = ...
    COLOR_BURN = ...
    HARD_LIGHT = ...
    SOFT_LIGHT = ...
    DIFFERENCE = ...
    EXCLUSION = ...
    HUE = ...
    SATURATION = ...
    COLOR = ...
    LUMINOSITY = ...

class AnnotationFlag(CoerciveIntEnum):
    INVISIBLE = ...
    HIDDEN = ...
    PRINT = ...
    NO_ZOOM = ...
    NO_ROTATE = ...
    NO_VIEW = ...
    READ_ONLY = ...
    LOCKED = ...
    TOGGLE_NO_VIEW = ...
    LOCKED_CONTENTS = ...

class AnnotationName(CoerciveEnum):
    NOTE = ...
    COMMENT = ...
    HELP = ...
    PARAGRAPH = ...
    NEW_PARAGRAPH = ...
    INSERT = ...

class FileAttachmentAnnotationName(CoerciveEnum):
    PUSH_PIN = ...
    GRAPH_PUSH_PIN = ...
    PAPERCLIP_TAG = ...

class IntersectionRule(CoerciveEnum):
    NONZERO = ...
    EVENODD = ...

class PathPaintRule(CoerciveEnum):
    STROKE = ...
    FILL_NONZERO = ...
    FILL_EVENODD = ...
    STROKE_FILL_NONZERO = ...
    STROKE_FILL_EVENODD = ...
    DONT_PAINT = ...
    AUTO = ...

class ClippingPathIntersectionRule(CoerciveEnum):
    NONZERO = ...
    EVENODD = ...

class StrokeCapStyle(CoerciveIntEnum):
    BUTT = ...
    ROUND = ...
    SQUARE = ...

class StrokeJoinStyle(CoerciveIntEnum):
    MITER = ...
    ROUND = ...
    BEVEL = ...

class PDFStyleKeys(Enum):
    FILL_ALPHA = ...
    BLEND_MODE = ...
    STROKE_ALPHA = ...
    STROKE_ADJUSTMENT = ...
    STROKE_WIDTH = ...
    STROKE_CAP_STYLE = ...
    STROKE_JOIN_STYLE = ...
    STROKE_MITER_LIMIT = ...
    STROKE_DASH_PATTERN = ...

class Corner(CoerciveEnum):
    TOP_RIGHT = ...
    TOP_LEFT = ...
    BOTTOM_RIGHT = ...
    BOTTOM_LEFT = ...

class FontDescriptorFlags(Flag):
    FIXED_PITCH = ...
    SYMBOLIC = ...
    ITALIC = ...
    FORCE_BOLD = ...

class AccessPermission(IntFlag):
    PRINT_LOW_RES = ...
    MODIFY = ...
    COPY = ...
    ANNOTATION = ...
    FILL_FORMS = ...
    COPY_FOR_ACCESSIBILITY = ...
    ASSEMBLE = ...
    PRINT_HIGH_RES = ...
    @classmethod
    def all(cls) -> int: ...
    @classmethod
    def none(cls) -> Literal[0]: ...

class EncryptionMethod(Enum):
    NO_ENCRYPTION = ...
    RC4 = ...
    AES_128 = ...
    AES_256 = ...
