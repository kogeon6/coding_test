def solution(n, wires):
    answer = n
    
    for cut in wires:
        
        graph = [[] for _ in range(n+1)]
        
        for a,b in wires:
            if cut == [a,b]:
                continue

            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        stack = [1]
        
        while stack:
            node = stack.pop()
            if node in visited:
                continue
                
            visited.add(node)
            
            for next_node in graph[node]:
                if next_node not in visited:
                    stack.append(next_node)
                    
        count = len(visited)
        difference = abs(count - (n-count))

    # 4. 최솟값 갱신
        answer = min(answer, difference)
    return answer