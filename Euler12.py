def get_factors(n):
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    return factors

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check if n is divisible by any number from 2 to square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    total = 0
    num_fax = 0
    i = 1
    while num_fax < 502:
        total += i
        if is_prime(total):
            i+=1
            continue
        num_fax = len(get_factors(total))
        i+=1
    print(total)
main()
