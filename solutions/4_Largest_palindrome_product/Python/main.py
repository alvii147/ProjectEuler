def is_palindrome(n: int) -> bool:
    """
    Check if number is palindrome
    """
    str_n = str(n)
    half_len = len(str_n) // 2

    return str_n[:half_len] == str_n[-half_len:][::-1]


def get_largest_palindrome_product() -> int:
    """
    Compute the largest palindrome product of two three-digit numbers.
    """
    largest_palindrome_product = -1
    # iterate over three-digit numbers
    for i in range(100, 1000):
        # iterate over the other possible three-digit numbers
        # we can skip all numbers that won't result in a product higher than the current maximum
        for j in range(max(i, largest_palindrome_product // i), 1000):
            prod = i * j
            if prod > largest_palindrome_product and is_palindrome(prod):
                largest_palindrome_product = prod

    return largest_palindrome_product


if __name__ == '__main__':
    print('Answer:', get_largest_palindrome_product())
