import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    length = len(scoville)
    while scoville[0] < K:
        
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        num = num1+2*num2
        heapq.heappush(scoville, num)
        answer+=1
        if scoville[0] < K and answer == length-1:
            return -1
    return answer