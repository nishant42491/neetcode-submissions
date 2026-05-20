from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowmap = defaultdict(list)
        colmap = defaultdict(list)
        cell_map = defaultdict(list)


        for i in range(9):
            for j in range(9):

                cur_let = board[i][j]

                if cur_let != ".":

                    if cur_let in rowmap[i]:

                        return False

                    elif cur_let in colmap[j]:

                        return False

                    elif cur_let in cell_map[(i//3,j//3)]:

                        return False

                    else:

                        rowmap[i].append(board[i][j])
                        colmap[j].append(board[i][j])
                        cell_map[(i//3,j//3)].append(board[i][j])

                    
        return True

                        
                        

