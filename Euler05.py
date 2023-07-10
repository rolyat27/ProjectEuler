#i learned in the worst thing ive ever made that to do this problem you only need to check divisibility by 11-20, because all the other numbers <20 are factors of those.

def main():
    num = 40
    divisor = 20
    while divisor > 10:
        if num%divisor == 0:
            divisor -= 1
        else:
            num += 20
            divisor = 20
    print(num)
main()
