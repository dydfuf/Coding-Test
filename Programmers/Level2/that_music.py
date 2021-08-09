import math

def timeDiff(start, end):
    startHour, startMin = map(int, start.split(":"))
    endHour, endMin = map(int , end.split(":"))

    totalStartMin = startHour * 60 + startMin
    totalEndMin = endHour * 60 + endMin
    result = int(totalEndMin) - int(totalStartMin)

    return result


def solution(m, musicinfos):
    answer = None
    m = m.replace("C#","c").replace("D#","d").replace("F#", "f").replace("G#", "g").replace("A#","a")
    for aMusicinfos in musicinfos:
        start, end, title, melody = aMusicinfos.split(",")
        melody = melody.replace("C#","c").replace("D#","d").replace("F#", "f").replace("G#", "g").replace("A#","a")

        diff = timeDiff(start, end)
        melody *= math.ceil(diff/len(melody))
        melody = melody[:diff]

        if m not in melody:
            continue

        if answer == None or answer[0] < diff or (answer[0] == diff and answer[1] > start):
            answer = [diff, start, title]

    if answer:
        return answer[-1]
    return "(None)"

if __name__ == '__main__':
    arr_m = ["ABCDEFG", "CC#BCC#BCC#BCC#B"	, "ABC"	]
    arr_musicinfos = [["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	, ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	, ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	]
    for m, musicinfos in zip(arr_m, arr_musicinfos):
        print(solution(m, musicinfos))