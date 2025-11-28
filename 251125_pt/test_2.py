# 파일 입출력
## 수동 닫기
# file = open("example.txt", "w") # 파일 열기
# file.write("Hello, Python!") # 파일에 쓰기
# file.close() # 파일 닫기
# with open("example.txt", "w") as file:
#     file.write("My name is ?")
# 파일 자동 닫힘
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example2.txt", "w", encoding="utf-8") as file:
#     file.write("안녕하세요. 최흥기 입니다.")

# lines = ["첫 번째 줄\n", '두 번째 줄\n', '세 번째 줄\n']

# with open('testlist.txt', 'w', encoding="utf-8") as file:
#     file.writelines(lines)

# with open('user_input2.txt', 'w', encoding='utf-8') as file:
#     while True:
#         line = input("파일에 저장할 내용을 입력하세요: ")
#         if line == '종료':
#             print("파일 내용 입력을 종료합니다.")
#             break
#         file.write(line)
# print('사용자 입력 내용이 저장되었습니다.')

# with open('user_input.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for idx, line in enumerate(lines):
#         print(f'{idx + 1}번째 줄: {line.strip()
# 
# }')

# with open('nami.png', 'rb') as file:
#     header = file.read(10)
#     print(f'{header}')

# def identifiy_file(file_path):
#     with open(file_path, 'rb') as file:
#         header = file.read(4)
#         print(header)
#         if header == b'\x89PNG': #PNG
#             return "PNG"
#         elif header[:2] == b'\xff\xd8': #JPEG
#             return "JPEG"
#         else:
#             return "Unknown format"
    
# print(identifiy_file('nami.png'))

with open('nami.png', 'rb') as source_file:
    data = source_file.read()

with open('copy_nami.png', 'wb') as test_file:
    test_file.write(data)


