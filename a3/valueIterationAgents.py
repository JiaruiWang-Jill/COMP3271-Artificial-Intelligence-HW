import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        states = self.mdp.getStates();
        listAction=[None] * len(states)
        self.actions=dict(zip(states, listAction))
        # Write value iteration code here
        state=   mdp.getStartState()
        "*** YOUR CODE HERE ***S"
    #    print ('startstate', state)

     #   print(states);
        temp0=util.Counter()
        for i in range(self.iterations):
          for state in states:
            possActions=mdp.getPossibleActions(state)
          #  print( mdp.getPossibleActions(state))
            maxQ=float("-inf")
            maxAction=None
            for action in possActions:
              temp=self.computeQValueFromValues(state, action)
              if temp>maxQ:
                maxQ=temp
                maxAction=action
                temp0[state]=maxQ
              self.actions[state]=maxAction
          self.values=temp0.copy()




    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        valueQ=0
      #  print("now is testing state, actino",state,action)
        for nextState, t in self.mdp.getTransitionStatesAndProbs(state, action):
          # print(nextState,t)
          # print(2,self.mdp.getReward(state, action,nextState))
          # print(3,self.discount)
          # print(4,self.getValue(nextState))
          valueQ+=t*(self.mdp.getReward(state, action,nextState) +self.discount *self.getValue(nextState))
     #   print("this is the calculated value q",valueQ)
        return valueQ

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
     
        return self.actions[state]

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
