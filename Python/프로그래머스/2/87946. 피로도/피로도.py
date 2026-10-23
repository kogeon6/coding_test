from itertools import permutations

def solution(k, dungeons):
    life=k
    answer = 0
    count = 0
    for i in permutations(dungeons,len(dungeons)):
        
        i = list(i)
        for j in range(len(i)):
            if life>=i[j][0]:
                life -= i[j][1]
                count+=1
                if count>answer:
                    answer = count
            else:
                
                life=k
                count = 0
                break
                
    
    return answer