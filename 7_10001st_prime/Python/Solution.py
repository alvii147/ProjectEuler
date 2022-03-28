def is_prime(n):
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    sqrt_n = n ** 0.5
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False

    return True

def nth_prime(n):
    if n == 1:
        return 2

    prime = 3
    prime_count = 2
    while prime_count < n:
        prime += 2
        if is_prime(prime):
            prime_count += 1

    return prime

prime_10001 = nth_prime(10001)

print('Answer:', prime_10001)
