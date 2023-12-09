from typing import List
from classes.state import State
from classes.action import Shift, Reduce, Accept

def findStateByOrderNumber(states: List[State], prevStateNo: int) -> State:
    return next((s for s in states if s.orderNumber == prevStateNo), None)

def determineShiftActions(states: List[State]): 
    for s in states[1:]:
        prevStateNo = s.prevStateOrderNumber
        symbol = s.gotoSymbol

        # for state with prevStateNo add: actions[symbol] = Shift(s)
        currStateNo = s.orderNumber
        if s.isCopy:
            currStateNo = s.copiedFromStateNumber
        
        currState = findStateByOrderNumber(states, currStateNo)
        prevState = findStateByOrderNumber(states, prevStateNo)
        prevState.actions[symbol] = Shift(currState)

def determineAcceptAction(states: List[State]):
    for s in states:
        for t in s.transitions:
            # Check if the dot is at the end of the start symbol
            if t.lhs == 'START' and t.positionDot == len(t.rhs):
                s.actions['#'] = Accept()  
                return
            
def determineReduceActions(states: List[State], grammar: List[tuple], followSets: dict):
    for s in states:
        for t in s.transitions:
            # Check if the dot is at the end of the start symbol
            if t.positionDot == len(t.rhs):
                rule = grammar[t.grammarRuleIndex]

                symbol = t.lhs
                for followSymbol in followSets[symbol]:
                    s.actions[followSymbol] = Reduce(rule[0], rule[1], rule[2])

def determineActions(states: List[State], grammar: List[tuple], followSets: dict):

    # Accept is of the highest priority
    # so it goes last (to override other actions)
    determineShiftActions(states)
    determineReduceActions(states, grammar, followSets)
    determineAcceptAction(states)