class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,i,j):
            dir=[(1,0),(0,1),(0,-1),(-1,0)]
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            if grid[i][j]=="1":
                grid[i][j]='#'
                for x,y in dir:
                    dfs(grid,x+i,y+j)
        res=0
        for l in range(len(grid)):
            for m in range(len(grid[0])):
                
                if grid[l][m]=='1':
                    res+=1
                    dfs(grid,l,m)
        return res