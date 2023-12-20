from grammar.determine_states import generateStateZero, generateStates
from grammar.determine_sets import generateFirstSets, generateFollowSets
from grammar.determine_actions import determineActions
from grammar.export_table import exportLRTAble

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

def process_grammar(grammar_path):

    fileData = open(grammar_path, 'r').readlines()

    # Grammar - list of rules (tuple: index, lhs, rhs)
    G, T, nT = import_grammar(fileData)

    generateStateZero(G)
    states = generateStates()

    # first and follow sets
    first_sets = generateFirstSets(G, T, nT)
    follow_sets = generateFollowSets(G, first_sets)

    # actions
    determineActions(states, G, follow_sets)

    # export table to excel
    exportLRTAble(T, nT, states)

    # output.txt
    with open('output.txt', 'w') as f:
        f.write('GRAMMAR\n')
        for rule in G:
            f.write(str(rule) + '\n')

        f.write('\nFIRST SETS\n')
        for key, value in first_sets.items():
            f.write(str(key) + ': ' + str(value) + '\n')

        f.write('\nFOLLOW SETS\n')
        for key, value in follow_sets.items():
            f.write(str(key) + ': ' + str(value) + '\n')
        
        f.write('\nSTATES:\n')   
        for s in states:
            f.write(str(s) + '\n') 

    return states