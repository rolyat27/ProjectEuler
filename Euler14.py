def sequence(n):
    res = n
    seq_list = []
    while res != 1:
        if res %2 == 0:
            res = res/2
            seq_list.append(res)
        else:
            res = 3*res + 1
            seq_list.append(res)
    return seq_list
def main():
    longest_list = []
    curr_list = []
    generated_longest = 1
    for i in range(1,1000001):
        curr_list = sequence(i)
        if len(curr_list) > len(longest_list):
            longest_list = curr_list
            generated_longest = i

    print(generated_longest)
    print(longest_list)
main()

