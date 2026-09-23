def solution(brown, yellow):
    answer = []
    array=[0] *2
    array_yellow=[]
    array_brown=[0]*2
    if yellow == 1:
            array[0] = 1
            array[1] = 1
            array_yellow.append(array)
    for i in range(1, yellow):
        if yellow % i == 0:
            array[0] = i
            array[1] = int(yellow / i)
            if i>int(yellow / i):
                break
            array_yellow.append(array)
            array=[0] *2
    for i in array_yellow:
        if (i[0] + i[1] + 2) *2 == brown:
            array_brown[0] = i[1] +2
            array_brown[1] = i[0]+2
            break
    
    return array_brown

# (4+2),(6+2) <- 4*6 <- (5+7) *2
# (1+2),(1+2) <- 1*1 <- (2+2) *2
# (1+2),(2+2) <- 1*2 <- (2+3) *2

# 가운데꺼 뽑고, (yellow) 오른쪽꺼 맞는지 검증(brown)
# 왼쪽은 그냥  더하고 정렬하는 거