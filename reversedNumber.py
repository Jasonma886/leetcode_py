class solution(object):

    def reversedNumber(self, x):
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            strg = str(x)
        if x >= 0:
            revst = strg[::-1]
        else:
            temp = strg[1:]
            temp2 = temp[::-1]
            revst = "-" + temp2
        if int(revst) >= 2 ** 31 - 1 or int(revst) <= -2 ** 31:
            return 0
        else:
            return int(revst)

    def mime(self, x):
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0

        is_negative = 1
        if x < 0:
            is_negative = -1

        string = str(abs(x))
        result = ''
        for i in string:
            result = i + result

        return int(result) * is_negative

if __name__ == '__main__':
    test = solution()
    print(test.mime(1534236469))