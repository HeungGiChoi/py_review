import sys, os, json

# print(sys.version)

# print("프로그램 종료.")
# sys.exit(0)
# print("프로그램 종료.")
# print("현재 디렉토리: ", os.getcwd())
# file_path = os.chdir(os.getcwd())
# # dir = os.popen('ls')

# # os.mkdir("test")

# # os.rmdir("test")

# print("PATH 환경 변수:", os.environ.get('PATH'))

data = {
    'a': "홍길동",
    'b': 25,
    'c': "서울"
}

json_str = json.dumps(data)
# json_str = data
print("JSON 문자열:", json_str)

json_obj = json.loads(json_str)
# json_obj = json_str
print("Python 객체: ", json_obj)
print(json_obj['a'])
