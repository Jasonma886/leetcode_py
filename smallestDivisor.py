# 1283. Find the Smallest Divisor Given a Threshold

import math


def smallestDivisor(nums, threshold):
    biggest = 0
    result = 0
    for idx, val in enumerate(nums):
        if val <= threshold:
            s = 0
            for x in nums:
                s += math.ceil(x / val)
            if biggest < s:
                biggest = s
                result = val

    return result


if __name__ == '__main__':
    print(smallestDivisor([2, 3, 5, 7, 11], 11))
