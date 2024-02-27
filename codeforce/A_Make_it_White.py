def Make_it_white():
    cases = int(input(''))
    while (cases):
        firstIndex = 0
        lastIndex = 0
        MIN_BOX = 0
        length = int(input(''))
        boxList = input('')
        for index in range(length):
            if firstIndex == 0 and boxList[index] =='B':
                firstIndex = index + 1
            elif index >= firstIndex and boxList[index] =='B':
                lastIndex = index + 1
        if lastIndex == 0 and firstIndex == 0 :
            MIN_BOX = 0
        elif lastIndex == 0 :
            MIN_BOX = 1
        else :
            MIN_BOX = lastIndex - firstIndex + 1
        print(MIN_BOX)
        cases -= 1
Make_it_white()