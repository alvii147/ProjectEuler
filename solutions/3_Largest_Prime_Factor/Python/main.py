def is_prime(n: int) -> bool:
    """
    Check if number is prime.
    """
    # 2 is prime
    if n == 2:
        return True

    # anything lower than 2 is not prime
    # even numbers are not prime
    if n < 2 or n % 2 == 0:
        return False

    # iterate over odd numbers from 3 to square root of n
    # check if any divides n
    # if so, n is not prime
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # n is prime otherwise
    return True


def get_largest_prime_factor(n: int) -> int | None:
    """
    Compute the largest prime factor of given number.
    """
    # store small factors to check for later
    small_factors = [2] if n % 2 == 0 else []

    # iterate over odd numbers from 3 to square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        # if n is not divisible by current number, skip
        if n % i != 0:
            continue

        # if the larger factor is prime, we found the largest prime factor
        large_factor = n // i
        if is_prime(large_factor):
            return large_factor

        # add small factor to list of small factors to check for later
        small_factors.append(i)

    # iterate over small factors and check if prime
    # doing so in reverse order guarantees that the first prime factor
    # is the largest one
    for i in range(len(small_factors) - 1, -1, -1):
        if is_prime(small_factors[i]):
            return small_factors[i]

    return None


if __name__ == '__main__':
    print('Answer:', get_largest_prime_factor(600_851_475_143))
