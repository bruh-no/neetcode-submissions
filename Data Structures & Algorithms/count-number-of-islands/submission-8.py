class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        q = deque()
        seen = set()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] == "1":
                    islands += 1
                    q.append((i,j))
                    while q:
                        curx, cury = q.pop()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = curx + dx, cury + dy
                            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and (nx, ny) not in seen):
                                seen.add((nx, ny))
                                q.append((nx, ny))
                                seen.add((i,j))
                        
        
        return islands





        