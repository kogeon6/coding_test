def solution(n, w, num):
    answer = 1
    array = [[] for _ in range(w)]
    
    for i in range(1, n+1):
        for j in range(w):
            if i%(2*w) == 0:
                array[0].append(i)
                break
            elif i % (2*w) == w-j:
                array[w-1-j].append(i)
                break
            elif i%(2*w) == w+j+1:
                array[w-1-j].append(i)
                break
    print(array)
    
    for i in range(1, w+1):
        if num % (2*w) == 0:
            index = 0
        elif num % (2*w) == i:
            index = i-1
        elif num % (2*w) == 2*w -i:
            index = i
    while array[index][-1] != num:
        array[index].pop()
        answer+=1
    return answer

# w가 3일 때 2배 만큼 만들어준다.
# w만큼 외부 배열 만들어줘.
# 6으로 나눴을 때 0이나 1 나머지 나오면 첫번째. 내부 배열 append로 더해줘. 0
# 2나 5 나머지 나오면 두번째. 내부 배열 append로 더해줘.
# 3이나 4 나머지 나오면 세번째. 내부 배열 append로 더해줘.

# w가 4일 때 2배 만큼 만들어준다.
# w만큼 외부 배열 만들어줘. 외부 array를 array
# 8으로 나눴을 때 0이나 1 나머지 나오면 0번째. 내부 배열 append로 더해줘. j=3 
# 2나 7 나머지 나오면 1번째. 내부 배열 append로 더해줘. j =2
# 3이나 6 나머지 나오면 2번째. 내부 배열 append로 더해줘. j=1
# 4나 5 나머지 나오면 3번째. 내부 배열 append로 더해줘. j=0

                
# if i % (2*w) ==
# [-1]번째 나오면 break
# pop(-1)로 완성 시키기









# 0 / 1 / 2 / 3 / 4 / 5
# 0 1 / 2 11 / 3 10 / 4 9 / 5 8 / 6 7

# 0 / 1 / 2
# 0 1 / 2 5 / 3 4
# def solution(n, w, num):
#     number =0
#     answer = 0
#     array = [[] for _ in range(w)]
#     for i in range(1, n+1):
#         k = i%(2*w)
#         if k>=1 and k<=w:
#             array[k-1].append(i)
#         elif k % (2*w) == 0:
#             array[0].append(i)
#         else:
#             array[(2*w)-k].append(i)
    
#     if num % (2*w) <=w and num % (2*w) >=1:
#         index = num % (2*w)
#     elif num % (2*w) == 0:
#         index = 0
#     else:
#         index = (2*w) - (num % (2*w))
#     print(index)
    
#     while number !=num:
#         number = array[index].pop()
#         print(number)
#         answer+=1
#     return answer
