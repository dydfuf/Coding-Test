import score

if __name__ == "__main__":
    ban = list()
    student = list()
    for _ in range(5):
        name = input("성명 : ")
        kor = int(input("국어점수 : "))
        eng = int(input("영어점수 : "))
        mat = int(input("수학점수 : "))

        student.append(name)
        student.append(kor)
        student.append(eng)
        student.append(mat)

        total = score.total(student)
        average = score.ave(student)
        grade = score.grade(student)

        student.append(total)
        student.append(average)
        student.append(grade)

        ban.append(student.copy())
        student.clear()

    for student in ban:
        score.output(student)

    print("\n2명 성적 비교하여 더 좋은 점수의 학생 찾기")
    score.output(ban[2])
    score.output(ban[4])
    print("성적이 더 좋은 학생")
    score.output(score.max_student(ban[2], ban[4]))

    print("\n3명 성적 비교하여 더 좋은 점수의 학생 찾기")
    score.output(ban[1])
    score.output(ban[2])
    score.output(ban[3])
    print("성적이 더 좋은 학생")
    score.output(score.max_student(ban[1], ban[2], ban[3]))