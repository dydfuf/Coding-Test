def solution(table, languages, preference):
    langDict = {}

    for aTable in table:
        split = aTable.split(" ")
        langDict[split[0]] = split[1:]

    lang = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]

    lang.sort()

    answer = ["",0]
    for l in lang:
        temp = 0
        for aLang, aPrefer in zip(languages, preference):
            if aLang in langDict[l]:
                idx = 5 - langDict[l].index(aLang)
            else:
                idx = 0
            temp += idx * aPrefer
        if temp > answer[1]:
            answer[0] = l
            answer[1] = temp

    return answer[0]

if __name__ == '__main__':
    arr_table = [["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]]
    arr_lang = [["PYTHON", "C++", "SQL"], ["JAVA", "JAVASCRIPT"]]
    arr_prefer = [[7, 5, 5], [7, 5]	]
    arr_result = ["HARDWARE", "PORTAL"]
    for table, language, preference, result in zip(arr_table, arr_lang, arr_prefer, arr_result):
        print(solution(table, language, preference), result)