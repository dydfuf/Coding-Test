from itertools import permutations

def solution(numbers):
    answer = 0
    make = set()

    numbers = list(map(str, numbers))

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            make.add(int("".join(j)))

    make_list = list(make)
    max_num = max(make_list) + 1
    # prime = []
    # for i in range(2, max_num + 1):
    #     prime.append(i)
    #
    # for i in range(2, int(max_num**(1/2))):
    #     if i in prime:
    #         idx = 2
    #         num = i
    #         temp = num * idx
    #         while temp < max_num:
    #             if temp in prime:
    #                 prime.remove(temp)
    #             idx += 1
    #             temp = num * idx
    a = [False, False] + [True]*(max_num-1)
    primes = []

    for i in range(2, max_num+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, max_num+1, i):
                a[j] = False

    for m in make_list:
        if m in primes:
            answer += 1

    # for m in make_list:
    #     if m in prime:
    #         answer += 1
    return answer


if __name__ == "__main__":
    arr_numbers = ["17", "011"]
    for numbers in arr_numbers:
        print(solution(numbers))
