# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = n
        while a < b:
            mid = (a + b) // 2
            if isBadVersion(mid):
                b = mid
            else:
                a = mid + 1
        return a



if __name__ == '__main__':
    test = Solution()
    print(test.firstBadVersion(5))
