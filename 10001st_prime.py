# By listing the first six prime numbers: 2, 3, 5, 7, and 11, we can see that the 6th prime is 13.

# What is the 10001st prime number?

# Answer: 104743

def sieve(limit: int) -> list[int]:
    primes = list(True for _ in range(limit+1))
    i = 2
    while i < limit:
        if primes[i]:
            for j in range(i*2, limit+1, i):
                primes[j] = False
        i += 1

    return list(i for i in range(2, limit+1) if primes[i])

# def main() -> int:
#     # limit = 104743
#     limit = 10001
#     while True:
#         primes = sieve(limit=limit)
#         if len(primes) >= 10001:
#             print(len(primes))
#             return primes[10000]
#         limit *= 2

def main() -> int:
    lp = rp = 10001
    while True:
        print(f"lp: {lp}")
        print(f"rp: {rp}")
        print()
        primes = sieve(limit=rp)
        if len(primes) == 10001:
            return rp
        if len(primes) < 10001:
            lp = rp
        if len(primes) > 10001:
            break
        rp *= 2
    
    while True:
        m = (lp + rp) // 2
        print(f"lp: {lp}")
        print(f"m: {m}")
        print(f"rp: {rp}")
        print()
        primes = sieve(limit=m)
        if len(primes) == 10001:
            break
        if len(primes) < 10001:
            lp = m
        if len(primes) > 10001:
            rp = m
    
    while len(sieve(limit=m)) == 10001:
        print(f"m: {m}")
        print()
        m-= 1

    return m+1


if __name__ == '__main__':
    print(main())