def drome_check(n):
    numstr = str(n)
    rev = numstr[::-1]
    if numstr == rev:
        return True
    else:
        return False

def main():
    largest_drome = 0
    curr = 0
    for i in range(999, 899, -1):
        for j in range(999, 899, -1):
            curr = i*j
            if drome_check(curr):
                if curr > largest_drome:
                    largest_drome = curr
    print(largest_drome)
main()
