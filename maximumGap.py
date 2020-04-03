import math
def MineMaximumGap(nums):
    print(nums)
    if len(nums) < 2:
        return 0

    nums = sorted(nums)
    gaps = []
    index = 1
    while index < len(nums):
        gaps.append(nums[index] - nums[index - 1])
        index += 1

    return max(gaps)


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    max_num = max(nums)
    min_num = min(nums)
    length = len(nums)
    if max_num == min_num:
        return 0

    interval = math.ceil((max_num - min_num) / (length - 1))



if __name__ == '__main__':
    print(MineMaximumGap([3, 6, 9, 1]))
