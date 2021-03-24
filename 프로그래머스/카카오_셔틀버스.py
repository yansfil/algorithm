"""
https://programmers.co.kr/learn/courses/30/lessons/17678
부분의 문제만 풀려고 하기 보단 전체적으로 문제를 조립하는 연습을 하라.
시간이 지나면서 순차적으로 동작해야하는 문제 유형을 잘 정리해보기
보통 while, for 루프문을 통해서 한 루프가 끝날 때 시간을 더하고 그 내부에서 처리를 하는 방식이다.
"""

def parseTime(time):
    time = int(time)
    return (str(time // 60) if time //60 >= 10 else "0"+str(time//60)) + ":" + (str(time % 60) if time % 60 >= 10 else "0" + str(time % 60))


def solution(n, t, m, timetable):
    timeQueue = [
        int(time[:2]) * 60 + int(time[3:]) for time in timetable
    ]
    timeQueue.sort()

    startTime = 540
    while n > 1:
        available = m
        while available and startTime >= timeQueue[0]:
            timeQueue.pop(0)
            available -= 1
        startTime += t
        n -= 1
    available = m
    for time in timeQueue:
        if time > startTime:
            return parseTime(startTime)
        available -= 1
        if available == 0:
            return parseTime(time - 1)
    print(startTime)
    return parseTime(startTime)

print(solution(2,1,2,	["09:00", "09:00", "09:00", "09:00"]))



### 파이썬 알고리즘 북 풀이
def solution(n, t, m, timetable):
    timeQueue = [
        int(time[:2]) * 60 + int(time[3:]) for time in timetable
    ]
    timeQueue.sort()
    startTime = 540
    current = startTime
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= startTime:
                current = timetable.pop(0) -1
            else :
                current = startTime
        startTime += t
    h,m = divmod(current,60)
    return str(h).zfill(2) + str(m).zfill(2)

