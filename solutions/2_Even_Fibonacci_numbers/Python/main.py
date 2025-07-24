from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """
    Recursively compute nth Fibonacci number.
    This function employs memoization to improve performance.
    """
    # return zero for zeroth or negative index
    # to accommodate the recursive case of 2nd Fibonacci number
    if n < 1:
        return 0

    # base case for first number
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def even_valued_fibonacci_sum(max_value: int) -> int:
    """
    Compute summation of even-valued Fibonacci numbers
    not exceeding the given maximum value.
    Fibonacci numbers are even if and only if the previous
    two numbers are odd. Thus, we can simply sum over every
    third Fibonacci number.
    """
    i = 3
    fib_sum = 0

    while True:
        f = fibonacci(i)
        if f > max_value:
            break

        fib_sum += fibonacci(i)
        i += 3

    return fib_sum


if __name__ == '__main__':
    print('Answer:', even_valued_fibonacci_sum(4_000_000))
