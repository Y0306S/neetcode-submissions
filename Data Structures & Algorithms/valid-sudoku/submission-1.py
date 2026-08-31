class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid sudoku can use mutliple passes one ot chekc the row one to chekc the col and one to chekc the both should be in O(n) time for both time and space complexity, which may delayed exits which can hurt performance
        # more efficient method is to use a set to speed up the processes to process all three outputs at once due to t sO91) lookup time
        """
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val!=".":
                    new = [(r, val), (val, c), (r//3, c//3, val)]
                    if any(n in visited for n in new):
                        return False
                    visited.update(new)
        return True
        """
        #however we can further speed this up by using bits instead of a hashmap
        row, col, box = [0] * 9, [0] * 9, [0] * 9 
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                val = 1<<(int(board[r][c])-1)
                if val & row[r] or val & col[c] or val & box[r//3*3 + c//3]:
                    return False
                row[r] |= val
                col[c] |= val
                box[r//3*3+c//3] |= val
        return True

