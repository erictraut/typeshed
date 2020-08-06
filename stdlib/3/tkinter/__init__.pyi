import sys
from enum import Enum
from tkinter.constants import *  # noqa: F403
from types import TracebackType
from typing import Any, Callable, Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union, overload
from typing_extensions import Literal, TypedDict

TclError: Any
wantobjects: Any
TkVersion: Any
TclVersion: Any
READABLE: Any
WRITABLE: Any
EXCEPTION: Any

# If a manual page mentions Tk_GetAnchor or refers to another manual page named
# 'options', then it means this. Note that some ttk widgets have other things
# named 'anchor' with a different set of allowed values.
_Anchor = Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]

# string must be e.g. '12.34', '12.34c', '12.34i', '12.34m', '12.34p'
# see Tk_GetPixels man page for what each suffix means
# Some ttk widgets also use empty string.
_ScreenUnits = Union[str, float]

if sys.version_info >= (3, 6):
    class EventType(str, Enum):
        Activate = ...
        ButtonPress = ...
        ButtonRelease = ...
        Circulate = ...
        CirculateRequest = ...
        ClientMessage = ...
        Colormap = ...
        Configure = ...
        ConfigureRequest = ...
        Create = ...
        Deactivate = ...
        Destroy = ...
        Enter = ...
        Expose = ...
        FocusIn = ...
        FocusOut = ...
        GraphicsExpose = ...
        Gravity = ...
        KeyPress = ...
        KeyRelease = ...
        Keymap = ...
        Leave = ...
        Map = ...
        MapRequest = ...
        Mapping = ...
        Motion = ...
        MouseWheel = ...
        NoExpose = ...
        Property = ...
        Reparent = ...
        ResizeRequest = ...
        Selection = ...
        SelectionClear = ...
        SelectionRequest = ...
        Unmap = ...
        VirtualEvent = ...
        Visibility = ...

# Events considered covariant because you should never assign to event.widget.
_W = TypeVar("_W", covariant=True, bound="Misc")

class Event(Generic[_W]):
    serial: int
    num: int
    focus: bool
    height: int
    width: int
    keycode: int
    state: Union[int, str]
    time: int
    x: int
    y: int
    x_root: int
    y_root: int
    char: str
    send_event: bool
    keysym: str
    keysym_num: int
    if sys.version_info >= (3, 6):
        type: EventType
    else:
        type: str
    widget: _W
    delta: int

def NoDefaultRoot(): ...

_TraceMode = Literal["array", "read", "write", "unset"]

class Variable:
    def __init__(self, master: Optional[Misc] = ..., value: Optional[Any] = ..., name: Optional[str] = ...) -> None: ...
    def set(self, value: Any) -> None: ...
    initialize = set
    def get(self) -> Any: ...
    if sys.version_info >= (3, 6):
        def trace_add(self, mode: _TraceMode, callback: Callable[[str, str, str], None]) -> str: ...
        def trace_remove(self, mode: _TraceMode, cbname: str) -> None: ...
        def trace_info(self) -> List[Tuple[Tuple[_TraceMode, ...], str]]: ...
    def trace_variable(self, mode, callback): ...  # deprecated
    def trace_vdelete(self, mode, cbname): ...  # deprecated
    def trace_vinfo(self): ...  # deprecated
    trace = trace_variable  # deprecated

class StringVar(Variable):
    def __init__(self, master: Optional[Misc] = ..., value: Optional[str] = ..., name: Optional[str] = ...) -> None: ...
    def set(self, value: str) -> None: ...
    initialize = set
    def get(self) -> str: ...

class IntVar(Variable):
    def __init__(self, master: Optional[Misc] = ..., value: Optional[int] = ..., name: Optional[str] = ...) -> None: ...
    def set(self, value: int) -> None: ...
    initialize = set
    def get(self) -> int: ...

class DoubleVar(Variable):
    def __init__(self, master: Optional[Misc] = ..., value: Optional[float] = ..., name: Optional[str] = ...) -> None: ...
    def set(self, value: float) -> None: ...
    initialize = set
    def get(self) -> float: ...

class BooleanVar(Variable):
    def __init__(self, master: Optional[Misc] = ..., value: Optional[bool] = ..., name: Optional[str] = ...) -> None: ...
    def set(self, value: bool) -> None: ...
    initialize = set
    def get(self) -> bool: ...

def mainloop(n: int = ...): ...

getint: Any
getdouble: Any

def getboolean(s): ...

