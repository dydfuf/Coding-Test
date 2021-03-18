import math


def solution(w,h):
    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    answer = math.ceil(h/w)
    gcd = math.gcd(h,w)
    gcd_h = h // gcd
    gcd_w = w // gcd

    for i in range(1, gcd_w):
        answer += math.ceil((gcd_h/gcd_w) * (i+1)) - math.floor((gcd_h/gcd_w) * i)

    answer *= gcd
    return (w*h) - answer


if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w, h))