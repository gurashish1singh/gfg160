from __future__ import annotations

from typing import MutableSequence

import array

from common import get_solution


def reverse_array_with_temp_array(input_array: MutableSequence) -> MutableSequence:
    """
    Given an array, reverse the array and return it.
    We use a temp array in this trivial solution.
    TC: O(n)
    SC: O(n)
    """
    length = len(input_array)
    if length < 2:
        return input_array

    temp_array = array.array("i", [] * length)
    for i, number in enumerate(input_array, start=1):
        temp_array.insert(-i, number)

    return temp_array


def reverse_array_with_pointers(input_array: MutableSequence) -> MutableSequence:
    """
    Given an array, reverse the array and return it.
    Here we use two pointers to swap the values from each end of the array
    TC: O(n)
    SC: O(1) -> no extra space is being usd
    """
    length = len(input_array)
    if length < 2:
        return input_array

    i = 0
    j = length - 1

    # We go uptil the middle and keep swapping values from each end
    # We can also use i < j instead of using length // 2
    while i < length // 2:
        input_array[i], input_array[j] = input_array[j], input_array[i]
        i += 1
        j -= 1

    return input_array


if __name__ == "__main__":
    """
    WE ASSUME THAT INPUT WILL ALWAYS BE AN ARRAY OF INTEGERS
    """
    lst1 = [1, 4, 5, 6, 7]
    input1 = array.array("i", lst1)
    out1 = array.array("i", lst1[::-1])
    get_solution(reverse_array_with_temp_array, _input=input1, expected_output=out1)

    lst2 = [2, 4, 5, 1]
    input2 = array.array("i", lst2)
    out2 = array.array("i", lst2[::-1])
    get_solution(reverse_array_with_temp_array, _input=input2, expected_output=out2)

    lst3 = [5, 3, 2, 5, 6, 7, 1]
    input3 = array.array("i", lst3)
    out3 = array.array("i", lst3[::-1])
    get_solution(reverse_array_with_pointers, _input=input3, expected_output=out3)

    lst4 = [5, 3, 2, 5, 6, 7, 1, 2]
    input4 = array.array("i", lst4)
    out4 = array.array("i", lst4[::-1])
    get_solution(reverse_array_with_pointers, _input=input4, expected_output=out4)
