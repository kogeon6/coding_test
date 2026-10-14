def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    people.sort(reverse = True)
    print(people)
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1    
        answer += 1
        
    return answer

# 두 개를 더해서 최댓값 순서대로 나열을 해. 일단 인덱스를 기억하고 있어야 해. 
# if 100 이하인 애들은 pop 해줘.
# 두 개 짜리 전부 끝나면 나머지는 그냥 읽어주기