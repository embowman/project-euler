# Starting in the top left corner of a  grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# Answer: 137846528820


def main() -> int:
    n = 20
    numerator = 1
    for i in range(2, n*2+1):
        numerator *= i
    denominator = 1
    for i in range(2, n+1):
        denominator *= i
    denominator = denominator**2
    return numerator // denominator


if __name__ == '__main__':
    print(main())
