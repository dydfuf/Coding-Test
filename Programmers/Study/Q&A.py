if __name__ == "__main__":
    questions = (["3+2",5,3],["6/2",3,5],["10-2",8,3,]
                ,["2의 3승",8,4],["5-2*2",1,5])

    reward = 0
    correct = 0
    incorrect = 0

    for question in questions:
        user_input = int(input(question[0] + " : "))
        if user_input == question[1]:
            reward += question[2]
            correct += 1
        else:
            incorrect += 1

    print("정답수 : ", correct)
    print("오답수 : ", incorrect)
    print("점  수 : ", reward)
