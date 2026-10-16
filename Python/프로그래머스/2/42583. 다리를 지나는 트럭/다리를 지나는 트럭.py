def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0
    bridge_truck = [0] * bridge_length 
    over_truck = []
    i = 0

    while len(over_truck) < len(truck_weights):        
        if i < len(truck_weights):
            if bridge_truck[-1] != 0:
                bridge_weight -= bridge_truck[-1]
            bridge_weight += truck_weights[i]
            if bridge_weight <= weight:
                bridge_truck.insert(0, truck_weights[i])
                i += 1
        if bridge_weight > weight:
            bridge_truck.insert(0,0)
            bridge_weight -= truck_weights[i]
        if bridge_truck[-1] != 0:
            over_truck.insert(0, bridge_truck.pop())
        else:
            bridge_truck.pop()
        answer += 1
    return answer
# bridge_weight 매번 리뉴얼
# 나가는 거는 stack.pop() 그리고 만약에 weight 이상이면 0으로, 이하면 들어오게
