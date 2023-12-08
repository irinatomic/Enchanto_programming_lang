from classes import State, Transition

states: State = []

# Grammar, Non-terminal symbols (uppercase), Terminal (all else)
def import_grammar(fileData):
    G, T, nT = [], [], []

    for i in range(len(fileData)):
        line = fileData[i]
        line = line.strip()
        line = line.replace('\n', '')
        sides = line.split(' -> ')

        lhs = sides[0].strip()
        rhs = sides[1].strip()

        nT.append(lhs) if lhs not in nT else None
        rhs_symbols = rhs.split(' ')
        for symbol in rhs_symbols:
            if symbol.isupper():
                nT.append(symbol) if symbol not in nT else None
            else:
                T.append(symbol) if symbol not in T else None
        if (lhs, rhs) not in G:
            G.append((i, lhs, rhs))

    T.append('$')
    return G, T, nT

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
# 1. kada u currentState, na jos mesta je naredni simbol == nonTerminal (addAdditionalRules)
# 2. kada je naredni simbol nonTerminal -> impl u klasi State/addTransition
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

                # NA KRAJU: da li nase je odvelo u neko vec postojce stanje
                copyOf = ledIntoAnExistingState(newState)
                if copyOf is not None:
                    newState.stateIsACopy(copyOf)
                    
                states.append(newState)


def main():

    fileData = open('grammar.txt', 'r').readlines()

    # Grammar - list of rules (tuple: index, lhs, rhs)
    G, T, nT = import_grammar(fileData)

    # print(G)
    # print(T)
    # print(nT)

    generateStateZero(G)
    generateStates()

    global states
    for s in states:
        print('State', s.orderNumber, '= goto(', s.prevStateOrderNumber, ',', s.gotoSymbol, ')', s.isCopy, s.copiedFromStateNumber)

        for t in s.transitions:            
            print('\t', t)

if __name__ == "__main__":
    main()