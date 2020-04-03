class solution(object):
    def findLongest(self, s):
        sub_str = []
        max_length = 0
        for i in s:
            if i in sub_str:
                sub_str = sub_str[sub_str.index(i) + 1:]
            sub_str.append(i)
            max_length = max(max_length, len(sub_str))

        return max_length

if __name__ == '__main__':
    result = solution()
    print(result.findLongest('asdfazxcvbnm'))