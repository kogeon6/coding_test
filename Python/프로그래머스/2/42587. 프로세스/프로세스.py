# def solution(priorities, location):
#     answer = 0
    
#     index = list(range(len(priorities)))
#     print(priorities)
#     print(index)
    
#     while priorities:
#         current = priorities.pop(0)
#         current_index = index.pop(0)
        
#         if priorities and current <max(priorities):
#             priorities.append(current)
#             index.append(current_index)
#         else:
#             answer += 1
        
#             if current_index == location :
#                 return answer
        
    

    
    
    

# # 2 3 0 1
# 1 2 3 4
# # 2 3 4 5 0 1


def solution(priorities, location):
    answer = 0
    index = []
    for i in range(len(priorities)):
        index.append(i)
    print(index)
    count = 0
    while priorities:
        current = priorities.pop(0)
        current_index = index.pop(0)
        count += 1
        if priorities and current < max(priorities):
            priorities.append(current)
            index.append(current_index)
            count -= 1
        elif current_index==location:
            return count
    
        
        
        
    return answer

