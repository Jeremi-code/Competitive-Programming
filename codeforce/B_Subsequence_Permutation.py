def Subsequence_Permutation(): 
    test_case_count = int(input(""))
    while(test_case_count ):
        length=int(input(''))
        word = input('')
        str_cp = list(word)
        str_sorted = sorted(str_cp)
        count = 0
        for i in range(length):
            if str_cp[i] != str_sorted[i]:
                count = count + 1
        print(count)
        test_case_count = test_case_count - 1

Subsequence_Permutation()
