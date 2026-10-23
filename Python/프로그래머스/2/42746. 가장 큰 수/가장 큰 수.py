# def solution(numbers):
#     answer = ''
#     numbers_array = []
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])
#         numbers_array.append([numbers[i] *4,numbers[i]])
    
    
#     numbers_array.sort(reverse=True)
#     for i in range(len(numbers_array)):
        
#         answer += numbers_array[i][1]
    
#     if answer[0] == "0":
#         return "0"
#     return answer






def solution(numbers):
    answer = ''
    array = []
    for i in numbers:
        array.append(str(i))
        
    array.sort(key = lambda x:x*4, reverse=True)
    
    
    for i in range(len(array)):
        answer += array[i]
    if answer[0] == '0':
        return '0'
    return answer




