state = [[" ","O","X"],["X","X","O"],["X","O"," "]]
def terminal(state):
        def slotsFilled():
            totalCount = 0
            for i in range(3):
                for j in range(3):
                    if state[i][j]!=" ":
                        totalCount+=1
            if totalCount==9:
                return True
    
        if slotsFilled():
            return True

        def rowAchieved():
            options = ("X","O")
            for k in options:
                for i in state:
                    rowFound = all(j==k for j in i)
                    if rowFound:
                        return True
            return False
        if rowAchieved():
            return True

        def columnAchieved():
            options = ("X","O")
            for i in range(3):
                column = []
                for j in range(3):
                    column.append(state[j][i])
                for k in options:
                    columnFound = all(j==k for j in column)
                    if columnFound:
                        return True
            return False
        if columnAchieved():
            return True

        def diagonalAchieved():
            options = ("X","O")
            for k in options:
                isDiagonal=0
                for i in range(3):
                    if state[i][i]==k:
                        isDiagonal+=1
                if isDiagonal==3:
                    return True
                isDiagonal=0
                for i in range(3):
                    if state[i][abs(2-i)]==k:
                        isDiagonal+=1
                if isDiagonal==3:
                    return True
            return False
        if diagonalAchieved():
            return True

        return False

# print(rowAchieved(state))
print(terminal(state))