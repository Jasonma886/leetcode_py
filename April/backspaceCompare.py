class Solution:
    def backspaceCompare(self, S, T):
        def transfer(s):
            while '#' in s:
                index = s.index('#')
                if index == 0:
                    s = s[1:]
                else:
                    s = s[0:index - 1] + s[index + 1:]

            return s

        if S == T: return True
        S = transfer(S)
        T = transfer(T)
        return S == T
