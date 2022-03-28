def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False

    sqrt_n = n ** 0.5
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False

    return True

n = 600851475143

sqrt_n = n ** 0.5
largest_prime_factor = -1
for i in range(3, int(sqrt_n) + 1, 2):
    if n % i == 0:
        lower_factor = i
        higher_factor = n / i
        if is_prime(higher_factor) and largest_prime_factor < higher_factor:
            largest_prime_factor = higher_factor
            break
        elif is_prime(lower_factor) and largest_prime_factor < lower_factor:
            largest_prime_factor = lower_factor

print('Answer:', largest_prime_factor)