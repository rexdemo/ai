import itertools


def solve_cryptarithmetic():
    letters = 'GOTU'

    for perm in itertools.permutations(range(10), len(letters)):
        G, O, T, U = perm

        if G == 0 or T == 0:
            continue

        GO = G * 10 + O
        TO = T * 10 + O
        OUT = O * 100 + U * 10 + T

        if GO + TO == OUT:
            return {
                'G': G,
                'O': O,
                'T': T,
                'U': U,
                'GO': GO,
                'TO': TO,
                'OUT': OUT
            }

    return None


solution = solve_cryptarithmetic()

if solution:
    print("Solution found!")
    print(f"GO: {solution['GO']}")
    print(f"TO: {solution['TO']}")
    print(f"OUT: {solution['OUT']}")

    print("Digit assignments:")
    for letter in 'GOTU':
        print(f"{letter} = {solution[letter]}")
else:
    print("No solution found.")
