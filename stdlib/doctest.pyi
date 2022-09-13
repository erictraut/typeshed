import types
import unittest
from _typeshed import ExcInfo
from collections.abc import Callable
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

__all__ = [
    "register_optionflag",
    "DONT_ACCEPT_TRUE_FOR_1",
    "DONT_ACCEPT_BLANKLINE",
    "NORMALIZE_WHITESPACE",
    "ELLIPSIS",
    "SKIP",
    "IGNORE_EXCEPTION_DETAIL",
    "COMPARISON_FLAGS",
    "REPORT_UDIFF",
    "REPORT_CDIFF",
    "REPORT_NDIFF",
    "REPORT_ONLY_FIRST_FAILURE",
    "REPORTING_FLAGS",
    "FAIL_FAST",
    "Example",
    "DocTest",
    "DocTestParser",
    "DocTestFinder",
    "DocTestRunner",
    "OutputChecker",
    "DocTestFailure",
    "UnexpectedException",
    "DebugRunner",
    "testmod",
    "testfile",
    "run_docstring_examples",
    "DocTestSuite",
    "DocFileSuite",
    "set_unittest_reportflags",
    "script_from_examples",
    "testsource",
    "debug_src",
    "debug",
]

class TestResults(NamedTuple):
    failed: int
    attempted: int

OPTIONFLAGS_BY_NAME: dict[str, int]

def register_optionflag(name: str) -> int: ...

DONT_ACCEPT_TRUE_FOR_1: int
DONT_ACCEPT_BLANKLINE: int
NORMALIZE_WHITESPACE: int
ELLIPSIS: int
SKIP: int
IGNORE_EXCEPTION_DETAIL: int

COMPARISON_FLAGS: int

REPORT_UDIFF: int
REPORT_CDIFF: int
REPORT_NDIFF: int
REPORT_ONLY_FIRST_FAILURE: int
FAIL_FAST: int

REPORTING_FLAGS: int

BLANKLINE_MARKER: str
ELLIPSIS_MARKER: str

