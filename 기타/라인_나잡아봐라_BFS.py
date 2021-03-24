# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
import collections
def go(conny_loc, brown_loc):
    time = 0
    queue = collections.deque([(brown_loc,0)])
    visited = [[] for _ in range(200000)]
    while True :
        conny_loc += time
        if conny_loc > 200000:
            return -1
        if time in visited[conny_loc]:
            return time
        for _ in range(len(queue)):
            cur_position, cur_time = queue.popleft()
            next_position = cur_position - 1
            if 0 <= next_position <= 200000 :
                queue.append((next_position, time+1))
                visited[next_position] += [time+1]
            next_position = cur_position + 1
            if 0 <= next_position <= 200000 :
                queue.append((next_position, time+1))
                visited[next_position] += [time + 1]
            next_position = cur_position * 2
            if 0 <= next_position <= 200000 :
                queue.append((next_position, time+1))
                visited[next_position] += [time + 1]
        time += 1
print(go(11,2))