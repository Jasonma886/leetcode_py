def smallerNumbersThanCurrent(nums):
    result = []
    clone = sorted(nums)
    for num in nums:
        result.append(clone.index(num))
    return result


if __name__ == '__main__':
    print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
