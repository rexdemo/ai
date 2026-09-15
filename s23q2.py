from itertools import permutations


def is_valid_assignment(assignment):
    S = assignment['S']
    E = assignment['E']
    N = assignment['N']
    D = assignment['D']
    M = assignment['M']
    O = assignment['O']
    R = assignment['R']
    Y = assignment['Y']

    SEND = S * 1000 + E * 100 + N * 10 + D
    MORE = M * 1000 + O * 100 + R * 10 + E
    MONEY = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

    return S != 0 and M != 0 and SEND + MORE == MONEY


def solve_cryptarithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    valid_assignments = []

    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))

        if is_valid_assignment(assignment):
            valid_assignments.append(assignment)

    return valid_assignments


def print_solutions(solutions):
    for solution in solutions:
        print(
            f"{solution['S']}{solution['E']}{solution['N']}{solution['D']} + "
            f"{solution['M']}{solution['O']}{solution['R']}{solution['E']} = "
            f"{solution['M']}{solution['O']}{solution['N']}{solution['E']}{solution['Y']}"
        )

        print("Digit assignments:")
        for letter in ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']:
            print(f"{letter} = {solution[letter]}")


if __name__ == "__main__":
    print("Solving Cryptarithmetic Problem: SEND + MORE = MONEY")

    solutions = solve_cryptarithmetic()

    if solutions:
        print("Valid solutions found:")
        print_solutions(solutions)
    else:
        print("No solution found.")
