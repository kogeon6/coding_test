def solution(sizes):
    answer = 0
    array1=[]
    index = 0
    array2=[]
    while sizes[index] != sizes[-1]:
        index+=1
    for i in range(index+1):
        array1.append(sizes[i][0])
        array1.append(sizes[i][1])
    
    array1.sort()
    answer1 = array1[-1]
    
    for i in range(index+1):
        if sizes[i][0] <= sizes[i][1]:
            min = sizes[i][0]
        else:
            min = sizes[i][1]
        array2.append(min)
    array2.sort()
    answer2 = array2[-1]
    answer = answer1 * answer2
    return answer

# 우선 가장 큰 거는 뽑아야 돼.
# 하나씩 다 탐색해서, 둘 중 더 작은 거를 뽑아
# 그 중에 가장 커야 함.
