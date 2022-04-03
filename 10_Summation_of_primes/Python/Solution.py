prime_list = [2]
prime_sum = 2

def is_prime_sequential(n):
    sqrt_n = n ** 0.5
    for i in prime_list:
        if i > sqrt_n:
            break

        if n % i == 0:
            return False

    return True

for i in range(3, 2000000, 2):
    if is_prime_sequential(i):
        prime_list.append(i)
        prime_sum += i

print('Answer:', prime_sum)
