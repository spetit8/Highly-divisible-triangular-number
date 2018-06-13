import math

def FindTriNum():
    Number = 1
    TriNum = 1
    LastTriNum = 1
    DivCount = 0
    MaxDivCount = 0

    while(True):
        Number += 1
        TriNum = LastTriNum + Number
        # print(TriNum)
        for i in range(1, int(math.ceil(math.sqrt(TriNum)))):
            if TriNum % i == 0:
                DivCount += 2
                if DivCount > 500:
                    return print(TriNum)

        if DivCount > MaxDivCount:
            MaxDivCount = DivCount
            print(MaxDivCount)
        DivCount = 1
        LastTriNum = TriNum

FindTriNum()
