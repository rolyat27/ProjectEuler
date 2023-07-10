def get_prime_list(n):
    prime = [True for i in range(n+1)]
    i = 2
    while i*i <= n:
        if prime[i] == True:
            for j in range(i*i, n+1, i):
                prime[j] = False
        i += 1
    prime_list = [i for i in range(2, n+1) if prime[i]]
    return sum(prime_list)
def main():
    print(get_prime_list(2000000))
main()

