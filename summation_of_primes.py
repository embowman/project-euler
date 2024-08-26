# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Answer: 142913828922

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
    return sum(sieve(limit=2_000_000))


if __name__ == '__main__':
    print(main())
