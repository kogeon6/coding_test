def solution(survey, choices):
    answer = ''
    array = ["RT", "CF","JM","AN"]
    count_A = 0
    count_N = 0
    count_J = 0
    count_M = 0
    count_C = 0
    count_F = 0
    count_R = 0
    count_T = 0
    for i in range(len(survey)):
        if survey[i] =="AN":
            if choices[i] == 1:
                count_A +=3
            if choices[i] == 2:
                count_A +=2
            if choices[i] == 3:
                count_A +=1
            if choices[i] == 5:
                count_N +=1
            if choices[i] == 6:
                count_N +=2
            if choices[i] == 7:
                count_N +=3
        if survey[i] =="NA":
            if choices[i] == 1:
                count_N +=3
            if choices[i] == 2:
                count_N +=2
            if choices[i] == 3:
                count_N +=1
            if choices[i] == 5:
                count_A +=1
            if choices[i] == 6:
                count_A +=2
            if choices[i] == 7:
                count_A +=3
        if survey[i] =="CF":
            if choices[i] == 1:
                count_C +=3
            if choices[i] == 2:
                count_C +=2
            if choices[i] == 3:
                count_C +=1
            if choices[i] == 5:
                count_F +=1
            if choices[i] == 6:
                count_F +=2
            if choices[i] == 7:
                count_F +=3
        if survey[i] =="FC":
            if choices[i] == 1:
                count_F +=3
            if choices[i] == 2:
                count_F +=2
            if choices[i] == 3:
                count_F +=1
            if choices[i] == 5:
                count_C +=1
            if choices[i] == 6:
                count_C +=2
            if choices[i] == 7:
                count_C +=3
        if survey[i] =="MJ":
            if choices[i] == 1:
                count_M +=3
            if choices[i] == 2:
                count_M +=2
            if choices[i] == 3:
                count_M +=1
            if choices[i] == 5:
                count_J +=1
            if choices[i] == 6:
                count_J +=2
            if choices[i] == 7:
                count_J +=3
        if survey[i] =="JM":
            if choices[i] == 1:
                count_J +=3
            if choices[i] == 2:
                count_J +=2
            if choices[i] == 3:
                count_J +=1
            if choices[i] == 5:
                count_M +=1
            if choices[i] == 6:
                count_M +=2
            if choices[i] == 7:
                count_M +=3
                
        if survey[i] =="RT":
            if choices[i] == 1:
                count_R +=3
            if choices[i] == 2:
                count_R +=2
            if choices[i] == 3:
                count_R +=1
            if choices[i] == 5:
                count_T +=1
            if choices[i] == 6:
                count_T +=2
            if choices[i] == 7:
                count_T +=3
        if survey[i] =="TR":
            if choices[i] == 1:
                count_T +=3
            if choices[i] == 2:
                count_T +=2
            if choices[i] == 3:
                count_T +=1
            if choices[i] == 5:
                count_R +=1
            if choices[i] == 6:
                count_R +=2
            if choices[i] == 7:
                count_R +=3
    print("count_A = ",count_A)
    print("count_N = ",count_N)
    print("count_C = ",count_C)
    print("count_F = ",count_F)
    print("count_M = ",count_M)
    print("count_J = ",count_J)
    print("count_R = ",count_R)
    print("count_T = ",count_T)
    
    if count_R>=count_T:
        answer+='R'
    else:
        answer+='T'
    if count_C>=count_F:
        answer+='C'
    else:
        answer+='F'
    if count_J>=count_M:
        answer+='J'
    else:
        answer+='M'
    if count_A>=count_N:
        answer+='A'
    else:
        answer+='N'
    
    return answer