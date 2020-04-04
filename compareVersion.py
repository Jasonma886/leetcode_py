# 165. Compare Version Numbers
from itertools import zip_longest

class Solution:
    def cmp(self, a, b):
        return (a > b) - (a < b)

    def compareVersion(self, version1, version2):
        v1_parts = map(int, version1.split('.'))
        v2_parts = map(int, version2.split('.'))
        for v1, v2 in zip_longest(v1_parts, v2_parts, fillvalue=0):
            res = self.cmp(v1, v2)
            if res != 0:
                return res

        return 0

def compareVersion(version1, version2):
    v1, v2 = version1.split('.'), version2.split('.')
    len1 = len(v1)
    len2 = len(v2)
    i = 0
    while i < len1 or i < len2:
        if i < len1 and i < len2:
            a = int(v1[i])
            b = int(v2[i])
            if a > b:
                return 1
            elif a < b:
                return -1
        elif i < len1:
            a = int(v1[i])
            if a > 0:
                return 1
        elif i < len2:
            b = int(v2[i])
            if b > 0:
                return -1

        i += 1

    return 0


if __name__ == '__main__':
    # print(compareVersion('7.05.2.4', '7.5.2'))
    test = Solution()
    print(test.compareVersion('7.05.2.4.0.0.0.4.4.4', '7.5.2'))
    print(compareVersion('7.05.2.4.0.0.0.4.4.4', '7.5.2'))
