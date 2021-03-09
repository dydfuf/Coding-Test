def dist(num, num2):
    left = [1, 4, 7, -1]
    right = [3, 6, 9, -2]
    center = [2, 5, 8, 0]
    if num in center:
        return abs(center.index(num) - center.index(num2))
    elif num in left:
        return abs(left.index(num) - center.index(num2))+1
    elif num in right:
        return abs(right.index(num) - center.index(num2))+1


def solution(numbers, hand):
    answer = ''
    curr_left = -1
    curr_right = -2
    left = [1, 4, 7]
    right = [3, 6, 9]
    center = [2, 5, 8, 0]
    for num in numbers:
        if num in left:
            curr_left = num
            answer += "L"
        elif num in right:
            curr_right = num
            answer += "R"
        elif num in center:
            dist_l_r = dist(curr_left, num)
            dist_r_l = dist(curr_right, num)

            if dist_l_r == dist_r_l:
                if hand == "right":
                    answer += "R"
                    curr_right = num
                elif hand == "left":
                    answer += "L"
                    curr_left = num
            elif dist_l_r < dist_r_l:
                answer += "L"
                curr_left = num
            elif dist_r_l < dist_l_r:
                answer += "R"
                curr_right = num

    return answer


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers, hand))
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    print(solution(numbers, hand))
