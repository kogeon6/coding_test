def solution(n, lost, reserve):
    
    
       
    same = []

    for student in lost:
        if student in reserve:
            same.append(student)

    for student in same:
        lost.remove(student)
        reserve.remove(student)
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        if not reserve:
            return answer
        for j in range(len(reserve)):
            
            
            if lost[i]== reserve[j]+1 or lost[i]== reserve[j]-1:
                
                del(reserve[j])
                answer+=1
                break
    print(reserve)
    print(lost)
    return answer

# lost reserve 같은 거를 찾아. 찾는다면, 그 둘 다 항 삭제.
# elif lost가 reserve의 +1과 같은 게 있다 그러면 그 둘 다 항 삭제
# elif lost가 reserve의 -1과 같은 게 있다 그러면 그 둘 다 항 삭제
# 최종적으로 n에서 lost 개수 빼서 answer 반환