def factorial(n: int) -> int:
    """
    Recursively calculate n!.
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

def factorial_over_factorial(n: int, m: int) -> int:
    """
    Calculate n! / m!, which is equivalent to
    n x (n - 1) x (n - 2) x ... x (m + 2) x (m + 1)
    """
    value = 1
    for i in range(n, m, -1):
        value *= i

    return value

def lattice_paths(n: int) -> int:
    """
    Calculate number of lattice paths in nxn grid.

    At each point, we can either go right or down.
    Since we move from top left to bottom right,
    there must be a total of n right movements and
    n down movements. This means, the number of
    lattice paths is simply the number of permutations
    of right and down movements.

    Total number of movements is 2n (n right, n down).
    So number of total permutations is (2n)!.
    However, the order of right movements doesn't matter,
    so we can divide this by n!. Similarly, the order of
    down movements doesn't matter, so we can divide this
    by n! again, giving us the total number of lattice
    paths of (2n)! / (n! * n!).
    """
    return factorial_over_factorial(2 * n, n) // factorial(n)

if __name__ == '__main__':
    print('Answer:', lattice_paths(20))
