from itertools import product


def solution(word):
    answer = 0
    array = []
    result = []
    for i in range(1,6):
        array.extend(product("AEIOU", repeat=i))
        
    for i in range(len(array)):
        result.append(''.join(array[i]))
    result.sort()
    print(result)
    
    for i in range(len(result)):
        if word == result[i]:
            answer =i+1
    return answer