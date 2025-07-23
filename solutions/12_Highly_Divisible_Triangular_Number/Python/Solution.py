import math
from functools import lru_cache


@lru_cache(maxsize=1, typed=False)
def sum_natural_numbers(n: int) -> int:
    if n <= 1:
        return n

    return n + sum_natural_numbers(n - 1)


def get_divisors_count(n: int) -> int:
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

if __name__ == '__main__':
    i = 1
    triangle_num_with_500_divisors = None
    while True:
        triangle_num = sum_natural_numbers(i)
        if get_divisors_count(triangle_num) > 500:
            triangle_num_with_500_divisors = triangle_num
            break

        i += 1

    print('Answer:', triangle_num_with_500_divisors)
