class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r / 3, c / 3)


        
        for r in range(9):
            for c in range(9):
                curNum = board[r][c]
                if curNum == ".":
                    continue
                if curNum in rows[r] or curNum in cols[c] or curNum in squares[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(curNum)
                    cols[c].add(curNum)
                    squares[(r // 3, c // 3)].add(board[r][c])


        return True

