useful_factors = [11, 12, 13, 14, 15, 16, 17, 18, 19][::-1]
smallest_multiple = -1
n = 20
while smallest_multiple < 0:
    divisible = True
    for i in useful_factors:
        if n % i != 0:
            divisible = False
            break

    if divisible:
        smallest_multiple = n
    else:
        n += 20

print('Answer:', smallest_multiple)
