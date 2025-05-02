from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (초기에는 0으로 채움)
    total_weight = 0  # 현재 다리 위 트럭의 총 무게
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1
        left = bridge.popleft()
        total_weight -= left

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 트럭을 못 올리면 빈 공간
    return time
