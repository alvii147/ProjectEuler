def gcd(x: int, y: int) -> int:
    """
    Recursively compute the greatest common divisor
    of two numbers using the Euclidean algorithm.
    """
    if x == 0:
        return y

    return gcd(y % x, x)


def lcm(*x: list[int]) -> int:
    """
    Recursively compute the lowest com
    """
    if len(x) < 2:
        raise ValueError('cannot compute LCM of one or less numbers')

    lcm_first_pair = (x[0] * x[1]) // gcd(x[0], x[1])

    if len(x) == 2:
        return lcm_first_pair

    return lcm(lcm_first_pair, *x[2:])


if __name__ == '__main__':
    print('Answer:', lcm(*list(range(1, 20))))
