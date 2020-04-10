from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        def recursive(m: int, cached: List) -> bool:
            if m == 1:
                return True
            if m in cached:
                return False
            cached.append(m)
            result = 0
            for i in str(m):
                result += int(i) ** 2
            return recursive(result, cached)

        return recursive(n, [])



if __name__ == '__main__':
    test = Solution()
    print(test.isHappy(19))