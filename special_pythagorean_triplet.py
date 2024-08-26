# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which, a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer: 31875000


def main() -> int:
    counter = 0
    for a in range(1, 332):
        for b in range(a+1, 500):
            for c in range(b+1, 501):
                counter += 1
                if c**2 == a**2 + b**2 and a + b + c == 1000:
                    print(f"a: {a}")
                    print(f"b: {b}")
                    print(f"c: {c}")
                    print(f"counter: {counter}")
                    return a * b * c


if __name__ == '__main__':
    print(main())
