from typing import List

def find_pair(nums: List[int], target: int) -> None:
    """function to find pairs of integers that sum a target value"""
    dict_num = {}
    pairs = []

    # do for in element and get key (position) and value of the number
    for key, value in enumerate(nums):
        # check if the needed number exists like a key in dict_num (key, target - num)
        # if the number exists, save the pair
        if (target - value) in dict_num:
            pairs.append((target - value, value))

        # save the current num value like a key in the dictionary
        dict_num[value] = key

    return pairs
