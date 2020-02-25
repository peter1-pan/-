#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def removeF(nums, val):
    for i, k in enumerate(nums):
        if k != val:
            nums[i] = k
    print(nums)
    print(len(nums))
    return len(nums)


nums = [3, 2, 2, 3]
val = 3
removeF(nums, val)
