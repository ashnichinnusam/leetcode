from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        pairs = 0

        for row in grid :
            rows[tuple(row)]+=1

        for col in range(n):
            coloumn = tuple(grid[r][col] for r in range(n)) 
            if coloumn in rows:
                pairs+=rows[coloumn]
        return pairs 
        