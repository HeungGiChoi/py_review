import requests

## 외부 api에서 데이터 가져옴
url = "https://koreanjson.com/posts"
response = requests.get(url)

# 응답 처리
if response.status_code == 200: # status_code : 응답 상태. 200이면 정상 응답.
    data = response.json()
    print("API 데이터: ", data)
else:
    print("API 요청 실패: ", response.status_code)