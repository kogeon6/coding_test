from itertools import permutations

def solution(numbers):
    answer = 0
    array = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            number = int(''.join(j))
            array.add(number)
            
    
    array =    list(array)
    answer = len(array)
    print(array)
    for i in range(len(array)):
        if array[i] <=1:
            answer -=1
        for j in range(2, array[i]):
            if array[i] % j == 0:
                
                    answer -=1
                    break
    return answer