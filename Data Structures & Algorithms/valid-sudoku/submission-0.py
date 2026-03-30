class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        hashmap = {key: set() for key in range(9)}

        for i in range(9):
            for j in range(9):

                if board[i][j] == "." : 
                    continue

                boxindex = int((i // 3) * 3 + (j // 3)) 

                if (board[i][j] in rowset[i] or
                    board[i][j] in colset[j] or
                    board[i][j] in hashmap[boxindex]):
                    return False
                
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                hashmap[boxindex].add(board[i][j])


        return True


