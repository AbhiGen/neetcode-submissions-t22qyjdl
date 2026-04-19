class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 🧠 IDEA:
        # A Sudoku board is valid if no number (1–9) repeats in:
        # 1. Any row
        # 2. Any column
        # 3. Any 3×3 sub-box
        #
        # We use sets to keep track of numbers already seen
        # in rows, columns, and 3×3 boxes.

        # ⏱️ Time Complexity:
        # O(81) → constant time (always a 9x9 board)

        # 🧠 Space Complexity:
        # O(81) → sets store at most 9 elements each

        rows = {}  # row index → set of numbers seen in that row
        cols = {}  # column index → set of numbers seen in that column
        sq = {}    # (box_row, box_col) → set of numbers in that 3x3 box

        # Traverse each cell in the Sudoku board
        for r in range(9):          # r → row index (0 to 8)
            for c in range(9):      # c → column index (0 to 8)

                # Skip empty cells
                if board[r][c] == '.':
                    continue

                num = board[r][c]        # Current number
                box = (r // 3, c // 3)   # Identify 3x3 sub-box

                # Initialize sets if not already created
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box not in sq:
                    sq[box] = set()

                # Check for duplicates
                if num in rows[r] or num in cols[c] or num in sq[box]:
                    return False

                # Mark number as seen
                rows[r].add(num)
                cols[c].add(num)
                sq[box].add(num)

        # No rule violations found
        return True
