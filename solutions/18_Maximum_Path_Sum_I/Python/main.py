triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def parse_tree(triangle: str) -> list[list[int]]:
    """
    Parse tree string into list of lists of integers.
    """
    return [[int(i) for i in line.split()] for line in triangle.strip().split('\n')]

def collapse(maximums: list[int], leaves: list[int]) -> list[int]:
    """
    Combine leaf values with running maximums. The new maximum is built
    by adding each leaf's value with the maximum of its children.
    """
    if len(maximums) - len(leaves) != 1:
        raise ValueError('Running maximums length should be one higher than the number of leaves')

    new_maximums = [0] * len(leaves)
    for i, leaf in enumerate(leaves):
        new_maximums[i] = leaf + max(maximums[i], maximums[i + 1])

    return new_maximums

def compute_maximum_path_sum(tree: list[list[int]]) -> int:
    maximums = [0] * (len(tree[-1]) + 1)
    for i in range(len(tree) - 1, -1, -1):
        maximums = collapse(maximums, tree[i])

    return maximums[0]

print('Answer:', compute_maximum_path_sum(parse_tree(triangle)))
