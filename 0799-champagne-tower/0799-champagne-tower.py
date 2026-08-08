class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        row = [float(poured)]

        for r in range(query_row):
            next_row = [0.0] * (r + 2)

            for i in range(r + 1):
                overflow = max(0.0, row[i] - 1.0)

                next_row[i] += overflow / 2
                next_row[i + 1] += overflow / 2

            row = next_row

        return min(1.0, row[query_glass])