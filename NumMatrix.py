class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.cached = {}

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        x = row1
        sum = 0
        key = (row1, col1, row2, col2)
        if key not in self.cached:
            while x >= row1 and x <= row2:
                sub_list = self.matrix[x]
                y = col1
                while y >= col1 and y <= col2:
                    sum += sub_list[y]
                    y += 1

                x += 1

            self.cached[key] = sum

        return self.cached[key]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class Solution(object):

    def __init__(self, matrix):
        if not matrix:
            return
        self.sums = [[0] * (len(matrix[0]) + 1)]
        for row in matrix:
            stack = [0]
            for x in row:
                stack.append(stack[-1] + x)
            self.sums.append(map(sum, zip(self.sums[-1], stack)))

    def sumRegion(self, top, left, bottom, right):
        return self.sums[bottom + 1][right + 1] + self.sums[top][left] - self.sums[top][right + 1] - \
               self.sums[bottom + 1][left]
