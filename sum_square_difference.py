# The sum of the sqaures of the first ten numbers is
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

# Answer: 25164150


def main() -> int:
    sum_squares = int()
    for n in range(1, 101):
        sum_squares += n**2
    
    square_sum = sum(range(1, 101))**2

    return square_sum - sum_squares


if __name__ == '__main__':
    print(main())
