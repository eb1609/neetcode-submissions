class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        while i<9:
            hash = set()
            j = 0
            while j<9:
                if board[i][j] != ".":
                    if board[i][j] in hash:
                        return False
                    hash.add(board[i][j])
                j+=1
            i+=1
        c = 0
        while c<9:
            seen = set()
            r=0
            while r<9:
                if board[r][c] != ".":
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
                r+=1
            c+=1
        startrows = 0
        while startrows<9:
            startcols = 0
            while startcols<9:
                square = set()
                row = startrows
                while row <startrows+3:
                    col = startcols
                    while col < startcols+3:
                        if board[row][col] != ".":
                            if board[row][col] in square:
                                return False
                            square.add(board[row][col])
                        col+=1
                    row+=1
                startcols+=3
            startrows+=3
        return True



        