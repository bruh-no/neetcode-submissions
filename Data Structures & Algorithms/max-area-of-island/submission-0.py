class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        curMax = 0
        rows, cols = len(grid), len(grid[0])
        visited = set() # (r,c) tuples stored here
        
        def dfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            curArea = 0

            while q:
                row, col = q.pop()
                curArea += 1
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    if (col + dc) in range(cols) and (row + dr) in range(rows) and grid[row + dr][col + dc] == 1 and (row + dr, col + dc) not in visited:
                        visited.add((row + dr, col + dc))
                        q.append((row + dr, col + dc))
            
            return curArea

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curMax = max(curMax, dfs(r,c))
        
        return curMax
        