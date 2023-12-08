from generator_states import generateStateZero, generateStates
from generator_sets import generateFirstSets, generateFollowSets

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

def main():

    fileData = open('grammar.txt', 'r').readlines()

    # Grammar - list of rules (tuple: index, lhs, rhs)
    G, T, nT = import_grammar(fileData)
    # print(G)
    # print(T)
    # print(nT)

    generateStateZero(G)
    states = generateStates()

    # for s in states:
    #     print('State', s.orderNumber, '= goto(', s.prevStateOrderNumber, ',', s.gotoSymbol, ')', s.isCopy, s.copiedFromStateNumber)
    #     for t in s.transitions:            
    #         print('\t', t)

    first_sets = generateFirstSets(G, T, nT)
    for s in first_sets:
        print(s, first_sets[s])

    follow_sets = generateFollowSets(G, T, nT)
    for s in follow_sets:
        print(s, follow_sets[s])

if __name__ == "__main__":
    main()