#!/usr/bin/env python3
from typing import Callable, Literal, TypedDict
import pysam
import pybedtools
import numpy as np
# Type hints!
# Variable annotations
# So many things with type hints.


def numToFloat(x: int) -> float:
    return x

print(numToFloat("5"))


def useNum() -> None:
    for i in range(numToFloat(5)):
        print(i)


useNum()


def makeWhitelistSegments(genome: pysam.FastaFile,
                          blacklist: pybedtools.BedTool | None = None) -> pybedtools.BedTool:
    """Get a list of windows where it is safe to draw inputs for your model.

    :param genome: A FastaFile (pysam object, not a string filename!).
    :param blacklist: (Optional) A BedTool that gives additional regions that should
        be excluded.
    :return: A BedTool that contains the whitelisted regions.
    """
    # Even though the types were not annotated in the docs, they
    # will be collected from the signature by autodoc.


def _findNonN(inSeq: np.ndarray, chromName: str) -> list[pybedtools.Interval]:
    ...


def resize(interval: pybedtools.Interval, mode: str, width: int,
           genome: pysam.FastaFile | None = None) -> pybedtools.Interval | Literal[False]:
    ...


class ApplyAdaptiveCountsLoss(object):

    heads: list[dict]
    aggression: float
    logsHistory: list[dict]
    λHistory: dict[str, list]

    def __init__(self, heads: list[dict], aggression: float):
        """Build the callback."""
        ...



def couldBeNone(arg: int | None) -> int:
    return arg + 2


def couldBeNone2(arg: int | None) -> int:
    assert arg is not None, "None param not supported!"
    return arg + 2


def wrongReturn() -> None:
    return 5


type GA_ANNOTATION_T = tuple[tuple[int, int], str, str] \
    | tuple[tuple[int, int], str, str, float, float]
"""The shape for an annotation object to pass to :func:`plotTraces`.

It contains:

1. a pair of integers, giving the start and stop points of that annotation,
2. a string giving its label,
3. a string giving its color,
4. (Optional) a float giving the bottom of its annotation box, and
5. (Optional) a float giving the top of its annotation box.

"""


type COLOR_SPEC_T = \
    dict[Literal["rgb"], tuple[float, float, float]] | \
    dict[Literal["rgba"], tuple[float, float, float, float]] | \
    dict[Literal["tol"], int] | \
    dict[Literal["tol-light"], int] | \
    dict[Literal["ibm"], int] | \
    dict[Literal["wong"], int] | \
    tuple[float, float, float] | \
    tuple[float, float, float, float]


class ANNOTATION_T(TypedDict):
    """Represents a genomic region of interest. Includes color and a name.

    start
        the start point of the annotation, in genomic coordinates.
    end
        The end point of the annotation, in genomic coordinates.
    name
        The string giving the name of the annotation.
    color
        a :py:data:`COLOR_SPEC_T` giving the color to use when drawing
        the annotation
    bottom
        As a fraction of the window height for annotations, where should this one's box start?
        (Optional, default: 0)
    top
        As a fraction of the window height for annotations, where should this one's box end?
        (Optional, default: 1.0)

    """

    start: int
    end: int
    name: str
    color: COLOR_SPEC_T
    bottom: float
    top: float


def setScore(scoreFn: Callable[[GA_ANNOTATION_T, list[np.ndarray]], float]) -> None:
    ...


def smartEditor() -> None:
    stuff = {1: "a", 2: "b"}

    stuff[3] = "c"
    stuff["d"] = 4

    # Use a variable annotation.
    stuff2: dict[int | str, int | str] = {1: "a", 2: "b"}

    stuff2[3] = "c"
    stuff2["d"] = 4

    # Use a variable annotation.
    stuff3: dict = {1: "a", 2: "b"}

    stuff3[3] = "c"
    stuff3["d"] = 4



# f-strings

def fStrings() -> None:
    x = "some string"
    print(f"The string is {x}.")

    # f-strings support nested quotes.
    x = {"abc": 5.6}
    print(f"value is {x["abc"] + 3}")
    # You can use an = format specifier to give the variable name, useful for debugging!
    print(f"Parameters: {x=}")

    # And the format specifier has most of the same semantics as string.format():
    fv = 8.2512121235
    print(f"{fv:8.3f}")

    # Even complex things can be injected into an f-string.
    prtStr = f"{fv:6.2f}"
    print(f"{len(prtStr)} or {len(prtStr.strip())}")


fStrings()

# Ordered dict literals and dict unions.

def dictsAreOrdered() -> None:
    stuff: dict = {3: "first", 2: "second", "one": "third"}
    for k, v in stuff.items():
        print(k, v)
    print()
    stuff[2] = None
    stuff[16] = 8
    for k, v in stuff.items():
        print(k, v)
dictsAreOrdered()

def dictUnion() -> None:
    d1 = {1: 10, 2: 20, 3: 30}
    d2 = {"a": "A", "b": "B", "c": "C"}
    print(d1 | d2)
    d3 = {1: 11, 4: 44}
    print(d1 | d3)
    print(d3 | d1)

    # also
    d1 |= d3
    print(d1)
dictUnion()

# Assignment expressions

def useAssign() -> None:
    a = list(range(20))
    if (n := len(a)) > 10:
        print(f"a is too long, got {n} but expected 10!")
    print(n)
    # Very handy for reading over files.
    with open("/etc/man_db.conf", "r") as fp:
        while (block := fp.read(256)) != "":
            print(block[0], end="")
    print()

    # "Try to limit the use of the walrus operator to clean cases that reduce complexity
    # and improve readability.


useAssign()

# Match operator

def useMatch() -> None:
    def process(toEval: str) -> int:
        vsp = toEval.split()

        match toEval.split():
            case [lhs, "+", rhs]:
                return int(lhs) + int(rhs)
            case [lhs, "-", rhs]:
                return int(lhs) - int(rhs)
            case ["sum", *rest]:
                return sum([int(x) for x in rest])
            case ["True"] | ["False"] as arg:
                return bool(arg) * 1
            case [val] if val in ["1", "2", "3"]:
                print(f"Intercepted {val=}")
                return int(val)
            case [val]:
                return int(val)
            case _:
                raise SyntaxError(f"Could not parse {toEval=}")
    cmd = "2 + 2"
    print(process(cmd))
    print(process("1 - 6"))
    print(process("4"))
    print(process("1"))
    print(process("sum 2 3 4 5 6"))
    print(process("True"))

    # The interpreter shows how to mix this with objects.
    def withClass(v):
        match v:
            case str(x):
                print(f"Got string {x.strip()}")
            case int(x):
                print(f"Got int {x=}")
            case float():
                print(f"Found a float in {v=}")
    withClass("abc")
    withClass(6.3)
    withClass(6)

useMatch()
# The GIL is now optional.

