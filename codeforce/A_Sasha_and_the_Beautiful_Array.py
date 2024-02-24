def Beautiful_Array() :
    test_case_count = int(input(''))
    while(test_case_count):
        length = int(input('')) - 1
        numbers_str = input('').split(' ')
        numbers_int = [int(x) for x in numbers_str]
        numbers_sorted = sorted(numbers_int)
        total = 0
        while(length):
            substracted = numbers_sorted[length] - numbers_sorted[length-1]
            total= total + substracted
            length = length - 1
        print(total)
        test_case_count = test_case_count - 1

Beautiful_Array()