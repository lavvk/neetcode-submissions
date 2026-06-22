class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            uniqueVals = set()
            values = []
            for val in row:
                if val != ".":
                    uniqueVals.add(val)
                    values.append(val)
            if len(values) != len(uniqueVals):
                return False

        for col in range(9):
            uniqueVals = set()
            values = []
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    uniqueVals.add(val)
                    values.append(val)
            if len(values) != len(uniqueVals):
                return False

        # each 3x3 subgrid
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                uniqueVals = set()
                values = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val != ".":
                            uniqueVals.add(val)
                            values.append(val)
                if len(values) != len(uniqueVals):
                    return False

        return True

