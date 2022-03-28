sum_of_multiples = 0

for i in range(3, 1000, 3):
    sum_of_multiples += i

for i in range(5, 1000, 5):
    if i % 3 != 0:
        sum_of_multiples += i

print('Answer:', sum_of_multiples)
