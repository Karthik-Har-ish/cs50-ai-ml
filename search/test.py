state = [["X","X"," "],["X","X","O"],["O","X","O"]]
def rowAchieved(state):
            options = ("X","O")
            for k in options:
                for i in state:
                    rowFound = all(j==k for j in i)
                    if rowFound:
                        return True
            return False
def columnAchieved(state):
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

# print(rowAchieved(state))
print(columnAchieved(state))