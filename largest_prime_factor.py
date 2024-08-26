# The prime factors of 13195 are 5, 7, 13, and 29.

# What is the largest prime factor of the number 600851475143?
# Answer: 6857


def sieve(limit: int) -> list[int]:
    primes = list(True for _ in range(limit+1))
    i = 2
    while i < limit:
        if primes[i]:
            for j in range(i*2, limit+1, i):
                primes[j] = False
        i += 1

    return list(i for i in range(2, limit+1) if primes[i])

def main() -> int:
    primes = sieve(limit=int(600_851_475_143**0.5))
    factors = list(p for p in primes if 600_851_475_143 % p == 0)

    return factors[-1]


if __name__ == '__main__':
    print(main())
