class Solution:
        
    def search_dfs(self, grid: List[List[str]],r,c):
          if r<0 or c<0 or r>=len(grid) or c>=len(grid[r]) or grid[r][c]=='0':
                 return
                                        
          grid[r][c] = '0'
                                                
          self.search_dfs(grid,r+1,c)
          self.search_dfs(grid,r,c+1)
          self.search_dfs(grid,r-1,c)
          self.search_dfs(grid,r,c-1)
                                                                                        
                                                                                          
    def numIslands(self, grid: List[List[str]]) -> int:
                                                                                                                                               count=0
                                                                                                                    
          for i in range(0,len(grid)):
              for j in range(0,len(grid[0])):
                                                                                                                                                        if grid[i][j] == '1':
                       self.search_dfs(grid,i,j)
                       count += 1     
                                                                                                                                                                                                                                                                                    return count
