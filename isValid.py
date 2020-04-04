def myIsValid(s):
    stack = []
    left_part = ['[', '{', '(']
    d = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for word in s:
        if len(stack) == 0:
            if word not in left_part:
                return False
            else:
                stack.append(word)
                continue
        if word not in left_part:
            temp = stack.pop()
            if temp != d[word]:
                return False
        else:
            stack.append(word)
    return stack == []


def isValid(s):
    dic = {'(': 1, ')': 2, '[': 3, ']': 6, '{': 5, '}': 10}
    res = []
    for one in s:
        temp = dic[one]
        if (temp % 2):
            res.append(temp)
        else:
            if (len(res) and res[-1] == temp // 2):
                del res[-1]
            else:
                return False
    return res == []


if __name__ == '__main__':
    print(isValid('{[]}'))
