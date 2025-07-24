from functools import lru_cache


@lru_cache(maxsize=None)
def compute_collatz_sequence_length(n: int) -> int:
    """
    Get the length of Collatz sequence starting from n.
    """
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + compute_collatz_sequence_length(n // 2)

    return 1 + compute_collatz_sequence_length((3 * n) + 1)


def get_longest_collatz_sequence_starter_in_range(upto: int) -> int:
    """
    Get the longest Collatz sequence starter under given number:
    """
    longest_sequence_starter = None
    longest_sequence_length = 0
    for i in range(1, 1_000_000):
        sequence_length = compute_collatz_sequence_length(i)
        if sequence_length > longest_sequence_length:
            longest_sequence_starter = i
            longest_sequence_length = sequence_length

    return longest_sequence_starter


if __name__ == '__main__':
    print('Answer:', get_longest_collatz_sequence_starter_in_range(1_000_000))
