import collections
def solution(record):
    id_table = collections.defaultdict(list)
    result = []
    for r in record:
        arr = r.split()
        action = arr[0]
        id = arr[1]
        nickname = arr[2] if len(arr) == 3 else None
        if nickname:
            for idx in id_table[id]:
                result[idx][0] = nickname
        if action == 'Enter':
            result.append([nickname, action])
            id_table[id] += len(result)-1,
        if action == 'Leave':
            nickname = result[id_table[id][-1]][0]
            result.append([nickname, action])
            id_table[id] += len(result) - 1,

    return([f'{nickname}님이 {"들어왔습니다" if action=="Enter" else "나갔습니다"}' for nickname,action in result])




solution(["Enter uid55 Hello", "Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Change uid55 Nope"])