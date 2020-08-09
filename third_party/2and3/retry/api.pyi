from logging import Logger
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, TypeVar, Union

_T = TypeVar("_T", bound=Callable[..., Any])
_Decorator = Callable[[_T], _T]
_R = TypeVar("_R")

def retry_call(
    f: Callable[..., _R],
    fargs: List[Any] = ...,
    fkwargs: Dict[str, Any] = ...,
    exceptions: Union[Type[Exception], Sequence[Type[Exception]]] = ...,
    tries: int = ...,
    delay: int = ...,
    max_delay: int = ...,
    backoff: int = ...,
    jitter: int = ...,
    logger: Optional[Logger] = ...,
) -> _R: ...
def retry(
    exceptions: Union[Type[Exception], Sequence[Type[Exception]]] = ...,
    tries: int = ...,
    delay: int = ...,
    max_delay: int = ...,
    backoff: int = ...,
    jitter: int = ...,
    logger: Optional[Logger] = ...,
) -> _Decorator: ...
