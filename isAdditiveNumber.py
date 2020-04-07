from itertools import combinations


def isAdditiveNumber(num):
    l = len(num)
    for i, j in combinations(range(1, l), 2):
        s1 = num[:i]
        s2 = num[i: j]
        temp = str(int(s1) + int(s2))
        if s1 != str(int(s1)) or s2 != str(int(s2)):
            continue
        while num.startswith(temp, j) and j < l:
            j += len(temp)
            s1, s2 = s2, temp
            temp = str(int(s1) + int(s2))

        if j == l:
            return True

    return False


if __name__ == '__main__':
    isAdditiveNumber('123123')
