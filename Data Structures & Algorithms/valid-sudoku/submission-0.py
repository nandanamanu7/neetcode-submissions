class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board[0]))]
        boxes = [set() for i in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                tile = board[r][c]

                if (tile == "."):
                    continue
                
                box = r // 3 * 3 + c // 3

                if (tile in rows[r] or tile in cols[c] or tile in boxes[box]):
                    return False
                
                else:
                    rows[r].add(tile)
                    cols[c].add(tile)
                    boxes[box].add(tile)

        return True        