# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 4, 6, and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168


def main() -> int:
    multiples = list(range(0, 1000, 3))
    multiples.extend(range(0, 1000, 5))
    multiples = set(multiples)

    return sum(multiples)


if __name__ == '__main__':
    print(main())
