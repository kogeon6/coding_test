def solution(today, terms, privacies):
    answer = []
    array = [[] for _ in range(len(privacies))]
    array_terms = [[] for _ in range(len(terms))]
    for i in range(len(privacies)):
        array[i].append(privacies[i][:4])
        if privacies[i][5] == "0":
            array[i].append(privacies[i][6])
        else:
            array[i].append(privacies[i][5:7])
        if privacies[i][8] == "0":
            array[i].append(privacies[i][9])
        else:
            array[i].append(privacies[i][8:10])
        array[i].append(privacies[i][-1])
    for i in range(len(array)):
        for j in range(3):
            array[i][j] = int(array[i][j])
    for i in range(len(terms)):
        array_terms[i].append(terms[i][0])
        array_terms[i].append(int(terms[i][2:]))
    for i in range(len(array_terms)):
        for j in range(len(array)):
            if array_terms[i][0] == array[j][-1]:
                array[j][1] = array_terms[i][1] + array[j][1]
                
                if array[j][2] ==1:
                    array[j][1]-=1
                    array[j][2]=28
                else:
                    array[j][2]-=1
                while array[j][1] > 12:
                    array[j][0] += 1
                    array[j][1] -= 12
    for i in range(len(array)):
        if int(today[:4]) > array[i][0]:
            answer.append(i+1)
            
        if int(today[:4]) == array[i][0]:
            if int(today[5:7]) >array[i][1]:
                answer.append(i+1)
                
        if int(today[:4]) == array[i][0]:
            if int(today[5:7]) == array[i][1]:
                if int(today[8:10]) > array[i][2]:
                    
                    answer.append(i+1)
                    
    print(array_terms)   
    print(array)
    return answer