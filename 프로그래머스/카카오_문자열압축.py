"""
https://programmers.co.kr/learn/courses/30/lessons/60057
크기에 맞춰서 문자열을 자르고 list에 넣는다
나눠진 list를 순회하면서 연속되는 값이 있을 때 처리를 해서 길이를 구한다.
"""

# BEFORE
def solution_bad(s):
        min_value = float('inf')
        for rg in range(1, (len(s) // 2) + 1):
            i = 0
            chunks, chunk_size = len(s), rg
            arr = [ s[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
            print(arr)
            cnt = 1
            string = ""
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    if cnt > 1 :
                        string += str(cnt) + arr[i]
                    else :
                        string += arr[i]
                elif arr[i] == arr[i+1]:
                    cnt += 1
                else:
                    if cnt > 1:
                        string += str(cnt) + arr[i]
                        cnt = 1
                    else:
                        string += arr[i]
            print(string)
            min_value = min(min_value, len(string))
        return min_value

# AFTER
def solution(s):
    min_value = float('inf')
    for rg in range(1, (len(s) // 2) + 1):
        chunks, chunk_size = len(s), rg
        arr = [s[i:i + chunk_size] for i in range(0, chunks, chunk_size)] #길이 단위로 문자 자르는 방법이 이렇게 쉬웠음 (이런 정형적인 방식은 구글링 빠르게 하는 게 좋을듯)
        prev_v = ""
        cnt = 1
        result = []
        for a in (arr + [""]): #마지막 처리가 애매할 때는 이렇게 뒤에 값을 붙여주자
            if prev_v == a:
                cnt += 1
            else:
                result.append([prev_v, cnt])
                prev_v = a
                cnt = 1
        min_value = min(min_value, sum(len(v) + (len(str(ct)) if ct > 1 else 0) for v, ct in result))
    return min_value


# Good Solution
# 이전 값을 비교할 때 zip을 사용하면 더 효과적으로 비교가 가능함..
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

