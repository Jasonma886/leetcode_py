import re


def longestValidParentheses(s):
    reg = r'(\(\))?'
    match = re.findall(reg, s)
    lastOne = False
    res = []
    current = ''
    for i in match:
        if i and lastOne:
            current += i
        elif i and not lastOne:
            current = i
            lastOne = True
        elif not i and lastOne:
            res.append(current)
            lastOne = False

    if len(res) == 0:
        return 0
    return max(map(len, res))


def longestValidParentheses2(s):
    stack = [0]
    ml = 0
    for word in s:
        if word == ')':
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                ml = max(ml, stack[-1])
            else:
                stack = [0]
        else:
            stack.append(0)
    return ml


if __name__ == '__main__':
    print(longestValidParentheses(''))
    print(longestValidParentheses2('((((()()()((((()'))
