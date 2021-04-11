import requests
class NetworkRequest :
    def __init__(self):
        pass
    def get(self):
        res = requests.get("https://www.naver.com",params={ #Query String 형태로 붙음 ?a=b
            "a" : "b"
        })

        res.request  # 내가 보낸 request 객체에 접근 가능
        res.status_code  # 응답 코드
        res.text  # body의 내용물을 text로 반환. encoding타입을 설정하는게 좋음
        res.content  # body를 byte로 변환
        res.raise_for_status()  # 200 OK 코드가 아닌 경우 에러 발동
        res.json()  # json response일 경우 딕셔너리 타입으로 바로 변환
    def post(self):
        res = requests.post("API URL",data={
            "a" : "1",
            "b" : 2
        })
NetworkRequest().get()