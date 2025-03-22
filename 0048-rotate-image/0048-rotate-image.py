class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i,size = 0,len(matrix[0])

        while i < size:
            for j in range(i+1,size):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
            i += 1

        for row in matrix:
            row.reverse()
        