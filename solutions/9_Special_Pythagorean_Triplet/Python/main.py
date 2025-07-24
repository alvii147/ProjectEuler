def get_pythagorean_triplet_with_sum(target_sum: int) -> tuple[int, int, int] | None:
    """
    Get Pythagorean triplet that adds up to target sum.
    """
    # iterate over values of a
    # a < b < c, so a cannot exceed a third of the target sum
    for a in range(1, target_sum // 3):
        # iterate over values of b
        # b < c, so b cannot exceed half of the difference between the target sum and a
        for b in range(a + 1, (target_sum - a) // 2):
            # c is what is left in the target sum
            c = target_sum - a - b
            # if a^2 + b^2 = c^2, we've found the Pythagorean triplet
            if (a ** 2) + (b ** 2) == (c ** 2):
                return a, b, c

    return None


def get_pythagorean_triplet_product_with_sum(target_sum: int) -> int | None:
    """
    Get the product of the Pythagorean triplet that adds up to target sum.
    """
    triplet = get_pythagorean_triplet_with_sum(target_sum)
    if triplet is None:
        return None

    a, b, c = triplet

    return a * b * c


if __name__ == '__main__':
    print('Answer', get_pythagorean_triplet_product_with_sum(1000))
