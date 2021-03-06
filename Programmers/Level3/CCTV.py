def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda route: route[1])
    prev_camera = -30000

    for route in routes:
        if prev_camera < route[0]:
            answer += 1
            prev_camera = route[1]

    return answer

routes = [[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
