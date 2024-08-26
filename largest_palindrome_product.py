# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

def main():
    pals = list(int(str(n)+str(n)[::-1]) for n in range(100, 999))
    prods = list()
    for n in pals:
        factors = list(f for f in range(100, 1000) if n % f == 0 and n / f < 1000)
        if factors:
            prods.append(n)

    return prods[-1]


if __name__ == '__main__':
    print(main())