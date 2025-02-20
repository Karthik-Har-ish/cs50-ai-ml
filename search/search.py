import time

class Node:
    def __init__(self,state,action,parent,pathCost):
        self.state = state
        self.action = action
        self.parent = parent
        self.pathCost = pathCost

class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def push(self,node):
        self.frontier.append(node)
    
    def pop(self):
        return self.frontier.pop()
    
    def containsState(self,state):
        return any(node.state==state for node in self.frontier)

    def empty(self):
        if self.frontier:
            return False
        return True
    def remove(self):
        if self.empty():
            print("Empty Stack error!!")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
        # TODO : USE POP INSTEAD OF THIS WEIRD CODE HERE

class QueueFrontier:
    def __init__(self):
        self.frontier = []
    
    def enqueue(self,node):
        self.frontier.append(node)

    def dequeue(self):
        dequeueItem = self.frontier[0]
        self.frontier = self.frontier[1:]
        return dequeueItem
    
    def containsState(self,state):
        return any(node.state==state for node in self.frontier)
    
    def empty(self):
        if self.frontier:
            return False
        return True
    
    def remove(self):
        if self.empty():
            print("Empty Stack error!!")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze:
    def __init__(self,filename):
        with open(filename) as textFile:
            contents=textFile.read()
        if contents.count("A")!=1:
            print("ERROR: there must be exactly one starting point!")
        elif contents.count("B")!=1:
            print("ERROR: there must be exactly one ending point!")
        
        contents = contents.splitlines()
        self.height=len(contents)
        self.width=len([line for line in contents])

        self.walls = []
        for i in range(self.height):
            row=[]
            for j in range(self.width):
                try:
                    if contents[i][j]=="A":
                        row.append(False)
                        self.start = (i,j)
                    elif contents[i][j]=="B":
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j]==" ":
                        row.append(False)
                    else:
                        row.append(True)
                except(IndexError):
                    row.append(False)
            self.walls.append(row)
        self.solution=None
        self.pathExplored = []

    def print(self,**kwargs):
        self.showPath = kwargs.get("showPath",False)
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i,row in enumerate(self.walls):
            for j,col in enumerate(row):
                if col:
                    print("█",end="")
                elif (i,j)==self.start:
                    print("A",end="")
                elif (i,j)==self.goal:
                    print("B",end="")
                elif solution is not None and (i,j) in solution:
                    print("*",end="")
                elif self.showPath and (i,j) in self.pathExplored:
                    print('.',end="")
                else:
                    print(" ",end="")
            print()
        print()

    def neighbours(self,state):
        row,col = state

        candidates = [
            ("up",(row-1,col)),
            ("down",(row+1,col)),
            ("left",(row,col-1)),
            ("right",(row,col+1)),
        ]

        result = []
    
        for action,(r,c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r,c)))
            except(IndexError):
                continue
        return result
    
    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start,action=None,parent=None,pathCost=0)
        frontier = StackFrontier()
        frontier.push(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No solution!")
            
            node = frontier.remove()
            self.num_explored+=1
            self.explored.add(node.state)
            self.pathExplored.append(node.state)
            if node.state==self.goal:
                actions = []
                cells = []
                
                while node.parent!=None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node=node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions,cells)
                break
            
            
            
            for action,state in self.neighbours(node.state):
                if not frontier.containsState(state) and state not in self.explored:
                    child = Node(state,action,node,node.pathCost+1)
                    frontier.push(child)
                

maze = Maze("maze.txt")

maze.print()
start=time.time()
maze.solve()
end = time.time()
maze.print()

print(maze.num_explored)
with open("log.txt","a") as log:
    log.write(str(end-start)+"seconds\n")