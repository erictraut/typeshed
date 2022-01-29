from typing import AnyStr, Iterable, Union

_EitherStr = Union[str, unicode]

def fnmatch(filename: _EitherStr, pattern: _EitherStr) -> bool: ...
def fnmatchcase(filename: _EitherStr, pattern: _EitherStr) -> bool: ...
def filter(names: Iterable[AnyStr], pattern: _EitherStr) -> list[AnyStr]: ...
def translate(pattern: AnyStr) -> AnyStr: ...
