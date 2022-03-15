from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeroes = []
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroes.append([i, j])
                
    for x, y in zeroes:
        matrix[x] = [0 for _ in range(n)]
        for i in range(m):
            matrix[i][y] = 0