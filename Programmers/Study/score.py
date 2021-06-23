def total(student):
    return student[1] + student[2] + student[3]


def ave(student):
    return (student[1] + student[2] + student[3]) / 3


def grade(student):
    average = ave(student)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def output(student):
    print(student[0], " : 국어 : ", student[1], " : 영어 : ", student[2], " : 수학 : ", student[3],
          " : 총점 : ", student[4], " : 평균 : ", student[5], " : 학점 : ", student[6])


def max_student(*args):
    students = args
    if len(students) == 2:
        if students[0][4] > students[1][4]:
            return students[0]
        else:
            return students[1]
    else:
        a = students[0][4]
        b = students[1][4]
        c = students[2][4]
        if (a >= b) and (a >= c):
            return students[0]
        elif (b >= a) and (b >= c):
            return students[1]
        else:
            return students[2]


