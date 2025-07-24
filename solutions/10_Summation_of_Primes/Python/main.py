def get_prime_sum_under(n: int) -> int:
    """
    Gets sum of all primes under a given value.
    """
    # hardcode 2 as first prime number
    primes = [2]
    # maintain sum of primes
    prime_sum = sum(primes)

    for i in range(3, n, 2):
        sqrt_i = i ** 0.5
        for prime in primes:
            # if we've exceeded the number's square root
            # without finding a prime that divides the number
            # then it is a prime number
            if prime > sqrt_i:
                primes.append(i)
                prime_sum += i
                break

            # if the number is divisible by a smaller prime number
            # then it is not prime
            if i % prime == 0:
                break

    return prime_sum


if __name__ == '__main__':
    print('Answer:', get_prime_sum_under(2_000_000))
