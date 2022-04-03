pythagorean_triplet_product = 0
break_loop = False
for a in range(1, 1001):
    for b in range(a, 1001):
        c = 1000 - a - b
        if (a ** 2) + (b ** 2) == c ** 2:
            pythagorean_triplet_product = a * b * c
            print(a, b, c)
            break_loop = True

        if break_loop:
            break

    if break_loop:
        break

print('Answer:', pythagorean_triplet_product)
