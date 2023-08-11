class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub_boxes[r // 3,c // 3]):
                    return False
                if (board[r][c] == '.'):
                    continue
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_boxes[r // 3,c // 3].add(board[r][c])

        return True