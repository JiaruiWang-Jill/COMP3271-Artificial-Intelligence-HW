"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""

    from util import Stack
    from game import Directions
    exploredSet=[]
    frontier=Stack()
    temp=(problem.getStartState(),'')
    #print("getStartState",problem.getStartState())
    frontier.push(temp)
    while(not frontier.isEmpty()):
        node = frontier.pop()
        if problem.isGoalState(node[-2]):
            path=[]
            for i in range(3,len(node)):
                if i%2 ==1:
                    path.append(node[i])
            #print("finally answer",path)
            return path
        if node[-2] not in exploredSet:
            exploredSet.append(node[-2])
            for pos, action, cost in problem.getSuccessors(node[-2]):
                #print("finding child",node+(pos,action))
                frontier.push(node+(pos,action))

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    from util import Queue
    from game import Directions
    exploredSet=()
    frontier=Queue()
    temp=[[problem.getStartState(),'']]
    frontier.push(temp)
    while(not frontier.isEmpty()):
        #print("frontier",frontier.list)
        node = frontier.pop()
        if node[-1][0] not in exploredSet:
            if problem.isGoalState(node[-1][0]):
                target=node[1:]
                path = [direc for pos, direc in target]
                return path
            else:
                exploredSet+=(node[-1][0],)
                for pos, action, cost in problem.getSuccessors(node[-1][0]):
                    frontier.push(node+[[pos,action]])


def uniformCostSearch(problem):
    from util import PriorityQueue
    from game import Directions

    exploredSet=[]
    frontier=PriorityQueue()
    frontier.push((problem.getStartState(),'',0),0)
    while(not frontier.isEmpty()):
        node = frontier.pop()
        if problem.isGoalState(node[-3]):
            path=[]
            for i in range(4,len(node)):
                if i%3 ==1:
                    path.append(node[i])
            print(path)
            return path
        if node[-3] not in exploredSet:
            exploredSet.append(node[-3])
            for pos, action, cost in problem.getSuccessors(node[-3]):
                #compare the g value
                frontier.push(node+(pos,action,cost+node[-1]),cost+node[-1])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    from util import PriorityQueue
    from game import Directions
    from searchAgents import manhattanHeuristic
    # print("testing, at least in")
    exploredSet=[]
    frontier=PriorityQueue();  
    aCost=0+heuristic(problem.getStartState(),problem)
    #print("starting point",heuristic(problem.getStartState(),problem))
    temp = [[problem.getStartState(),'',aCost]]
    frontier.push(temp,aCost)
    while(not frontier.isEmpty()):
        node = frontier.pop()
        if problem.isGoalState(node[-1][0]):            
            target=node[1:]
            #print(target)
            path = [direc for pos, direc,cost in target]
            #print("path",path)
            #print("result testing",heuristic(node[-1][0],problem))
            return path
        if node[-1][0] not in exploredSet:
            exploredSet.append(node[-1][0])
            b1=heuristic(node[-1][0],problem)
            target =node[1:]
            path = [direc for pos, direc,cost in target]
            a1=problem.getCostOfActions(path)
            for pos, action, cost in problem.getSuccessors(node[-1][0]): 
                currentCost=heuristic(pos,problem)
                lastCost=heuristic(node[-1][0],problem)
                #compare the g value and heuristic value at the same time
                result =  node+[[pos,action,cost+node[-1][2]+currentCost-lastCost]]
                frontier.push(result,cost+node[-1][2] + currentCost - lastCost)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
