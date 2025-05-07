"""
Given an unsorted array, rotate to the left - counter clockwise direction by D steps
where D is a positive integer. Change the array in place.
"""

from __future__ import annotations

from typing import MutableSequence

import array
from functools import partial

from common import get_solution


def rotate_array(input_array: MutableSequence, number_of_rotations: int) -> MutableSequence:
    """
    TC: O(n * d) -> since we are looping d times
    SC: O(1) -> we are nto using any extra space
    """
    length = len(input_array)
    if length < 2:
        return input_array

    if number_of_rotations in (0, length):
        return input_array

    for _ in range(number_of_rotations):
        # We loop based on number of rotations
        # We grab the first number from the array and then
        # loop through the array from the 2nd number while replacing
        # the previous index with the current number.
        first_number = input_array[0]
        for i, number in enumerate(input_array[1:]):
            input_array[i] = number

        # finally we put the first number at the last index
        input_array[-1] = first_number

    return input_array


def rotate_array_to_the_right(
    input_array: MutableSequence, number_of_rotations: int
) -> MutableSequence:
    """
    We reverse the array first, then we mod the number of rotations
    with the length of the array. We then reverse the first K items
    and then reverse the rest of the items.
    TC: O(1) -> We are doing everything in memory
    SC: O(1) -> we are nnotto using any extra space
    """
    left = 0
    length = len(input_array)
    right = length - 1

    # mod the number of rotations
    number_of_rotations %= length

    # first we reverse the whole array
    _reverse_subset(input_array, left, right)

    # reverse the first items till number_of_rotations index
    left = 0
    right = number_of_rotations - 1
    _reverse_subset(input_array, left, right)

    # now we reverse the remainder of the items
    left = number_of_rotations
    right = length - 1
    _reverse_subset(input_array, left, right)

    return input_array


def _reverse_subset(arr: MutableSequence, left_index: int, right_index: int) -> None:
    # Operation is done in place
    while left_index < right_index:
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        left_index += 1
        right_index -= 1


if __name__ == "__main__":
    """
    WE ASSUME THAT INPUT WILL ALWAYS BE AN ARRAY OF INTEGERS
    """
    lst1 = [1, 4, 5, 6, 7]
    input1 = array.array("i", lst1)
    out1 = array.array("i", lst1)
    get_solution(partial(rotate_array, number_of_rotations=0), _input=input1, expected_output=out1)

    lst2 = [1, 4, 5, 6, 7]
    input2 = array.array("i", lst2)
    out2 = array.array("i", [4, 5, 6, 7, 1])
    get_solution(
        partial(rotate_array, number_of_rotations=1),
        _input=input2,
        expected_output=out2,
    )

    lst3 = [1, 4, 5, 6, 7]
    input3 = array.array("i", lst3)
    out3 = array.array("i", [6, 7, 1, 4, 5])
    get_solution(
        partial(rotate_array, number_of_rotations=8),
        _input=input3,
        expected_output=out3,
    )

    lst4 = [1, 4, 5, 6, 7]
    input4 = array.array("i", lst4)
    out4 = array.array("i", lst4)
    get_solution(
        partial(rotate_array, number_of_rotations=5),
        _input=input4,
        expected_output=out4,
    )

    lst5 = [1, 4, 5, 6, 7]
    input5 = array.array("i", lst5)
    out5 = array.array("i", [5, 6, 7, 1, 4])
    get_solution(
        partial(rotate_array_to_the_right, number_of_rotations=8),
        _input=input5,
        expected_output=out5,
    )

    lst6 = [1, 4, 5, 6, 7]
    input6 = array.array("i", lst6)
    out6 = array.array("i", lst6)
    get_solution(
        partial(rotate_array_to_the_right, number_of_rotations=5),
        _input=input6,
        expected_output=out6,
    )

    lst7 = [-1, -100, 3, 99]
    input7 = array.array("i", lst7)
    out7 = array.array("i", [3, 99, -1, -100])
    get_solution(
        partial(rotate_array_to_the_right, number_of_rotations=2),
        _input=input7,
        expected_output=out7,
    )

    lst8 = [1, 2, 3, 4, 5, 6]
    input8 = array.array("i", lst8)
    out8 = array.array("i", [5, 6, 1, 2, 3, 4])
    get_solution(
        partial(rotate_array_to_the_right, number_of_rotations=2),
        _input=input8,
        expected_output=out8,
    )
