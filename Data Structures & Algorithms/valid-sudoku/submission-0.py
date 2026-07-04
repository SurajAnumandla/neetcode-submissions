from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)   
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c] 
                if val!= ".":
                    if val in rows[r]:
                        return False
                    else:
                        rows[r].add(val)
                    if val in cols[c]:
                        return False
                    else:
                        cols[c].add(val)

                    box_key = (r//3,c//3)

                    if val in boxes[box_key]:
                        return False
                    else:
                        boxes[box_key].add(val)
        return True
                                     