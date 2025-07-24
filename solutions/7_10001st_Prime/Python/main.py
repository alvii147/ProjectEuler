def get_nth_prime(n: int) -> int:
    """
    Gets the nth prime number.
    """
    # allocate space for first n prime numbers
    primes = [0] * n
    # hardcode 2 as first prime number
    primes[0] = 2
    # maintain a count for the number of prime numbers calculated
    n_primes = 1
    # start from 3 to iterate over potential prime numbers
    i = 3

    # keep building prime numbers until we have n prime numbers
    while n_primes < n:
        sqrt_i = i ** 0.5
        # iterate over previously found prime numbers
        for j in range(n_primes):
            # if we've exceeded the number's square root
            # without finding a prime that divides the current number
            # then it is a prime number
            if primes[j] > sqrt_i:
                primes[n_primes] = i
                n_primes += 1
                break

            # if the number is divisible by a smaller prime number
            # then it is not prime
            if i % primes[j] == 0:
                break

        # increment by 2, as even numbers are not prime
        i += 2

    return primes[-1]


if __name__ == '__main__':
    print('Answer:', get_nth_prime(10001))
