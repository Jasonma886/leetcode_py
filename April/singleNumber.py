from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        while len(nums) > 0:
            n = nums.pop()
            if n in nums:
                del nums[nums.index(n)]
            else:
                return n
        return None


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        temp = defaultdict(bool)
        while len(nums) > 0:
            n = nums.pop()
            temp[n] = not temp[n]
            if not temp[n]:
                del temp[n]

        return list(temp.keys())[0]