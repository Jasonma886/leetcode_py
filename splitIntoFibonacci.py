from itertools import combinations
from math import pow


def splitIntoFibonacci(S):
    l = len(S)
    limit = int(pow(2, 31) - 1)

    def isValid(num):
        return int(num) < limit

    for i, j in combinations(range(1, l), 2):
        s1 = S[:i]
        s2 = S[i:j]
        # if s1 or s2 starts with '0', then continue to next one.
        if str(int(s1)) != s1 or str(int(s2)) != s2:
            continue
        s3 = str(int(s1) + int(s2))
        res = [s1, s2]
        while S.startswith(s3, j):
            if not isValid(s3):
                break
            res.append(s3)
            j += len(s3)
            s1, s2 = s2, s3
            s3 = str(int(s1) + int(s2))

        if j == l:
            return res

    return []


if __name__ == '__main__':
    print(splitIntoFibonacci(
        "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
