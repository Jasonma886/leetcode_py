
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """


target = TreeNode(3)
original = TreeNode([7, 4, 3, None, None, 6, 19])

if __name__ == '__main__':
    test = Solution()
    test.getTargetCopy(original, original, target)