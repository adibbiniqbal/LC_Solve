class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        minCost = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                minCost += cost[i]
        return minCost

        