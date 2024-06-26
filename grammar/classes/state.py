from typing import List, Dict
from .action import Action

# Rule from grammar + position dot
# Rules are an array of Symbols (string)
class Transition:
    
    def __init__(self, ruleIndex: int, lhs: str, rhs: List[str], positionDot: int):
        self.grammarRule = lhs + ' -> ' + ' '.join(rhs)
        self.grammarRuleIndex = ruleIndex
        self.lhs = lhs
        self.rhs = rhs
        self.positionDot = positionDot                  # position of dot in rhs 

    def __str__(self):
        rhs_with_dot = ' '.join([f'. {x}' if i == self.positionDot else x for i, x in enumerate(self.rhs)])
        to_return = f"{self.lhs} -> {rhs_with_dot}"
        if self.positionDot == len(self.rhs):
            return to_return + ' .'
        return to_return
    
    # equal if the rule and position of dot are the same
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Transition):
            return self.lhs == __value.lhs and self.rhs == __value.rhs and self.positionDot == __value.positionDot

class State:
    # gotoSymbol can be a terminal or non-terminal
    def __init__(self, orderNumber: int, prevStateOrderNumber: int, gotoSymbol: str):
        self.orderNumber = orderNumber
        self.prevStateOrderNumber = prevStateOrderNumber
        self.gotoSymbol = gotoSymbol
        self.transitions: Transition = []
        # is added later
        self.isCopy = False
        self.copiedFromStateNumber = None
        # actions for LR table
        self.actions: Dict[str, Action] = {}
        # za rekurziju
        self.addedNTphaseTwo = []

    def addTransition(self, transition: Transition):
        self.transitions.append(transition)

    def alreadyHasTransForNonTerminal(self, nonTerminal: str):
        for t in self.transitions:
            if t.lhs == nonTerminal:
                return True
        return False
    
    def stateIsACopy(self, copiedFromStateNumber: int):
        self.isCopy = True
        self.copiedFromStateNumber = copiedFromStateNumber
        self.transitions = []

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, State):
            return self.gotoSymbol == __value.gotoSymbol and self.transitions == __value.transitions
        return False
    
    def __str__(self) -> str:
        state_string = f"State {self.orderNumber} = goto({self.prevStateOrderNumber}, {self.gotoSymbol}) {'copy of State ' + str(self.copiedFromStateNumber) if self.isCopy else ''}\n"

        transitions_string = ""
        if self.transitions:
            for t in self.transitions:
                transitions_string += f'\t{t}\n'

        actions_string = ""
        if self.actions:
            actions_string += '\n\tActions:\n'
            for symbol, action in self.actions.items():
                actions_string += f'\tfor {symbol}: {action.name} {action}\n'

        return state_string + transitions_string + actions_string
