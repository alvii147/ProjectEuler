def compute_multiplication_digits(x: list[int], y: int) -> list[int]:
    reversed_digits = []
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        x_digit = x[i]
        mul = (x_digit * y) + carry
        reversed_digits.append(mul % 10)
        carry = mul // 10

    while carry > 0:
        reversed_digits.append(carry % 10)
        carry //= 10

    return list(reversed(reversed_digits))

def compute_power_digits(n: int, p: int) -> list[int]:
    value = [1]
    for _ in range(p):
        value = compute_multiplication_digits(value, n)

    return value

def compute_power_digit_sum(n: int, p: int) -> int:
    return sum(compute_power_digits(n, p))

if __name__ == '__main__':
    print('Answer:', compute_power_digit_sum(2, 1000))
