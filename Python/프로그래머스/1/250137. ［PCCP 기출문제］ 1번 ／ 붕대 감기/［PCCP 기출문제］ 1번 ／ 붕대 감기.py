def solution(bandage, health, attacks):
    answer = health
    time =0
    con=0
    end_time=attacks[-1][0]+1
    while True:
        print("time = ", time,end=" ")
        
        if time == end_time:
            break
        
        if attacks[0][0] == time:
            answer-=attacks.pop(0)[1]
            con=0
            if answer <=0:
                return -1
        elif con == bandage[0]-1:
            answer+=bandage[2]+bandage[1]
            con=0
            if answer>=health:
                answer=health
        else:
            answer+=bandage[1]
            con+=1
            if answer>=health:
                answer=health
        time+=1
        if time==1:
            con=0
        print("answer: ", answer,end=" ")
        print("con = ",con)
    return answer