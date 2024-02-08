from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count

if __name__ == "__main__":
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
    x = [-1,0,1,0]
    y = [0,1,0,-1]
    row = len(grid)
    col = len(grid[0])

    