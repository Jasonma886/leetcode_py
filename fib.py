class Solution(object):
    def __init__(self):
        self.cached = {}

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        if N not in self.cached:
            self.cached[N] = self.fib(N - 1) + self.fib(N - 2)

        return self.cached[N]

# 0112358
if __name__ == '__main__':
    # print(fib(6))
    test = Solution()
    print(test.fib(6))