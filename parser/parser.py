from grammar.classes.state import State
from grammar.classes.action import Action
from typing import List
import sys

def check_syntax(words: List[str], states: List[State]) -> bool:
    stateZero = states[0]

    magazine = []
    magazine.append(stateZero)

    while True:
        currentState = magazine[len(magazine) - 1]
        nextWord = words[0]

        # ----------
        for obj in magazine:
            if isinstance(obj, State):
                sys.stdout.write(f'S{obj.orderNumber}')
            else:
                sys.stdout.write(str(obj))
            sys.stdout.write(' ')
        print('\n')
        # ----------

        # Next action
        action: Action = currentState.actions[nextWord]

        # Error
        if action is None:
            return False

        # Accept
        if action.name == 'Accept':
            return True

        # Shift
        if action.name == 'Shift':
            magazine.append(nextWord)
            magazine.append(action.intoState)
            words = words[1:]
            continue

        # Reduce
        if action.name == 'Reduce':
            ruleRhs = action.rhs
            print(ruleRhs)
            return
        # # If the action is reduce, pop the magazine for the length of the right hand side of the rule
        # # and push the left hand side of the rule
        # if action.type == 'reduce':
        #     for i in range(action.rule.rhs.length):
        #         magazine.pop()
        #     magazine.push(action.rule.lhs)
        #     continue




