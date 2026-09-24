# def solution(phone_book):
#     answer = True
#     dict={}
#     array=[]
#     for key in phone_book:
#         if key not in dict:
#             dict[key] = key
#     print(dict)
#     min = 20
#     for key in dict:
#         if len(key) < min:
#             min = len(key)
#         if len(key) == min:
#             array.append(key)
#     print(array)
#     return answer




def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        min_len = min(len(phone_book[i]),len(phone_book[i+1]))
        for k in range(min_len):
            if phone_book[i][k]!= phone_book[i+1][k]:
                break
            elif k==min_len-1:
                return False
    return answer
# 완전 탐색 진행 i 랑 i+j
# i는 phone_book 길이 만큼
# j는 1부터 phone_book 길이 -i

# 이 내부에 i꺼만큼 길이 반복해서 다르면 break 끝까지 같으면 return true