
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
                    if self.state[i][j]!=" ":
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
            print("diagonal achieved by one agent")
            # TODO:  FINISH DIAGONAL ACHIEVED CONDITION
        
        if diagonalAchieved():
            return True

        return False
        # for i in range(3):
        #     for j in range(3):
        #         for k in options:
        #             if row[i][j]==k:

        # if 3 in row.values():
        #     return True
        # row.clear()
        # for i in range(3):
        #     for j in range(3):
        #         if self.state[i][j]!=" ":
        #             row[j]=row.get(j,0)+1
        # if 3 in row.values():
        #     return True
        # row.clear()
        # totalCount=0
        # for i in range(3):
        #     if self.state[i][i]=="X":
        #         total

    

        
        for i in range(3):
            for j in range(3):
                if self.state[i][j]!=" "
                row[]
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