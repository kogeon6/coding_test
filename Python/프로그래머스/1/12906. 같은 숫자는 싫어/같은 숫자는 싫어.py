# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if i==0:
#             answer.append(arr[i])
#         elif arr[i-1] != arr[i]:
#             answer.append(arr[i])
        
#     return answer











def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer