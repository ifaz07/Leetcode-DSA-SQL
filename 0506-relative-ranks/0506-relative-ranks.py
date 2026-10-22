import heapq

class Solution(object):
    def findRelativeRanks(self, score):
        heap = []

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))

        answer = [""] * len(score)
        rank = 1

        while heap:
            s, i = heapq.heappop(heap)

            if rank == 1:
                answer[i] = "Gold Medal"
            elif rank == 2:
                answer[i] = "Silver Medal"
            elif rank == 3:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank)

            rank += 1

        return answer