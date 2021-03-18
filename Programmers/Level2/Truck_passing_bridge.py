def solution(bridge_length, weight, truck_weights):
    time = 0
    arrived_truck = []
    passing_truck = []
    passing_time = []
    num_of_truck = len(truck_weights)

    while len(arrived_truck) != num_of_truck:
        if len(passing_time) != 0 and passing_time[0] == 0:
            passing_time.pop(0)
            arrived_truck.append(passing_truck.pop(0))

        if len(passing_truck) == 0:
            if len(truck_weights) == 0:
                break
            passing_truck.append(truck_weights.pop(0))
            passing_time.append(bridge_length)
        elif len(truck_weights) != 0 and sum(passing_truck) + truck_weights[0] <= weight:
            passing_truck.append(truck_weights.pop(0))
            passing_time.append(bridge_length)

        time += 1

        for i in range(len(passing_time)):
            passing_time[i] -= 1

    return time+1


if __name__ == "__main__":
    arr_bridge_length = [2, 100, 100]
    arr_weight = [10, 100, 100]
    arr_truck_weights = [[7, 4, 5, 6], [10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
    for bridge_length, weight, truck_weights in zip(arr_bridge_length, arr_weight, arr_truck_weights):
        print(solution(bridge_length, weight, truck_weights))
