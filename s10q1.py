import itertools


def solve_cryptarithmetic():
    letters = 'TWOFUR'

    for perm in itertools.permutations(range(10), len(letters)):
        T, W, O, F, U, R = perm

        TWO = T * 100 + W * 10 + O
        FOUR = F * 1000 + O * 100 + U * 10 + R

        if TWO + TWO == FOUR:
            return {
                'T': T, 'W': W, 'O': O,
                'F': F, 'U': U, 'R': R,
                'TWO': TWO, 'FOUR': FOUR
            }

    return None


solution = solve_cryptarithmetic()

if solution:
    print("Solution found!")
    print(f"TWO: {solution['TWO']}")
    print(f"FOUR: {solution['FOUR']:04d}")
    print("Digit assignments:")

    for letter in 'TWOFUR':
        print(f"{letter} = {solution[letter]}")
else:
    print("No solution found.")
