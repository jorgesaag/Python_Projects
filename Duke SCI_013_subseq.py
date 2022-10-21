import sys

def maxSeq(list):
    bi = 1
    max_seq_val = 1
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return 1
    else:
        while bi < len(list):
            if list[bi] > list[bi - 1]:
                i = bi
                length = 1
                while i < len(list) and list[i] > list[i - 1]:
                    length += 1
                    i += 1
                    bi = i
                    max_seq_val = max(max_seq_val, length)
            else:
                bi += 1
    return max_seq_val


def check(input_list, expected_answer):
    print("Testing maxSeq(" + str(input_list) + ")")
    ans = maxSeq(input_list)
    if(ans == expected_answer):
        print(" → maxSeq passed this test case")
    else:
        print(" → maxSeq failed this test: got " + str(ans) + " but expected " + str(expected_answer))
        sys.exit(1)
        pass
    pass

#test cases
check([1, 2, 3], 3)
check([], 0)
check([1, 2, 3, 3, 4], 3)
check([1, 2, 3, 4], 4)
check([1, 2, 3, 1, 5, 7, 8, 9], 5)
check([-1, 0, 1, 2, 3], 5)