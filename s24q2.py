from itertools import permutations


def is_valid_assignment(assignment):
    C = assignment['C']
    R = assignment['R']
    O = assignment['O']
    S = assignment['S']
    A = assignment['A']
    D = assignment['D']
    N = assignment['N']
    G = assignment['G']
    E = assignment['E']

    CROSS = C * 10000 + R * 1000 + O * 100 + S * 10 + S
    ROADS = R * 10000 + O * 1000 + A * 100 + D * 10 + S
    DANGER = D * 100000 + A * 10000 + N * 1000 + G * 100 + E * 10 + R

    return CROSS + ROADS == DANGER


def solve_cryptarithmetic():
    letters = ['C', 'R', 'O', 'S', 'A', 'D', 'N', 'G', 'E']
    valid_assignments = []

    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))

        if is_valid_assignment(assignment):
            valid_assignments.append(assignment)

    return valid_assignments


def print_solutions(solutions):
    for solution in solutions:
        print(
            f"{solution['C']}{solution['R']}{solution['O']}{solution['S']}{solution['S']} + "
            f"{solution['R']}{solution['O']}{solution['A']}{solution['D']}{solution['S']} = "
            f"{solution['D']}{solution['A']}{solution['N']}{solution['G']}{solution['E']}{solution['R']}"
        )

        print("Digit assignments:")
        for letter in ['C', 'R', 'O', 'S', 'A', 'D', 'N', 'G', 'E']:
            print(f"{letter} = {solution[letter]}")


if __name__ == "__main__":
    print("Solving Cryptarithmetic Problem: CROSS + ROADS = DANGER")

    solutions = solve_cryptarithmetic()

    if solutions:
        print("Valid solutions found:")
        print_solutions(solutions)
    else:
        print("No solution found.")