# This class is the base class of all widgets. Don't use BaseWidget or Widget
# for that because Tk doesn't inherit from Widget or BaseWidget.
class Misc:
    def destroy(self): ...
    def deletecommand(self, name): ...
    def tk_strictMotif(self, boolean: Optional[Any] = ...): ...
    def tk_bisque(self): ...
    def tk_setPalette(self, *args, **kw): ...
    if sys.version_info < (3, 6):
        def tk_menuBar(self, *args): ...
    def wait_variable(self, name: Union[str, Variable] = ...): ...
    waitvar: Any
    def wait_window(self, window: Optional[Any] = ...): ...
    def wait_visibility(self, window: Optional[Any] = ...): ...
    def setvar(self, name: str = ..., value: str = ...): ...
    def getvar(self, name: str = ...): ...
    def getint(self, s): ...
    def getdouble(self, s): ...
    def getboolean(self, s): ...
    def focus_set(self): ...
    focus: Any
    def focus_force(self): ...
    def focus_get(self): ...
    def focus_displayof(self): ...
    def focus_lastfor(self): ...
    def tk_focusFollowsMouse(self): ...
    def tk_focusNext(self): ...
    def tk_focusPrev(self): ...
    def after(self, ms, func: Optional[Any] = ..., *args): ...
    def after_idle(self, func, *args): ...
    def after_cancel(self, id): ...
    def bell(self, displayof: int = ...): ...
    def clipboard_get(self, **kw): ...
    def clipboard_clear(self, **kw): ...
    def clipboard_append(self, string, **kw): ...
    def grab_current(self): ...
    def grab_release(self): ...
    def grab_set(self): ...
    def grab_set_global(self): ...
    def grab_status(self): ...
    def option_add(self, pattern, value, priority: Optional[Any] = ...): ...
    def option_clear(self): ...
    def option_get(self, name, className): ...
    def option_readfile(self, fileName, priority: Optional[Any] = ...): ...
    def selection_clear(self, **kw): ...
    def selection_get(self, **kw): ...
    def selection_handle(self, command, **kw): ...
    def selection_own(self, **kw): ...
    def selection_own_get(self, **kw): ...
    def send(self, interp, cmd, *args): ...
    def lower(self, belowThis: Optional[Any] = ...): ...
    def tkraise(self, aboveThis: Optional[Any] = ...): ...
    lift: Any
    def winfo_atom(self, name, displayof: int = ...): ...
    def winfo_atomname(self, id, displayof: int = ...): ...
    def winfo_cells(self): ...
    def winfo_children(self): ...
    def winfo_class(self): ...
    def winfo_colormapfull(self): ...
    def winfo_containing(self, rootX, rootY, displayof: int = ...): ...
    def winfo_depth(self): ...
    def winfo_exists(self): ...
    def winfo_fpixels(self, number): ...
    def winfo_geometry(self): ...
    def winfo_height(self): ...
    def winfo_id(self): ...
    def winfo_interps(self, displayof: int = ...): ...
    def winfo_ismapped(self): ...
    def winfo_manager(self): ...
    def winfo_name(self): ...
    def winfo_parent(self): ...
    def winfo_pathname(self, id, displayof: int = ...): ...
    def winfo_pixels(self, number): ...
    def winfo_pointerx(self): ...
    def winfo_pointerxy(self): ...
    def winfo_pointery(self): ...
    def winfo_reqheight(self): ...
    def winfo_reqwidth(self): ...
    def winfo_rgb(self, color): ...
    def winfo_rootx(self): ...
    def winfo_rooty(self): ...
    def winfo_screen(self): ...
    def winfo_screencells(self): ...
    def winfo_screendepth(self): ...
    def winfo_screenheight(self): ...
    def winfo_screenmmheight(self): ...
    def winfo_screenmmwidth(self): ...
    def winfo_screenvisual(self): ...
    def winfo_screenwidth(self): ...
    def winfo_server(self): ...
    def winfo_toplevel(self): ...
    def winfo_viewable(self): ...
    def winfo_visual(self): ...
    def winfo_visualid(self): ...
    def winfo_visualsavailable(self, includeids: int = ...): ...
    def winfo_vrootheight(self): ...
    def winfo_vrootwidth(self): ...
    def winfo_vrootx(self): ...
    def winfo_vrooty(self): ...
    def winfo_width(self): ...
    def winfo_x(self): ...
    def winfo_y(self): ...
    def update(self): ...
    def update_idletasks(self): ...
    def bindtags(self, tagList: Optional[Any] = ...): ...
    # bind with isinstance(func, str) doesn't return anything, but all other
    # binds do. The default value of func is not str.
    @overload
    def bind(
        self,
        sequence: Optional[str] = ...,
        func: Optional[Callable[[Event[Misc]], Optional[Literal["break"]]]] = ...,
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def bind(self, sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def bind(self, *, func: str, add: Optional[bool] = ...) -> None: ...
    # There's no way to know what type of widget bind_all and bind_class
    # callbacks will get, so those are Misc.
    @overload
    def bind_all(
        self,
        sequence: Optional[str] = ...,
        func: Optional[Callable[[Event[Misc]], Optional[Literal["break"]]]] = ...,
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def bind_all(self, sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def bind_all(self, *, func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def bind_class(
        self,
        className: str,
        sequence: Optional[str] = ...,
        func: Optional[Callable[[Event[Misc]], Optional[Literal["break"]]]] = ...,
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def bind_class(self, className: str, sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def bind_class(self, className: str, *, func: str, add: Optional[bool] = ...) -> None: ...
    def unbind(self, sequence: str, funcid: Optional[str] = ...) -> None: ...
    def unbind_all(self, sequence: str) -> None: ...
    def unbind_class(self, className: str, sequence: str) -> None: ...
    def mainloop(self, n: int = ...): ...
    def quit(self): ...
    def nametowidget(self, name): ...
    register: Any
    def configure(self, cnf: Optional[Any] = ..., **kw): ...
    config = configure
    def cget(self, key): ...
    __getitem__: Any
    def __setitem__(self, key, value): ...
    def keys(self): ...
    @overload
    def pack_propagate(self, flag: bool) -> Optional[bool]: ...
    @overload
    def pack_propagate(self) -> None: ...
    propagate = pack_propagate
    def grid_anchor(self, anchor: Optional[_Anchor] = ...) -> None: ...
    anchor = grid_anchor
    @overload
    def grid_bbox(
        self, column: None = ..., row: None = ..., col2: None = ..., row2: None = ...
    ) -> Optional[Tuple[int, int, int, int]]: ...
    @overload
    def grid_bbox(self, column: int, row: int, col2: None = ..., row2: None = ...) -> Optional[Tuple[int, int, int, int]]: ...
    @overload
    def grid_bbox(self, column: int, row: int, col2: int, row2: int) -> Optional[Tuple[int, int, int, int]]: ...
    # commented out to avoid conflicting with other bbox methods
    # bbox = grid_bbox
    def grid_columnconfigure(self, index, cnf=..., **kw): ...  # TODO
    def grid_rowconfigure(self, index, cnf=..., **kw): ...  # TODO
    columnconfigure = grid_columnconfigure
    rowconfigure = grid_rowconfigure
    def grid_location(self, x: _ScreenUnits, y: _ScreenUnits) -> Tuple[int, int]: ...
    @overload
    def grid_propagate(self, flag: bool) -> None: ...
    @overload
    def grid_propagate(self) -> bool: ...
    def grid_size(self) -> Tuple[int, int]: ...
    size = grid_size
    # Widget because Toplevel or Tk is never a slave
    def pack_slaves(self) -> List[Widget]: ...
    def grid_slaves(self, row: Optional[int] = ..., column: Optional[int] = ...) -> List[Widget]: ...
    def place_slaves(self) -> List[Widget]: ...
    slaves = pack_slaves
    def event_add(self, virtual, *sequences): ...
    def event_delete(self, virtual, *sequences): ...
    def event_generate(self, sequence, **kw): ...
    def event_info(self, virtual: Optional[Any] = ...): ...
    def image_names(self): ...
    def image_types(self): ...

class CallWrapper:
    func: Any
    subst: Any
    widget: Any
    def __init__(self, func, subst, widget): ...
    def __call__(self, *args): ...

class XView:
    def xview(self, *args): ...
    def xview_moveto(self, fraction): ...
    def xview_scroll(self, number, what): ...

class YView:
    def yview(self, *args): ...
    def yview_moveto(self, fraction): ...
    def yview_scroll(self, number, what): ...

class Wm:
    def wm_aspect(
        self,
        minNumer: Optional[Any] = ...,
        minDenom: Optional[Any] = ...,
        maxNumer: Optional[Any] = ...,
        maxDenom: Optional[Any] = ...,
    ): ...
    aspect: Any
    def wm_attributes(self, *args): ...
    attributes: Any
    def wm_client(self, name: Optional[Any] = ...): ...
    client: Any
    def wm_colormapwindows(self, *wlist): ...
    colormapwindows: Any
    def wm_command(self, value: Optional[Any] = ...): ...
    command: Any
    def wm_deiconify(self): ...
    deiconify: Any
    def wm_focusmodel(self, model: Optional[Any] = ...): ...
    focusmodel: Any
    def wm_forget(self, window): ...
    forget: Any
    def wm_frame(self): ...
    frame: Any
    def wm_geometry(self, newGeometry: Optional[Any] = ...): ...
    geometry: Any
    def wm_grid(
        self,
        baseWidth: Optional[Any] = ...,
        baseHeight: Optional[Any] = ...,
        widthInc: Optional[Any] = ...,
        heightInc: Optional[Any] = ...,
    ): ...
    grid: Any
    def wm_group(self, pathName: Optional[Any] = ...): ...
    group: Any
    def wm_iconbitmap(self, bitmap: Optional[Any] = ..., default: Optional[Any] = ...): ...
    iconbitmap: Any
    def wm_iconify(self): ...
    iconify: Any
    def wm_iconmask(self, bitmap: Optional[Any] = ...): ...
    iconmask: Any
    def wm_iconname(self, newName: Optional[Any] = ...): ...
    iconname: Any
    def wm_iconphoto(self, default: bool = ..., *args): ...
    iconphoto: Any
    def wm_iconposition(self, x: Optional[Any] = ..., y: Optional[Any] = ...): ...
    iconposition: Any
    def wm_iconwindow(self, pathName: Optional[Any] = ...): ...
    iconwindow: Any
    def wm_manage(self, widget): ...
    manage: Any
    def wm_maxsize(self, width: Optional[Any] = ..., height: Optional[Any] = ...): ...
    maxsize: Any
    def wm_minsize(self, width: Optional[Any] = ..., height: Optional[Any] = ...): ...
    minsize: Any
    def wm_overrideredirect(self, boolean: Optional[Any] = ...): ...
    overrideredirect: Any
    def wm_positionfrom(self, who: Optional[Any] = ...): ...
    positionfrom: Any
    def wm_protocol(self, name: Optional[Any] = ..., func: Optional[Any] = ...): ...
    protocol: Any
    def wm_resizable(self, width: Optional[Any] = ..., height: Optional[Any] = ...): ...
    resizable: Any
    def wm_sizefrom(self, who: Optional[Any] = ...): ...
    sizefrom: Any
    def wm_state(self, newstate: Optional[Any] = ...): ...
    state: Any
    def wm_title(self, string: Optional[Any] = ...): ...
    title: Any
    def wm_transient(self, master: Optional[Any] = ...): ...
    transient: Any
    def wm_withdraw(self): ...
    withdraw: Any

class Tk(Misc, Wm):
    master: Optional[Any]
    children: Dict[str, Any]
    tk: Any
    def __init__(
        self,
        screenName: Optional[str] = ...,
        baseName: Optional[str] = ...,
        className: str = ...,
        useTk: bool = ...,
        sync: bool = ...,
        use: Optional[str] = ...,
    ) -> None: ...
    def loadtk(self) -> None: ...
    def destroy(self) -> None: ...
    def readprofile(self, baseName: str, className: str) -> None: ...
    report_callback_exception: Callable[[Type[BaseException], BaseException, TracebackType], Any]
    def __getattr__(self, attr: str) -> Any: ...

def Tcl(screenName: Optional[Any] = ..., baseName: Optional[Any] = ..., className: str = ..., useTk: bool = ...): ...

_InMiscTotal = TypedDict("_InMiscTotal", {"in": Misc})
_InMiscNonTotal = TypedDict("_InMiscNonTotal", {"in": Misc}, total=False)

class _PackInfo(_InMiscTotal):
    # 'before' and 'after' never appear in _PackInfo
    anchor: _Anchor
    expand: Literal[0, 1]
    fill: Literal["none", "x", "y", "both"]
    side: Literal["left", "right", "top", "bottom"]
    # Paddings come out as int or tuple of int, even though any _ScreenUnits
    # can be specified in pack().
    ipadx: Union[int, Tuple[int, int]]
    ipady: Union[int, Tuple[int, int]]
    padx: Union[int, Tuple[int, int]]
    pady: Union[int, Tuple[int, int]]

class Pack:
    # _PackInfo is not the valid type for cnf because pad stuff accepts any
    # _ScreenUnits instead of int only. I didn't bother to create another
    # TypedDict for cnf because it appears to be a legacy thing that was
    # replaced by **kwargs.
    def pack_configure(
        self,
        cnf: Optional[Dict[str, Any]] = ...,
        *,
        after: Misc = ...,
        anchor: _Anchor = ...,
        before: Misc = ...,
        expand: bool = ...,
        fill: Literal["none", "x", "y", "both"] = ...,
        side: Literal["left", "right", "top", "bottom"] = ...,
        ipadx: Union[_ScreenUnits, Tuple[_ScreenUnits, _ScreenUnits]] = ...,
        ipady: Union[_ScreenUnits, Tuple[_ScreenUnits, _ScreenUnits]] = ...,
        padx: Union[_ScreenUnits, Tuple[_ScreenUnits, _ScreenUnits]] = ...,
        pady: Union[_ScreenUnits, Tuple[_ScreenUnits, _ScreenUnits]] = ...,
        in_: Misc = ...,
    ) -> None: ...
    def pack_forget(self) -> None: ...
    def pack_info(self) -> _PackInfo: ...  # errors if widget hasn't been packed
    pack = pack_configure
    forget = pack_forget
    propagate = Misc.pack_propagate
    # commented out to avoid mypy getting confused with multiple
    # inheritance and how things get overrided with different things
    # info = pack_info
    # pack_propagate = Misc.pack_propagate
    # configure = pack_configure
    # config = pack_configure
    # slaves = Misc.pack_slaves
    # pack_slaves = Misc.pack_slaves

class _PlaceInfo(_InMiscNonTotal, total=False):  # empty dict if widget hasn't been placed
    anchor: _Anchor
    bordermode: Literal["inside", "outside", "ignore"]
    width: str  # can be int()ed (even after e.g. widget.place(height='2.3c') or similar)
    height: str  # can be int()ed
    x: str  # can be int()ed
    y: str  # can be int()ed
    relheight: str  # can be float()ed if not empty string
    relwidth: str  # can be float()ed if not empty string
    relx: float  # can be float()ed if not empty string
    rely: float  # can be float()ed if not empty string

class Place:
    def place_configure(
        self,
        cnf: Optional[Dict[str, Any]] = ...,
        *,
        anchor: _Anchor = ...,
        bordermode: Literal["inside", "outside", "ignore"] = ...,
        width: _ScreenUnits = ...,
        height: _ScreenUnits = ...,
        x: _ScreenUnits = ...,
        y: _ScreenUnits = ...,
        relheight: float = ...,
        relwidth: float = ...,
        relx: float = ...,
        rely: float = ...,
        in_: Misc = ...,
    ) -> None: ...
    def place_forget(self) -> None: ...
    def place_info(self) -> _PlaceInfo: ...
    place = place_configure
    info = place_info
    # commented out to avoid mypy getting confused with multiple
    # inheritance and how things get overrided with different things
    # config = place_configure
    # configure = place_configure
    # forget = place_forget
    # slaves = Misc.place_slaves
    # place_slaves = Misc.place_slaves

class _GridInfo(_InMiscNonTotal, total=False):  # empty dict if widget hasn't been gridded
    column: int
    columnspan: int
    row: int
    rowspan: int
    ipadx: int
    ipady: int
    padx: int
    pady: int
    sticky: str  # consists of letters 'n', 's', 'w', 'e', no repeats, may be empty

class Grid:
    def grid_configure(
        self,
        cnf: Optional[Dict[str, Any]] = ...,
        *,
        column: int = ...,
        columnspan: int = ...,
        row: int = ...,
        rowspan: int = ...,
        ipadx: _ScreenUnits = ...,
        ipady: _ScreenUnits = ...,
        padx: _ScreenUnits = ...,
        pady: _ScreenUnits = ...,
        sticky: str = ...,  # consists of letters 'n', 's', 'w', 'e', may contain repeats, may be empty
        in_: Misc = ...,
    ) -> None: ...
    def grid_forget(self) -> None: ...
    def grid_remove(self) -> None: ...
    def grid_info(self) -> _GridInfo: ...
    grid = grid_configure
    location = Misc.grid_location
    size = Misc.grid_size
    # commented out to avoid mypy getting confused with multiple
    # inheritance and how things get overrided with different things
    # bbox = Misc.grid_bbox
    # grid_bbox = Misc.grid_bbox
    # forget = grid_forget
    # info = grid_info
    # grid_location = Misc.grid_location
    # grid_propagate = Misc.grid_propagate
    # grid_size = Misc.grid_size
    # rowconfigure = Misc.grid_rowconfigure
    # grid_rowconfigure = Misc.grid_rowconfigure
    # grid_columnconfigure = Misc.grid_columnconfigure
    # columnconfigure = Misc.grid_columnconfigure
    # config = grid_configure
    # configure = grid_configure
    # propagate = Misc.grid_propagate
    # slaves = Misc.grid_slaves
    # grid_slaves = Misc.grid_slaves

class BaseWidget(Misc):
    widgetName: Any
    def __init__(self, master, widgetName, cnf=..., kw=..., extra=...): ...
    def destroy(self): ...

# This class represents any widget except Toplevel or Tk.
class Widget(BaseWidget, Pack, Place, Grid):
    # Allow bind callbacks to take e.g. Event[Label] instead of Event[Misc].
    # Tk and Toplevel get notified for their child widgets' events, but other
    # widgets don't.
    @overload
    def bind(
        self: _W,
        sequence: Optional[str] = ...,
        func: Optional[Callable[[Event[_W]], Optional[Literal["break"]]]] = ...,
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def bind(self, sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def bind(self, *, func: str, add: Optional[bool] = ...) -> None: ...

class Toplevel(BaseWidget, Wm):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Button(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def flash(self): ...
    def invoke(self): ...

class Canvas(Widget, XView, YView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def addtag(self, *args): ...
    def addtag_above(self, newtag, tagOrId): ...
    def addtag_all(self, newtag): ...
    def addtag_below(self, newtag, tagOrId): ...
    def addtag_closest(self, newtag, x, y, halo: Optional[Any] = ..., start: Optional[Any] = ...): ...
    def addtag_enclosed(self, newtag, x1, y1, x2, y2): ...
    def addtag_overlapping(self, newtag, x1, y1, x2, y2): ...
    def addtag_withtag(self, newtag, tagOrId): ...
    def bbox(self, *args): ...
    @overload
    def tag_bind(
        self,
        tagOrId: Union[str, int],
        sequence: Optional[str] = ...,
        func: Optional[Callable[[Event[Canvas]], Optional[Literal["break"]]]] = ...,
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def tag_bind(self, tagOrId: Union[str, int], sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    @overload
    def tag_bind(self, tagOrId: Union[str, int], *, func: str, add: Optional[bool] = ...) -> None: ...
    def tag_unbind(self, tagOrId: Union[str, int], sequence: str, funcid: Optional[str] = ...) -> None: ...
    def canvasx(self, screenx, gridspacing: Optional[Any] = ...): ...
    def canvasy(self, screeny, gridspacing: Optional[Any] = ...): ...
    def coords(self, *args): ...
    def create_arc(self, *args, **kw): ...
    def create_bitmap(self, *args, **kw): ...
    def create_image(self, *args, **kw): ...
    def create_line(self, *args, **kw): ...
    def create_oval(self, *args, **kw): ...
    def create_polygon(self, *args, **kw): ...
    def create_rectangle(self, *args, **kw): ...
    def create_text(self, *args, **kw): ...
    def create_window(self, *args, **kw): ...
    def dchars(self, *args): ...
    def delete(self, *args): ...
    def dtag(self, *args): ...
    def find(self, *args): ...
    def find_above(self, tagOrId): ...
    def find_all(self): ...
    def find_below(self, tagOrId): ...
    def find_closest(self, x, y, halo: Optional[Any] = ..., start: Optional[Any] = ...): ...
    def find_enclosed(self, x1, y1, x2, y2): ...
    def find_overlapping(self, x1, y1, x2, y2): ...
    def find_withtag(self, tagOrId): ...
    def focus(self, *args): ...
    def gettags(self, *args): ...
    def icursor(self, *args): ...
    def index(self, *args): ...
    def insert(self, *args): ...
    def itemcget(self, tagOrId, option): ...
    def itemconfigure(self, tagOrId, cnf: Optional[Any] = ..., **kw): ...
    itemconfig: Any
    def tag_lower(self, *args): ...
    lower: Any
    def move(self, *args): ...
    if sys.version_info >= (3, 8):
        def moveto(self, tagOrId: Union[int, str], x: str = ..., y: str = ...) -> None: ...
    def postscript(self, cnf=..., **kw): ...
    def tag_raise(self, *args): ...
    lift: Any
    def scale(self, *args): ...
    def scan_mark(self, x, y): ...
    def scan_dragto(self, x, y, gain: int = ...): ...
    def select_adjust(self, tagOrId, index): ...
    def select_clear(self): ...
    def select_from(self, tagOrId, index): ...
    def select_item(self): ...
    def select_to(self, tagOrId, index): ...
    def type(self, tagOrId): ...

class Checkbutton(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def deselect(self): ...
    def flash(self): ...
    def invoke(self): ...
    def select(self): ...
    def toggle(self): ...

class Entry(Widget, XView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def delete(self, first, last: Optional[Any] = ...): ...
    def get(self): ...
    def icursor(self, index): ...
    def index(self, index): ...
    def insert(self, index, string): ...
    def scan_mark(self, x): ...
    def scan_dragto(self, x): ...
    def selection_adjust(self, index): ...
    select_adjust: Any
    def selection_clear(self): ...
    select_clear: Any
    def selection_from(self, index): ...
    select_from: Any
    def selection_present(self): ...
    select_present: Any
    def selection_range(self, start, end): ...
    select_range: Any
    def selection_to(self, index): ...
    select_to: Any

class Frame(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Label(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Listbox(Widget, XView, YView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def activate(self, index): ...
    def bbox(self, index): ...
    def curselection(self): ...
    def delete(self, first, last: Optional[Any] = ...): ...
    def get(self, first, last: Optional[Any] = ...): ...
    def index(self, index): ...
    def insert(self, index, *elements): ...
    def nearest(self, y): ...
    def scan_mark(self, x, y): ...
    def scan_dragto(self, x, y): ...
    def see(self, index): ...
    def selection_anchor(self, index): ...
    select_anchor: Any
    def selection_clear(self, first, last: Optional[Any] = ...): ...  # type: ignore
    select_clear: Any
    def selection_includes(self, index): ...
    select_includes: Any
    def selection_set(self, first, last: Optional[Any] = ...): ...
    select_set: Any
    def size(self): ...
    def itemcget(self, index, option): ...
    def itemconfigure(self, index, cnf: Optional[Any] = ..., **kw): ...
    itemconfig: Any

class Menu(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def tk_popup(self, x, y, entry: str = ...): ...
    if sys.version_info < (3, 6):
        def tk_bindForTraversal(self): ...
    def activate(self, index): ...
    def add(self, itemType, cnf=..., **kw): ...
    def add_cascade(self, cnf=..., **kw): ...
    def add_checkbutton(self, cnf=..., **kw): ...
    def add_command(self, cnf=..., **kw): ...
    def add_radiobutton(self, cnf=..., **kw): ...
    def add_separator(self, cnf=..., **kw): ...
    def insert(self, index, itemType, cnf=..., **kw): ...
    def insert_cascade(self, index, cnf=..., **kw): ...
    def insert_checkbutton(self, index, cnf=..., **kw): ...
    def insert_command(self, index, cnf=..., **kw): ...
    def insert_radiobutton(self, index, cnf=..., **kw): ...
    def insert_separator(self, index, cnf=..., **kw): ...
    def delete(self, index1, index2: Optional[Any] = ...): ...
    def entrycget(self, index, option): ...
    def entryconfigure(self, index, cnf: Optional[Any] = ..., **kw): ...
    entryconfig: Any
    def index(self, index): ...
    def invoke(self, index): ...
    def post(self, x, y): ...
    def type(self, index): ...
    def unpost(self): ...
    def xposition(self, index): ...
    def yposition(self, index): ...

class Menubutton(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Message(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class Radiobutton(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def deselect(self): ...
    def flash(self): ...
    def invoke(self): ...
    def select(self): ...

class Scale(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def get(self): ...
    def set(self, value): ...
    def coords(self, value: Optional[Any] = ...): ...
    def identify(self, x, y): ...

class Scrollbar(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def activate(self, index: Optional[Any] = ...): ...
    def delta(self, deltax, deltay): ...
    def fraction(self, x, y): ...
    def identify(self, x, y): ...
    def get(self): ...
    def set(self, first, last): ...

class Text(Widget, XView, YView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def bbox(self, index): ...
    def compare(self, index1, op, index2): ...
    def count(self, index1, index2, *args): ...
    def debug(self, boolean: Optional[Any] = ...): ...
    def delete(self, index1, index2: Optional[Any] = ...): ...
    def dlineinfo(self, index): ...
    def dump(self, index1, index2: Optional[Any] = ..., command: Optional[Any] = ..., **kw): ...
    def edit(self, *args): ...
    def edit_modified(self, arg: Optional[Any] = ...): ...
    def edit_redo(self): ...
    def edit_reset(self): ...
    def edit_separator(self): ...
    def edit_undo(self): ...
    def get(self, index1, index2: Optional[Any] = ...): ...
    def image_cget(self, index, option): ...
    def image_configure(self, index, cnf: Optional[Any] = ..., **kw): ...
    def image_create(self, index, cnf=..., **kw): ...
    def image_names(self): ...
    def index(self, index): ...
    def insert(self, index, chars, *args): ...
    def mark_gravity(self, markName, direction: Optional[Any] = ...): ...
    def mark_names(self): ...
    def mark_set(self, markName, index): ...
    def mark_unset(self, *markNames): ...
    def mark_next(self, index): ...
    def mark_previous(self, index): ...
    def peer_create(self, newPathName, cnf=..., **kw): ...
    def peer_names(self): ...
    def replace(self, index1, index2, chars, *args): ...
    def scan_mark(self, x, y): ...
    def scan_dragto(self, x, y): ...
    def search(
        self,
        pattern,
        index,
        stopindex: Optional[Any] = ...,
        forwards: Optional[Any] = ...,
        backwards: Optional[Any] = ...,
        exact: Optional[Any] = ...,
        regexp: Optional[Any] = ...,
        nocase: Optional[Any] = ...,
        count: Optional[Any] = ...,
        elide: Optional[Any] = ...,
    ): ...
    def see(self, index): ...
    def tag_add(self, tagName, index1, *args): ...
    # tag_bind stuff is very similar to Canvas
    @overload
    def tag_bind(
        self,
        tagName: str,
        sequence: Optional[str],
        func: Optional[Callable[[Event[Text]], Optional[Literal["break"]]]],
        add: Optional[bool] = ...,
    ) -> str: ...
    @overload
    def tag_bind(self, tagName: str, sequence: Optional[str], func: str, add: Optional[bool] = ...) -> None: ...
    def tag_unbind(self, tagName: str, sequence: str, funcid: Optional[str] = ...) -> None: ...
    def tag_cget(self, tagName, option): ...
    def tag_configure(self, tagName, cnf: Optional[Any] = ..., **kw): ...
    tag_config: Any
    def tag_delete(self, *tagNames): ...
    def tag_lower(self, tagName, belowThis: Optional[Any] = ...): ...
    def tag_names(self, index: Optional[Any] = ...): ...
    def tag_nextrange(self, tagName, index1, index2: Optional[Any] = ...): ...
    def tag_prevrange(self, tagName, index1, index2: Optional[Any] = ...): ...
    def tag_raise(self, tagName, aboveThis: Optional[Any] = ...): ...
    def tag_ranges(self, tagName): ...
    def tag_remove(self, tagName, index1, index2: Optional[Any] = ...): ...
    def window_cget(self, index, option): ...
    def window_configure(self, index, cnf: Optional[Any] = ..., **kw): ...
    window_config: Any
    def window_create(self, index, cnf=..., **kw): ...
    def window_names(self): ...
    def yview_pickplace(self, *what): ...

class _setit:
    def __init__(self, var, value, callback: Optional[Any] = ...): ...
    def __call__(self, *args): ...

class OptionMenu(Menubutton):
    widgetName: Any
    menuname: Any
    def __init__(self, master, variable, value, *values, **kwargs): ...
    def __getitem__(self, name): ...
    def destroy(self): ...

class Image:
    name: Any
    tk: Any
    def __init__(self, imgtype, name: Optional[Any] = ..., cnf=..., master: Optional[Any] = ..., **kw): ...
    def __del__(self): ...
    def __setitem__(self, key, value): ...
    def __getitem__(self, key): ...
    def configure(self, **kw): ...
    config: Any
    def height(self): ...
    def type(self): ...
    def width(self): ...

class PhotoImage(Image):
    def __init__(self, name: Optional[Any] = ..., cnf=..., master: Optional[Any] = ..., **kw): ...
    def blank(self): ...
    def cget(self, option): ...
    def __getitem__(self, key): ...
    def copy(self): ...
    def zoom(self, x, y: str = ...): ...
    def subsample(self, x, y: str = ...): ...
    def get(self, x, y): ...
    def put(self, data, to: Optional[Any] = ...): ...
    def write(self, filename, format: Optional[Any] = ..., from_coords: Optional[Any] = ...): ...
    if sys.version_info >= (3, 8):
        def transparency_get(self, x: int, y: int) -> bool: ...
        def transparency_set(self, x: int, y: int, boolean: bool) -> None: ...

class BitmapImage(Image):
    def __init__(self, name: Optional[Any] = ..., cnf=..., master: Optional[Any] = ..., **kw): ...

def image_names(): ...
def image_types(): ...

class Spinbox(Widget, XView):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def bbox(self, index): ...
    def delete(self, first, last: Optional[Any] = ...): ...
    def get(self): ...
    def icursor(self, index): ...
    def identify(self, x, y): ...
    def index(self, index): ...
    def insert(self, index, s): ...
    def invoke(self, element): ...
    def scan(self, *args): ...
    def scan_mark(self, x): ...
    def scan_dragto(self, x): ...
    def selection(self, *args: Any) -> Tuple[int, ...]: ...
    def selection_adjust(self, index): ...
    def selection_clear(self): ...
    def selection_element(self, element: Optional[Any] = ...): ...
    if sys.version_info >= (3, 8):
        def selection_from(self, index: int) -> None: ...
        def selection_present(self) -> None: ...
        def selection_range(self, start: int, end: int) -> None: ...
        def selection_to(self, index: int) -> None: ...

class LabelFrame(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...

class PanedWindow(Widget):
    def __init__(self, master: Optional[Any] = ..., cnf=..., **kw): ...
    def add(self, child, **kw): ...
    def remove(self, child): ...
    forget: Any
    def identify(self, x, y): ...
    def proxy(self, *args): ...
    def proxy_coord(self): ...
    def proxy_forget(self): ...
    def proxy_place(self, x, y): ...
    def sash(self, *args): ...
    def sash_coord(self, index): ...
    def sash_mark(self, index): ...
    def sash_place(self, index, x, y): ...
    def panecget(self, child, option): ...
    def paneconfigure(self, tagOrId, cnf: Optional[Any] = ..., **kw): ...
    paneconfig: Any
    def panes(self): ...
