# def solution(genres, plays):
#     answer = []
#     genres_dict = {}
#     genres_play_dict = {}
#     for i in range(len(genres)):
#         if genres[i] not in genres_dict:
#             genres_dict[genres[i]]=[]
        
#         genres_dict[genres[i]].append([i,plays[i]])
#     for key in genres_dict:
#         genres_dict[key].sort(key = lambda x:x[1], reverse=True)
    
#     print(genres_dict)
#     result = sorted(
#         genres_dict.items(),
#         key = lambda x: sum(i[1] for i in x[1]),
#         reverse=True
#     )
#     print(result)
    
#     for i in result:
#         if len(i[1]) >= 2:
#             answer.append(i[1][0][0])
#             answer.append(i[1][1][0])
#         elif len(i[1]) == 1:
#             answer.append(i[1][0][0])
            
    
            
#     return answer

# # {"classic" : [[0, 500], [2, 150], [3, 800]]}




def solution(genres, plays):
    answer = []
    genres_dict = {}
    for key in range(len(genres)):
        array = []
        if genres[key] not in genres_dict:
            genres_dict[genres[key]] = []
        array.append(key)
        array.append(plays[key])
        genres_dict[genres[key]].append(array)
    for key in genres_dict:
        genres_dict[key].sort(key = lambda x:x[1],reverse = True)
    a = sorted(
        genres_dict.items(), 
        key = lambda x: sum(i[1] for i in x[1]),
        reverse = True
    )
    print(genres_dict)
    print(a)
    for key in a:
        
        if len(key[1]) >=2:
            answer.append(key[1][0][0])
            answer.append(key[1][1][0])
        else:
            answer.append(key[1][0][0])
        
    return answer