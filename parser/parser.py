from grammar.classes.state import State
from grammar.classes.action import Action
from typing import List
import sys

def check_syntax(words: List[str], states: List[State]) -> bool:

    state_zero = states[0]
    magazine = []
    magazine.append(state_zero)

    correct = None

    while correct is None:

        # ----------------- DEBUG -----------------------
        # print(words)
        # for obj in magazine:
        #     if isinstance(obj, State):
        #         sys.stdout.write(f'S{obj.orderNumber}')
        #     else:
        #         sys.stdout.write(str(obj))
        #     sys.stdout.write(' ')
        # print('\n')
        # -----------------------------------------------

        current_state = magazine[len(magazine) - 1]
        next_word = words[0]
        action: Action = current_state.actions.get(next_word)

        # Error
        if action is None:
            correct = False
            return False
        
        # Accept
        if action.name == 'Accept':
            correct = True
            return True
        
        # Shift
        if action.name == 'Shift':
            magazine.append(next_word)                  # word
            magazine.append(action.intoState)           # state
            words = words[1:]

        # Reduce
        if action.name == 'Reduce':
            ruleRhs: List[str] = action.rhs.split(' ')
            # pop the magazine for rhs.len * 2
            for i in range(len(ruleRhs) * 2):
                magazine.pop()

            # push the lhs to magazine
            lhs = action.lhs
            curr_state = magazine[len(magazine) - 1]
            tmp_action = curr_state.actions.get(lhs)        # get -> to prevent KeyError

            # just in case 
            if tmp_action is None or tmp_action.name != 'Shift':
                correct = False
                return False
            
            next_state = tmp_action.intoState
            magazine.append(lhs)                        # word
            magazine.append(next_state)                 # state

    return correct