class Example:
    source: str
    want: str
    exc_msg: str | None
    lineno: int
    indent: int
    options: dict[int, bool]
    def __init__(
        self,
        source: str,
        want: str,
        exc_msg: str | None = ...,
        lineno: int = ...,
        indent: int = ...,
        options: dict[int, bool] | None = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class DocTest:
    examples: list[Example]
    globs: dict[str, Any]
    name: str
    filename: str | None
    lineno: int | None
    docstring: str | None
    def __init__(
        self,
        examples: list[Example],
        globs: dict[str, Any],
        name: str,
        filename: str | None,
        lineno: int | None,
        docstring: str | None,
    ) -> None: ...
    def __lt__(self, other: DocTest) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class DocTestParser:
    def parse(self, string: str, name: str = ...) -> list[str | Example]: ...
    def get_doctest(self, string: str, globs: dict[str, Any], name: str, filename: str | None, lineno: int | None) -> DocTest: ...
    def get_examples(self, string: str, name: str = ...) -> list[Example]: ...

class DocTestFinder:
    def __init__(
        self, verbose: bool = ..., parser: DocTestParser = ..., recurse: bool = ..., exclude_empty: bool = ...
    ) -> None: ...
    def find(
        self,
        obj: object,
        name: str | None = ...,
        module: None | bool | types.ModuleType = ...,
        globs: dict[str, Any] | None = ...,
        extraglobs: dict[str, Any] | None = ...,
    ) -> list[DocTest]: ...

_Out: TypeAlias = Callable[[str], object]

class DocTestRunner:
    DIVIDER: str
    optionflags: int
    original_optionflags: int
    tries: int
    failures: int
    test: DocTest
    def __init__(self, checker: OutputChecker | None = ..., verbose: bool | None = ..., optionflags: int = ...) -> None: ...
    def report_start(self, out: _Out, test: DocTest, example: Example) -> None: ...
    def report_success(self, out: _Out, test: DocTest, example: Example, got: str) -> None: ...
    def report_failure(self, out: _Out, test: DocTest, example: Example, got: str) -> None: ...
    def report_unexpected_exception(self, out: _Out, test: DocTest, example: Example, exc_info: ExcInfo) -> None: ...
    def run(
        self, test: DocTest, compileflags: int | None = ..., out: _Out | None = ..., clear_globs: bool = ...
    ) -> TestResults: ...
    def summarize(self, verbose: bool | None = ...) -> TestResults: ...
    def merge(self, other: DocTestRunner) -> None: ...

class OutputChecker:
    def check_output(self, want: str, got: str, optionflags: int) -> bool: ...
    def output_difference(self, example: Example, got: str, optionflags: int) -> str: ...

class DocTestFailure(Exception):
    test: DocTest
    example: Example
    got: str
    def __init__(self, test: DocTest, example: Example, got: str) -> None: ...

class UnexpectedException(Exception):
    test: DocTest
    example: Example
    exc_info: ExcInfo
    def __init__(self, test: DocTest, example: Example, exc_info: ExcInfo) -> None: ...

class DebugRunner(DocTestRunner): ...

master: DocTestRunner | None

def testmod(
    m: types.ModuleType | None = ...,
    name: str | None = ...,
    globs: dict[str, Any] | None = ...,
    verbose: bool | None = ...,
    report: bool = ...,
    optionflags: int = ...,
    extraglobs: dict[str, Any] | None = ...,
    raise_on_error: bool = ...,
    exclude_empty: bool = ...,
) -> TestResults: ...
def testfile(
    filename: str,
    module_relative: bool = ...,
    name: str | None = ...,
    package: None | str | types.ModuleType = ...,
    globs: dict[str, Any] | None = ...,
    verbose: bool | None = ...,
    report: bool = ...,
    optionflags: int = ...,
    extraglobs: dict[str, Any] | None = ...,
    raise_on_error: bool = ...,
    parser: DocTestParser = ...,
    encoding: str | None = ...,
) -> TestResults: ...
def run_docstring_examples(
    f: object, globs: dict[str, Any], verbose: bool = ..., name: str = ..., compileflags: int | None = ..., optionflags: int = ...
) -> None: ...
def set_unittest_reportflags(flags: int) -> int: ...

class DocTestCase(unittest.TestCase):
    def __init__(
        self,
        test: DocTest,
        optionflags: int = ...,
        setUp: Callable[[DocTest], object] | None = ...,
        tearDown: Callable[[DocTest], object] | None = ...,
        checker: OutputChecker | None = ...,
    ) -> None: ...
    def runTest(self) -> None: ...
    def format_failure(self, err: str) -> str: ...
    def __eq__(self, other: object) -> bool: ...

class SkipDocTestCase(DocTestCase):
    def __init__(self, module: types.ModuleType) -> None: ...
    def test_skip(self) -> None: ...

class _DocTestSuite(unittest.TestSuite): ...

def DocTestSuite(
    module: None | str | types.ModuleType = ...,
    globs: dict[str, Any] | None = ...,
    extraglobs: dict[str, Any] | None = ...,
    test_finder: DocTestFinder | None = ...,
    **options: Any,
) -> _DocTestSuite: ...

class DocFileCase(DocTestCase): ...

def DocFileTest(
    path: str,
    module_relative: bool = ...,
    package: None | str | types.ModuleType = ...,
    globs: dict[str, Any] | None = ...,
    parser: DocTestParser = ...,
    encoding: str | None = ...,
    **options: Any,
) -> DocFileCase: ...
def DocFileSuite(*paths: str, **kw: Any) -> _DocTestSuite: ...
def script_from_examples(s: str) -> str: ...
def testsource(module: None | str | types.ModuleType, name: str) -> str: ...
def debug_src(src: str, pm: bool = ..., globs: dict[str, Any] | None = ...) -> None: ...
def debug_script(src: str, pm: bool = ..., globs: dict[str, Any] | None = ...) -> None: ...
def debug(module: None | str | types.ModuleType, name: str, pm: bool = ...) -> None: ...
