from itertools import combinations
from collections import defaultdict

def lenLongestFibSubseq(A):
    res = []
    l = len(A)
    for a, b, c in combinations(range(0, l - 1), 3):
        if A[a] + A[b] != A[c]:
            continue
        temp = [A[a], A[b], A[c]]
        a, b = b, c
        while c <= l - 1:
            if A[a] + A[b] == A[c]:
                a, b = b, c
                temp.append(A[c])
            c += 1
        if len(temp) > len(res):
            res = temp

    return res

class Solution(object):
    # 动态规划(dp)
    def lenLongestFibSubseq(self, A):
        dp = defaultdict(int)
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])

if __name__ == '__main__':
    print(lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))