def is_palindrome(n):
    str_n = str(n)
    half_len = len(str_n) // 2

    return str_n[:half_len] == str_n[-half_len:][::-1]

largest_palindrome_product = 0
for i in range(10, 1000):
    for j in range(max(i, largest_palindrome_product // i), 1000):
        prod = i * j
        if prod > largest_palindrome_product and is_palindrome(prod):
            largest_palindrome_product = prod

print('Answer:', largest_palindrome_product)
