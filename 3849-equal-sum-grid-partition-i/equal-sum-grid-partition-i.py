class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        if total & 1:
            return False
        curr = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr += grid[r][c]
            if curr == total - curr:
                return True
        curr = 0
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                curr += grid[r][c]
            if curr == total - curr:
                return True
        return False
        
        