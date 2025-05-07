from __future__ import annotations

from typing import (
    Any,
    Callable,
)

from copy import deepcopy
from functools import partial


def get_solution(func: Callable | partial, _input: Any, expected_output: Any) -> Any:
    original_input = deepcopy(_input)
    actual_output = func(_input)
    print(f"Output for {original_input=} is {actual_output}")
    assert actual_output == expected_output, f"{actual_output=} does not match {expected_output=}"
