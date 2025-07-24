import math
from functools import lru_cache


@lru_cache(maxsize=1, typed=False)
def sum_natural_numbers(n: int) -> int:
    """
    Recursively compute sum of first n natural numbers.
    """
    if n <= 1:
        return n

    return n + sum_natural_numbers(n - 1)


def get_divisors_count(n: int) -> int:
    """
    Get number of divisors for n.
    """
    if n == 1:
        return 1

    divisors_count = 2
    sqrt = n ** 0.5
    sqrt_ceil = math.ceil(sqrt)
    if sqrt == sqrt_ceil:
        divisors_count += 1

    for i in range(2, sqrt_ceil):
        if n % i == 0:
            divisors_count += 2

    return divisors_count


def get_first_triangle_num_with_divisors(num_divisors: int) -> int:
    """
    Get first triangle number with more than the given number of divisors.
    """
    n = 1
    while True:
        triangle_num = sum_natural_numbers(n)
        if get_divisors_count(triangle_num) > num_divisors:
            return triangle_num

        n += 1


if __name__ == '__main__':
    print('Answer:', get_first_triangle_num_with_divisors(500))
