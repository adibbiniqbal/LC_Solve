class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        s = list(set(arr))
        s.sort()
        rank = {}
        for i, n in enumerate(s, 1):
            rank[n] = i
        return list(rank[x] for x in arr)
        