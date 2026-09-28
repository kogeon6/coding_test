def solution(N, stages):
    answer = []
    array = [0]*N
    number = len(stages)
    challenge_array=[0]*N
    for i in range(N):
        for j in range(number):
            if i+1 == stages[j]:
                array[i] += 1
    
    for i in range(N):
        challenge_array[i]=number
        number -= array[i]
    for i in range(len(array)):
        if challenge_array[i]==0:
            array[i]=0
        else:
            array[i] = array[i] / challenge_array[i]
    array_copy=[]
    array_copy=array.copy()
    array_copy.sort(reverse=True)
    print(array)
    print(array_copy)
    for i in range(len(array)):
        for j in range(len(array)):
            if array_copy[i]==array[j]:
                if (j+1) not in answer:
                    answer.append(j+1)
                    break
    return answer