class Solution(object):
    def transpose(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        trans = [[] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                trans[j].append(matrix[i][j])

        return trans