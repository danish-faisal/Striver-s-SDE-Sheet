# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # calling the recursive-solver -> wait till True is returned from that functiona indicating the board is solved
        # will never enter else part as the given testcases will always have a solution
        return board if self.solve(board) else []
    
    def solve(self,board):
        # iterate over 9 rows of sudoku-board
        for row in range(0,9):
            # iterate over 9 cols of sudoku-board
            for col in range(0,9):
                # check if the pos is empty
                if board[row][col]=='.':
                    # 1-by-1 place all 1-9 digits in the empty-pos
                    for n in range(1,10):
                        #  check if the no. 'n' at empty-pos is valid
                        if self.isValid(row,col,board,str(n)):
                            # if yes place it in the pos -> call the function-recursively to check the next-empty and fill it
                            board[row][col]=str(n)
                            if self.solve(board):
                                return True
                            # backtracking step -> for a non-valid soln empty the filled pos to be fille with another-no.
                            board[row][col]='.'
                    # will reach here only if no-soln is found
                    return False
        return True
    
    def isValid(self,row,col,board,n):
        for i in range(0,9):
            # check if all the places in same row has the same-no.
            if board[row][i]==n:
                return False
            # check if all the places in same col has the same-no.
            if board[i][col]==n:
                return False
            # logic to go over each pos in 3x3 sub-matrix of 9x9 board
            # check if any position in the same box has the same-no.
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==n:
                return False
        # if none of the above cases returned false -> the no. selected is valid, return true
        return True