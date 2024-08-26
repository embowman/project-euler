# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

# Answer: 232792560


def sieve(limit: int) -> list[int]:
    primes = list(True for _ in range(limit+1))
    i = 2
    while i < limit:
        if primes[i]:
            for j in range(i*2, limit+1, i):
                primes[j] = False
        i += 1

    return list(i for i in range(2, limit+1) if primes[i])

def get_counts(product: int, factors: list[int]) -> dict:
    counts = dict()
    for f in factors:
        if f not in counts:
            counts[f] = 0
        while product % f == 0:
            counts[f] += 1
            product //= f
    
    return counts

def main() -> int:
    primes = sieve(limit=20)
    total_factors = dict()
    for n in range(2, 21):
        n_factors_list = list(p for p in primes if n % p == 0)
        n_factors_dict = get_counts(product=n, factors=n_factors_list)
        for f in n_factors_dict:
            if f not in total_factors:
                total_factors[f] = n_factors_dict[f]
                continue
            if total_factors[f] < n_factors_dict[f]:
                total_factors[f] = n_factors_dict[f]
                continue
    
    smallest_multiple = 1
    for f in total_factors:
        smallest_multiple *= f ** total_factors[f]

    return smallest_multiple


if __name__ == '__main__':
    print(main())
