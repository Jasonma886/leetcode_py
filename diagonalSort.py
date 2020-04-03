# Input: mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
# Output: [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]


def diagonalSort(mat):
    print(sum(mat, []))
    # mat[i] 长度
    mat_len = len(mat)
    flat = sorted(sum(mat, []))
    result = []
    for idx, val in enumerate(flat):
        (x, y) = divmod(idx, mat_len)
        if x == 0:
            result.append([val])
        else:
            result[y].append(val)
    return result

if __name__ == '__main__':
    diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
