# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

# Answer: 21124


def main() -> int:
    big_ol_string = ""
    for num in range(1, 1000):
        s = f"{num:0>3}"
        a_map = {
            "0": "", "1": "one", "2": "two", "3": "three", "4": "four",
            "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
            "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
            "14": "fourteen", "15": "fifteen", "16": "sixteen",
            "17": "seventeen", "18": "eighteen", "19": "nineteen"
        }
        b_map = {
            "0": "", "1": "", "2": "twenty", "3": "thirty",
            "4": "forty", "5": "fifty", "6": "sixty",
            "7": "seventy", "8": "eighty", "9": "ninety"
        }
        if s[0] != "0":
            big_ol_string += f"{a_map[s[0]]}hundred"
            if s[1:] == "00":
                continue
            big_ol_string += "and"
        if s[1] == "1":
            big_ol_string += a_map[s[1:]]
        else:
            big_ol_string += f"{b_map[s[1]]}{a_map[s[2]]}"
    return len(big_ol_string + "onethousand")


if __name__ == '__main__':
    print(main())
