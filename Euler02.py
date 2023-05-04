def main():
    prev = 1
    curr = 1
    fib = [1,1]
    i = 0
    even_sum = 0
    while curr < 4000000:
        prev, curr = curr, prev+curr
        fib.append(curr)
    for i in range(len(fib)):
        if fib[i]%2 == 0:
            even_sum += fib[i]
    print(even_sum)
main()

