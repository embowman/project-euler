# The sequence of triangle numbers is generated by adding the natural
# numbers. So the 7th triangle number would be:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
 
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# Answer: 76576500


def main() -> int:
    dividend = 0
    for counter in range(12376):
        dividend += counter
        num_divisors = 0
        for n in range(1, int(dividend**0.5)):
            if dividend % n:
                continue
            if num_divisors == 250:
                return dividend
            num_divisors += 1


if __name__ == '__main__':
    print(main())
