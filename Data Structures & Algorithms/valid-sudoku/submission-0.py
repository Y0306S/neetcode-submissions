class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid sudoku can use mutliple passes one ot chekc the row one to chekc the col and one to chekc the both should be in O(n) time for both time and space complexity, which may delayed exits which can hurt performance
        # more efficient method is to use a set to speed up the processes to process all three outputs at once due to t sO91) lookup time
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
