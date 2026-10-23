# def solution(array, commands):
#     answer = []
    
#     for i in range(len(commands)):
#         tmp = []
#         for j in range(commands[i][0]-1,commands[i][1]):
#             tmp.append(array[j])
#         tmp.sort()
#         answer.append(tmp[commands[i][2]-1])
        
#     return answer









def solution(array, commands):
    answer = []
    temp=[]
    
    for i in commands:
        start = i[0]-1
        end = i[1]
        select = i[2] -1
        temp =[]
        for i in range(start, end):
            
            temp.append(array[i])
        temp.sort()
        answer.append(temp[select])
        print(temp)
    return answer