# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# Answer: 1366


def main() -> int:
    digits = list(int(d) for d in str(2**1000))
    return sum(digits)


if __name__ == '__main__':
    print(main())
