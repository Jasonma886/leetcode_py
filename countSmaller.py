#!/usr/bin/env python2.7


# def countSmaller(nums):
#     result = []
#     for index, num in enumerate(nums):
#         temp = nums[index + 1:]
#         counter = 0
#         for x in temp:
#             if num > x:
#                 counter += 1
#
#         result.append(counter)
#
#     return result


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.count = 1


class Solution:
    def __init__(self):
        self.root = None
        self.count = 0

    def inset(self, root, val):
        if root == None:
            return Node(val)
        # print(root.val, val, root.count)
        root.count += 1
        if root.val >= val:
            if root.left:
                self.inset(root.left, val)
            else:
                root.left = Node(val)
        else:
            self.count += 1
            if root.left:
                self.count += root.left.count
            if root.right:
                self.inset(root.right, val)
            else:
                root.right = Node(val)

    def countSmaller(self, nums):
        if nums == []:
            return []
        if len(nums) == 1:
            return [0]

        output = [0]
        self.root = Node(nums[-1])

        for ele in nums[::-1][1:]:
            self.count = 0
            # print(ele)
            self.inset(self.root, ele)
            output.append(self.count)
            # print( )

        return output[::-1]

class Mine:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, root, val):
        current = root
        root.count += 1
        if current.val > val:
            current.count += 1
            if current.left:
                self.insert(current.left, val)
            else:
                current.left = Node(val)
        else:
            if current.right:
                self.insert(current.right, val)
            else:
                current.right = Node(val)


    def countSmaller(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]

        result = []
        self.root = Node(nums[-1])

        for num in nums[::-1][1:]:
            self.count = 0
            self.insert(self.root, num)



if __name__ == '__main__':
    # Mine().countSmaller([1,2])
    result = Mine()
    print(result.countSmaller(
        [5183, 2271, 3067, 539, 8939, 2999, 9264, 737, 3974, 5846, -210, 9278, 5800, 2675, 6608, 1133, -1, 6018, 9672,
         5179, 9842, 7424, -209, 2988, 2757, 5984, 1107, 2644, -499, 7234, 7539, 6525, 347, 5718, -742, 1797, 5292, 976,
         8752, 8297, 1312, 3385, 5924, 2882, 6091, -282, 2595, 96, 1906, 8014, 7667, 5895, 7283, 7974, -167, 7068, 3946,
         6223, 189, 1589, 2058, 9277, -302, 8157, 8256, 5261, 8067, 1071, 9470, 2682, 8197, 5632, 753, 3179, 8187, 9042,
         2438, 6431, 3945, 9539, 8608, 9383, 4757, 1675, 3448, 3436, 6238, 7946, -369, -693, 1382, 9774]))

