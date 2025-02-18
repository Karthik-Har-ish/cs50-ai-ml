
class GameState:
    def __init__(self,state,action,parent):
        self.state = state
        self.action=action
        self.parent=parent
        

        
    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j],end="")
                if j != 2:
                    print("|",end="")
            print("-----")
    def player(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j]!=" ":
                    count+=1
        if count%2==0:
            return "X"
        else:
            return "O"
        
    def actions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j]==" ":
                    actions.append((i,j))
        return actions
    
    def result(self,action):
        newState = self.state
        newState[action[0]][action[1]]=self.player()
        return newState
    
    def terminal(self,state):
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

class Min:
    def __init__(self,state):
        pass
        self.state = state
    
    """
    TODO : 
        -> COMPLETE AND CORRECT THE WORKING OF TERMINAL(STATE) / terminal(self)
            
        -> COMPLETE THE WORKING OF UTILITY(STATE)
        -> CREATE THE MINMAX ALGORITHM, AND FIGURE OUT HOW TO IMPLEMENT IT TO PLAY VERSUS PLAYER AND PLAY VERSUS ITSELF 
            -CLASSES REQUIRED
            -METHODS REQUIRED
            -ANY OTHER REQUIREMENTS
        ->PERFORM OPTIMIZATIONS LIKE ALPHA BETA PRUNING AND DEPTH LIMITED MINMAX 
    """