# The following iterative sequence is defined for the set of positive
# integers:

# n -> n / 2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
# sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Answer: 837799


def main() -> int:
    memo = {1: 0}
    longest_chain_starter = 1
    longest_chain_length = 0

    for k in range(2, 1_000_000):
        counter = 0
        n = k
        while n != 1:
            if n in memo:
                counter += memo[n]
                break
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            counter += 1
        memo[k] = counter
        if counter >= longest_chain_length:
            longest_chain_length = counter
            if k > longest_chain_starter:
                longest_chain_starter = k

    return longest_chain_starter


if __name__ == '__main__':
    print(main())
