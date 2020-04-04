# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# class NumArray(object):
#
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#         self.length = len(nums)
#         self.dict = {}
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         if i >= self.length:
#             return 0
#         if not (i, j) in self.dict:
#             temp = self.nums[i:j + 1]
#             self.dict[(i, j)] = sum(temp)
#
#         return self.dict[(i, j)]

class NumArray(object):
    def __init__(self, nums):
        self.sums = [0]
        sum = 0
        for num in nums:
            sum += num
            self.sums.append(sum)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]


if __name__ == '__main__':
    test = NumArray([2, 3, 4, 5, -2])
    print(test.sumRange(2, 4))
