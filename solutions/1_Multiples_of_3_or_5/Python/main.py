def compute_sum_of_multiples(n: int, *nums: tuple[int]) -> int:
    """
    Compute sum of all multiples of nums under n
    """
    # maintain set of all multiples
    multiples = set()
    for num in nums:
        # update multiples with union of current multiples
        # and the multiples of each value in nums
        multiples.update(range(num, n, num))

    # return sum of multiples
    return sum(multiples)


if __name__ == '__main__':
    print('Answer:', compute_sum_of_multiples(1000, 3, 5))
