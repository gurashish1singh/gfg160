from __future__ import annotations

from typing import MutableSequence

import array

from common import get_solution


def insert_zeroes_at_end_with_temp_array(input_array: MutableSequence) -> MutableSequence:
    """
    This is a solution where we can use a temp array.
    Given an array, move all zeroes to the end.
    TC: O(n) -> only one traversal
    SC: O(n) -> 2 arrays being used
    """
    length = len(input_array)
    if length < 2:
        return input_array

    temp_array = array.array("i", [] * length)
    zero_count = 0
    for number in input_array:
        if number != 0:
            temp_array.append(number)
        else:
            zero_count += 1

    for zeroes in range(zero_count):
        temp_array.append(0)

    return temp_array


def insert_zeroes_at_end(input_array: MutableSequence) -> MutableSequence:
    """
    This solution uses 2 pointers. 1 pointer will keep incrememnting
    to check if current value is non-zero, 2nd pointr will keep track of empty positions.
    We do iterate twice in this solution.
    TC: O(2n) ~ O(n)
    SC: O(1) -> no extra array was used
    """
    length = len(input_array)
    if length < 2:
        return input_array

    count = 0
    for i, number in enumerate(input_array):
        if number != 0:
            # For every non-zero number, we assign the number at the "count" index as the number from "i" index.
            # Then we incrememnt the count value.
            input_array[count] = input_array[i]
            count += 1

    for i in range(count, length):
        # This means there were zeroes present in the array and we have to add them to the end
        input_array[i] = 0

    return input_array


def insert_zeroes_at_end_with_swap(input_array: MutableSequence) -> MutableSequence:
    """
    This solution uses 2 pointers. 1 pointer will keep incrememnting
    to check if current value is non-zero, 2nd pointer tracks the zeroes and we swap
    the non-zero and zero values in place.
    TC: O(2n) ~ O(n)
    SC: O(1) -> no extra array was used
    """
    length = len(input_array)
    if length < 2:
        return input_array

    count = 0
    for i, number in enumerate(input_array):
        if number != 0:
            # For every non-zero number, we swap the number at the "count" index and "i" index.
            # Then we increment the count value.
            # NOTE: We only incrememt count for every non-zero value. This is how we are able to
            # accurately swap non-zero values with zeroes.
            input_array[i], input_array[count] = input_array[count], input_array[i]
            count += 1

    return input_array


if __name__ == "__main__":
    """
    WE ASSUME THAT INPUT WILL ALWAYS BE AN ARRAY OF INTEGERS
    """
    input1 = array.array("i", [1, 0, 2, 4, 0, 3, 5, 0])
    out1 = array.array("i", [1, 2, 4, 3, 5, 0, 0, 0])
    get_solution(func=insert_zeroes_at_end_with_temp_array, _input=input1, expected_output=out1)

    input2 = array.array("i", [1, 2])
    out2 = array.array("i", [1, 2])
    get_solution(
        func=insert_zeroes_at_end_with_temp_array, _input=input2, expected_output=out2
    )

    input3 = array.array("i", [1, 2])
    out3 = array.array("i", [1, 2])
    get_solution(
        func=insert_zeroes_at_end, _input=input3, expected_output=out3
    )

    input4 = array.array("i", [1, 0, 2, 4, 0, 3, 5, 0])
    out4 = array.array("i", [1, 2, 4, 3, 5, 0, 0, 0])
    get_solution(func=insert_zeroes_at_end, _input=input4, expected_output=out4)

    input5 = array.array("i", [1, 2])
    out5 = array.array("i", [1, 2])
    get_solution(
        func=insert_zeroes_at_end_with_swap, _input=input5, expected_output=out5
    )

    input6 = array.array("i", [1, 0, 2, 4, 0, 3, 5, 0])
    out6 = array.array("i", [1, 2, 4, 3, 5, 0, 0, 0])
    get_solution(func=insert_zeroes_at_end_with_swap, _input=input6, expected_output=out6)

    input7 = array.array("i", [0, 0, 0])
    out7 = array.array("i", [0, 0, 0])
    get_solution(
        func=insert_zeroes_at_end_with_swap, _input=input7, expected_output=out7
    )

    input8 = array.array("i", [0, 0, 0, 4])
    out8 = array.array("i", [4, 0, 0, 0])
    get_solution(
        func=insert_zeroes_at_end_with_swap, _input=input8, expected_output=out8
    )

    input9 = array.array("i", [1, 2, 3, 4])
    out9 = array.array("i", [1, 2, 3, 4])
    get_solution(
        func=insert_zeroes_at_end_with_swap, _input=input9, expected_output=out9
    )
