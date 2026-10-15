# def solution(s):
#     answer = True
#     cnt_left = 0
#     cnt_right = 0
#     if s[0] != "(" or s[-1] != ")":
#         return False
#     for i in range(len(s)):
#         if s[i] == "(":
#             cnt_left += 1
#         elif s[i] == ")":
#             cnt_right +=1
#         if cnt_right>cnt_left:
#             return False
#     if cnt_left == cnt_right:
#         return True
#     else:
#         return False

# # 처음부터 끝까지 쭉 훑는다 (for문)
# # 처음이 (가 아니거나 )가 아니면 그냥 false 반환
# # 그냥 왼쪽이랑 오른쪽 개수 같으면 True 반환
# # (())) 이렇게 되면 안됨













def solution(s):
    answer = False
    array = []
    if s == "":
        return False
    for i in range(len(s)):
        array.append(s[i])
        
        if len(array) >=2:
            if array[-1] ==")" and array[-2] =="(":
                del(array[-1])
                del(array[-1])
        
    if array == []:
        return True
    else:   
        return False
    