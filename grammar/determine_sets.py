from typing import List

follow_sets: dict = {}

# FIRST SETS
def generateFirstSets(G, T, nT):

    first_sets = {symbol: set() for symbol in nT}
    epsilon = '$'
    changed = True               # track changes in the FIRST sets

    # Until no changes
    while changed:
        changed = False  

        for rule in G:
            lhs, rhs = rule[1], rule[2].split(' ')  
            if lhs not in nT:           # extra check
                continue

            # go through production (rhs)
            for symbol in rhs:
                if symbol in nT:
                    # Iterate through the FIRST set of the symbol -> nadskup
                    for term in first_sets[symbol]:
                        if term != epsilon and term not in first_sets[lhs]:
                            first_sets[lhs].add(term)
                            changed = True                           # Changes occur
                    
                    # If epsilon is not in the FIRST set of the symbol, break the loop
                    if epsilon not in first_sets[symbol]:
                        break  

                # Non-terminal
                elif symbol != epsilon:
                    # Add the symbol to the FIRST set of the left-hand side
                    if symbol not in first_sets[lhs]:
                        first_sets[lhs].add(symbol)
                        changed = True                              # Changes occur
                    break                                           # Break to handle the next rule
            
             # If the loop completes without breaking, add epsilon to the FIRST set of the left-hand side
            else:
                first_sets[lhs].add(epsilon)
                changed = True                                      # Changes occur           

    return first_sets

# FOLLOW SETS
def generateFollowSets(G, first_sets): 
    global follow_sets
    nT = extractNonTerminalsInOrder(G)

    follow_sets = {symbol: set() for symbol in nT}
    epsilon = '#'
    follow_sets[nT[0]].add(epsilon)             # Add # to the start symbol
    
    for nt in nT:
        rules = findRulesWithNonTeminal(G, nt)
        for rule in rules:
            lhs = rule[1]
            rhs = rule[2].split(' ')
            ntIndex = rhs.index(nt)

            # A -> c CURR
            # follow(CURR) += follow(A)
            # PROBLEM: follow(A) might not be initialized yet
            if nt == rhs[-1]:
                if (len(follow_sets[lhs]) == 0):
                    generateFollowSetForNT(G, first_sets, lhs, nT)
                follow_sets[nt] = follow_sets[nt].union(follow_sets[lhs])

            nextSymbol = rhs[ntIndex + 1] if ntIndex + 1 < len(rhs) else None

            # if the next symbol is a non-terminal
            # A -> c CURR NEXT
            # follow(curr) += first(next)
            if nextSymbol is not None and nextSymbol in nT:
                follow_sets[nt] = follow_sets[nt].union(first_sets[nextSymbol])

            # if the next symbol is a terminal
            if nextSymbol is not None and nextSymbol not in nT:
                follow_sets[nt].add(nextSymbol)

    return follow_sets

# FOLLOW SETS - helper
# Only for 1 non-terminal
def generateFollowSetForNT(G, first_sets, nt: str, nT: List[str]):
    global follow_sets
    rules = findRulesWithNonTeminal(G, nt)

    for rule in rules:
            lhs = rule[1]
            rhs = rule[2].split(' ')
            ntIndex = rhs.index(nt)

            # A -> c CURR
            # follow(CURR) += follow(A)
            # PROBLEM: follow(A) might not be initialized yet
            if nt == rhs[-1]:
                if (len(follow_sets[lhs]) == 0):
                    generateFollowSetForNT(G, first_sets, lhs, nT)
                follow_sets[nt] = follow_sets[nt].union(follow_sets[lhs])

            nextSymbol = rhs[ntIndex + 1] if ntIndex + 1 < len(rhs) else None

            # if the next symbol is a non-terminal
            # A -> c CURR NEXT
            # follow(curr) += first(next)
            if nextSymbol is not None and nextSymbol in nT:
                follow_sets[nt] = follow_sets[nt].union(first_sets[nextSymbol])

            # if the next symbol is a terminal
            if nextSymbol is not None and nextSymbol not in nT:
                follow_sets[nt].add(nextSymbol)

def extractNonTerminalsInOrder(G):
    nT = []
    for rule in G:
        lhs = rule[1]
        if lhs not in nT:
            nT.append(lhs)
    return nT

def findRulesWithNonTeminal(G: List[tuple], nt : str):
    rules = []
    for rule in G:
        rhs = rule[2].split(' ')    # if on the right side of the rule
        if nt in rhs:            
            rules.append(rule)
    return rules    