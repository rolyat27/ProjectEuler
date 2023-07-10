def main():
    lst = [int(i) for i in range(101)]
    square_sum = (sum(lst))**2
    sum_square = 0 
    for i in lst:
        sum_square += i*i
    diff = square_sum - sum_square
    print(diff)
main()

