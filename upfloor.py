



def UpFloor(inNumber):
    if inNumber == 1:
        return 1
    elif inNumber == 2:
        return 2

    stepOneBefore = 1
    stepTwoBefore = 2

    currentWays = 0
    for i in range(3,inNumber+1):
        currentWays = stepOneBefore + stepTwoBefore 
        stepTwoBefore = stepOneBefore
        stepOneBefore = currentWays

        # print(i)

    print("共有走法：",currentWays)


UpFloor(3)