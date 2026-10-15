# def solution(bandage, health, attacks):
#     answer = health
#     time =0
#     con=0
#     end_time=attacks[-1][0]+1
#     while True:
#         print("time = ", time,end=" ")
        
#         if time == end_time:
#             break
        
#         if attacks[0][0] == time:
#             answer-=attacks.pop(0)[1]
#             con=0
#             if answer <=0:
#                 return -1
#         elif con == bandage[0]-1:
#             answer+=bandage[2]+bandage[1]
#             con=0
#             if answer>=health:
#                 answer=health
#         else:
#             answer+=bandage[1]
#             con+=1
#             if answer>=health:
#                 answer=health
#         time+=1
#         if time==1:
#             con=0
#         print("answer: ", answer,end=" ")
#         print("con = ",con)
#     return answer
























def solution(bandage, health, attacks):
    answer = health
    attack_time = 0
    time = attacks[-1][0]
    k=0
    for i in range(1, time+1):
        
        if i != attacks[0][0]:   
            
            attack_time += 1
            answer += bandage[1]
            if answer >health:
                answer = health
            elif attack_time == bandage[0]:
                answer += bandage[2]
                attack_time = 0
        else:
            attack_time = 0
            answer -= attacks[0][1]
            del attacks[0]             
        print("attack_time = ", attack_time, end=" ")
        print("time = ", i, end=" ")
        print("answer = ", answer)
        if answer <=0:
            return -1
    
    
    return answer




