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
def generateFollowSets(G, T, nT):
    follow_sets = {symbol: set() for symbol in nT}
    epsilon = '#'       # Representing end of input (added as a terminal)

    changed = True      # track changes in the FOLLOW sets
    while changed:
        changed = False

        for rule in G:
            lhs, rhs = rule[1], rule[2].split(' ')
            for i, symbol in enumerate(rhs):
                if symbol in nT:
                    next_symbol = None

                     # Traverse the symbols to the right of the current non-terminal
                    for j in range(i + 1, len(rhs)):
                        next_symbol = rhs[j]

                        # If it's a non-terminal, update its FOLLOW set based on the current non-terminal
                        if next_symbol in nT:
                            if epsilon not in follow_sets[next_symbol] and next_symbol != lhs:
                                follow_sets[next_symbol].add(epsilon)
                                changed = True

                             # Break loop when encountering a non-terminal symbol
                            break

                        # If it's a terminal, add it to the FOLLOW set and break
                        elif next_symbol in T:
                            if next_symbol not in follow_sets[symbol]:
                                follow_sets[symbol].add(next_symbol)
                                changed = True
                            break
                    
                    # If the loop completes without breaking, update the FOLLOW set with the current non-terminal's FOLLOW set
                    else:
                        if lhs != symbol:
                            for term in follow_sets[lhs]:
                                if term not in follow_sets[symbol]:
                                    follow_sets[symbol].add(term)
                                    changed = True

        # Adding the # symbol to the FOLLOW set of the start symbol
        if '#' not in follow_sets[nT[0]]:
            follow_sets[nT[0]].add('#')
            changed = True

    return follow_sets