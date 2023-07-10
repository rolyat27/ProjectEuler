def is_prime(n):
    divisor = 2
    prime = True
    while divisor <= n/2:
        if n%divisor == 0:
            prime = False
            break
        divisor += 1
    return prime

def main():
    prime_list = [2]
    cap = 10001
    i = 3
    while len(prime_list) < cap:
        if is_prime(i):
            prime_list.append(i)
        i += 2
    print(prime_list[-1])
main()

