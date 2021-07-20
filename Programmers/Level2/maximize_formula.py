def calc(op, left, right):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right


def solution(expression):
    result = []
    ori_atoms = []

    idx = 0

    # 수식을 연산자와 피연산자로 나누기
    # 100 + 200
    for i in range(len(expression)):
        if expression[i] == "+" or expression[i] == "-" or expression[i] == "*":
            ori_atoms.append(expression[idx:i])
            ori_atoms.append(expression[i])
            idx = i + 1
        # elif expression[i] == "-":
        #     ori_atoms.append(expression[idx:i])
        #     ori_atoms.append(expression[i])
        #     idx = i + 1
        # elif expression[i] == "*":
        #     ori_atoms.append(expression[idx:i])
        #     ori_atoms.append(expression[i])
        #     idx = i + 1
    ori_atoms.append(expression[idx:])
    print(ori_atoms)

    # 가능한 6가지 조합
    pri = [
        ["*", "+", "-"],
        ["*", "-", "+"],
        ["+", "*", "-"],
        ["+", "-", "*"],
        ["-", "+", "*"],
        ["-", "+", "*"]
    ]
    '''
    조합 만들
    from itertools import permutations
    pr = ['+','-','*']
    pm = list(map(''.join, permutations(pr)))
    '''
    for pr in pri:
        temp = []
        atoms = ori_atoms
        for a in pr:
            if a in atoms:
                i = 0
                while i < len(atoms):
                    if i == len(atoms) - 1:
                        temp.append(atoms[i])
                        break
                    if atoms[i] == a:
                        temp_pop = temp.pop()
                        if a == "*":
                            temp.append(temp_pop * int(atoms[i + 1]))
                        elif a == "+":
                            temp.append(temp_pop + int(atoms[i + 1]))
                        elif a == "-":
                            temp.append(temp_pop - int(atoms[i + 1]))

                        # temp.append(calc(a, temp_pop, int(atoms[i + 1])))

                        i += 2

                    elif atoms[i + 1] == a:
                        if a == "*":
                            temp.append(int(atoms[i]) * int(atoms[i + 2]))
                        elif a == "+":
                            temp.append(int(atoms[i]) + int(atoms[i + 2]))
                        elif a == "-":
                            temp.append(int(atoms[i]) - int(atoms[i + 2]))

                        # temp.append(calc(a, int(atoms[i], int(atoms[i + 2])))

                        i += 3
                    else:
                        temp.append(atoms[i])
                        i += 1
            else:
                temp = atoms
            atoms = temp
            if not a == pr[-1]:
                temp = []

        # 최댓값 비교
        if not result:
            result.append(abs(temp.pop()))
        else:
            if result[0] < abs(temp[0]):
                result.pop()
                result.append(abs(temp[0]))
        print(result)

    return result[0]


if __name__ == "__main__":
    arr_expression = [
        "200-300-500-600*40+500+500"
    ]
    for expression in arr_expression:
        print(solution(expression))
