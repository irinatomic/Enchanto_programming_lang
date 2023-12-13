from classes.state import State, Transition

states: State = []

def isAlreadyDeterminedState(oldStateNumber, nextSymbol):
    global states
    for state in states:
        if state.prevStateOrderNumber == oldStateNumber and state.gotoSymbol == nextSymbol:
            return True 
    return False

def ledIntoAnExistingState(newState: State):
    global states
    for s in states:
        if s == newState:
            return s.orderNumber
    return None

def generateStateZero(grammar):
    global states
    stateZero = State(0, None, None,)

    for rule in grammar:
        rhs = rule[2].split(' ')
        transition = Transition(rule[0], rule[1], rhs, 0)
        stateZero.addTransition(transition)
    states.append(stateZero)

# gledamo da li u listi prelaza za trenutno stanje,
# ima jos pravila gde je naredni simbol onaj koji je prosledjen
def addTransitionsOne(currState, newState, nextSymbol):

    for t in currState.transitions:
        if t.positionDot <= len(t.rhs)-1 and t.rhs[t.positionDot] == nextSymbol:
            newT = Transition(t.grammarRuleIndex, t.lhs, t.rhs, t.positionDot+1)
            newState.addTransition(newT)

            newNextSymbol = newT.rhs[newT.positionDot] if newT.positionDot <= len(newT.rhs)-1 else None
            addTransitionsTwo(newState, newNextSymbol)

# zelimo da za nT sa desne strane dodamo pravila tamo gde je on sa leve strane
# U PRAVILIMA ZERO STATE-a
def addTransitionsTwo(newState, newNextSymbol):

    # zbog rekurzije - jednom dodajemo pravila za newNextSymbol za newState
    if newNextSymbol in newState.addedNTphaseTwo:
        return
    newState.addedNTphaseTwo.append(newNextSymbol)

    if newNextSymbol is None or newNextSymbol.islower():
        return
    
    global states
    zeroState = states[0]
    for t in zeroState.transitions:
        if t.lhs == newNextSymbol:
            # ovde sad ne pomeramo dot !
            newT = Transition(t.grammarRuleIndex, t.lhs, t.rhs, t.positionDot)
            newState.addTransition(newT)

            # trazimo novi simbol sa desne strane
            newNewNextSymbol = t.rhs[t.positionDot] if t.positionDot <= len(t.rhs)-1 else None
            addTransitionsTwo(newState, newNewNextSymbol)


# Imamo 2 momenta kada dodajemo dodatna pravila (transitions u newState):
# 1. kada u currentState, na jos mesta je naredni simbol == nonTerminal (addTransitionsOne)
# 2. kada je naredni simbol nonTerminal -> dodajemo pravila za njega iz stateZero (addTransitionsTwo)
def generateStates():
    global states

    for state in states:
        if state.isCopy:
            continue

        for transition in state.transitions:
            if transition.positionDot <= len(transition.rhs)-1:
                nextSymbol = transition.rhs[transition.positionDot]
                # generate a new state
                # newState = goto(currState, nextSymbol)

                # ne zelimo 2 puta isti prelaz za trenutno stanje
                if isAlreadyDeterminedState(state.orderNumber, nextSymbol):
                    continue

                newState = State(len(states), state.orderNumber, nextSymbol)

                if not newState.alreadyHasTransForNonTerminal(nextSymbol):
                    addTransitionsOne(state, newState, nextSymbol)

                # NA KRAJU: da li nas je odvelo u neko vec postojce stanje?
                copyOf = ledIntoAnExistingState(newState)
                if copyOf is not None:
                    newState.stateIsACopy(copyOf)
                    
                states.append(newState)

    return states