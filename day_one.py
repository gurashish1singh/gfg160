from __future__ import annotations

import sys

from common import get_solution


def find_second_largest_number(input_list: list[int]) -> int:
    """
    Find the 2nd largest number given a list of numbers
    - list could contain duplicates
    - list could contain all the same numbers - in this case we return -1
    - time complexity should be O(n) and space complexity should be O(1)
    """
    default = -1
    length = len(input_list)
    if length < 2:
        return default

    max_number = -sys.maxsize
    second_largest_number = -sys.maxsize

    for number in input_list:
        # if current number is greater than max, we update max number and
        # use the previous max as second largest value
        if number > max_number:
            second_largest_number = max_number
            max_number = number

        # we update second_largest_number if current number is less than max number
        # and greater than second_largest_number
        elif second_largest_number < number < max_number:
            second_largest_number = number

    # We return -1, if there no second largest numnber is found
    if second_largest_number in (-sys.maxsize, max_number):
        return default
    return second_largest_number


if __name__ == "__main__":
    input1 = []
    get_solution(func=find_second_largest_number, _input=input1, expected_output=-1)

    input2 = [5]
    get_solution(func=find_second_largest_number, _input=input2, expected_output=-1)

    input3 = [10, 10, 10]
    get_solution(func=find_second_largest_number, _input=input3, expected_output=-1)

    input4 = [10, 5, 10]
    get_solution(func=find_second_largest_number, _input=input4, expected_output=5)

    input5 = [10, 35, 11, 9, 5, 2]
    get_solution(func=find_second_largest_number, _input=input5, expected_output=11)

    input6 = [12, 35, 1, 10, 34, 1, 35]
    get_solution(func=find_second_largest_number, _input=input6, expected_output=34)
