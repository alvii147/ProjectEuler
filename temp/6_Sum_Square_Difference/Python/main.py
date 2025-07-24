def get_sum_of_squares(n: int) -> int:
    """
    Compute sum of squares from 1 to n.
    """
    return sum(i ** 2 for i in range(1, n + 1))


def get_square_of_sum(n: int) -> int:
    """
    Compute square of sum from 1 to n.
    """
    return sum(range(1, n + 1)) ** 2


def get_sum_square_difference(n: int) -> int:
    """
    Compute sum square difference from 1 to n.
    """
    return get_square_of_sum(n) - get_sum_of_squares(n)


if __name__ == '__main__':
    print('Answer:', get_sum_square_difference(100))
