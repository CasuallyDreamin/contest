import math
from sys import exit

def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

def find_proper_divisors(n):
    
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != 1 and i != n // i and n // i != n:
                divisors.add(n // i)
    divisors.discard(n)  # remove the number itself if present
    return sorted(divisors)

def check_sum_of_divisors(n):

    divisors = find_proper_divisors(n)
    total = sum(divisors)
    if is_power_of_two(total):
        return 1
    else:
        return 0

def main():
    try:
        n = int(input("num: "))
        if n > 2**14 or n < 1:
            exit("Invalid input")
    except ValueError:
        exit("Invalid input")

    print(check_sum_of_divisors(n))

if __name__ == "__main__":
    main()