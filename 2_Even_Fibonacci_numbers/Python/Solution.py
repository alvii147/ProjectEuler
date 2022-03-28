even_valued_sum = 0
term_1 = 1
term_2 = 1
term_3 = term_1 + term_2

while term_3 < 4000000:
    if term_3 % 2 == 0:
        even_valued_sum += term_3

    term_1 = term_2
    term_2 = term_3
    term_3 = term_1 + term_2

print('Answer:', even_valued_sum)
