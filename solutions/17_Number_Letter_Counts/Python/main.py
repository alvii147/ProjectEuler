NUMBERS_TO_LETTERS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

HUNDRED = 'hundred'
THOUSAND = 'thousand'
AND = 'and'


def get_number_in_words(n: int) -> list[str]:
    if n > 1000 or n < 0:
        raise ValueError('n must be between 0 and 1000')

    if n in NUMBERS_TO_LETTERS:
        return [NUMBERS_TO_LETTERS[n]]

    if n == 1000:
        return [
            NUMBERS_TO_LETTERS[n // 1000],
            THOUSAND,
        ]

    units = n % 10
    if n < 100:
        return [
            NUMBERS_TO_LETTERS[n - units],
            NUMBERS_TO_LETTERS[units],
        ]

    tens = n % 100
    if tens == 0:
        return [
            NUMBERS_TO_LETTERS[n // 100],
            HUNDRED,
        ]

    if tens % 10 == 0 or tens > 10 and tens < 20:
        return [
            NUMBERS_TO_LETTERS[n // 100],
            HUNDRED,
            AND,
            NUMBERS_TO_LETTERS[(n % 100)],
        ]

    if units == tens:
        return [
            NUMBERS_TO_LETTERS[n // 100],
            HUNDRED,
            AND,
            NUMBERS_TO_LETTERS[units],
        ]

    return [
        NUMBERS_TO_LETTERS[n // 100],
        HUNDRED,
        AND,
        NUMBERS_TO_LETTERS[(n % 100) - units],
        NUMBERS_TO_LETTERS[units],
    ]


def get_list_len(l: list[str]):
    return sum(map(lambda x: len(x), l))


def get_sum_of_number_letters(n: int):
    return sum(get_list_len(get_number_in_words(i)) for i in range(1, n + 1))


if __name__ == '__main__':
    print('Answer:', get_sum_of_number_letters(1000))
