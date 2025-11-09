## 각종 문자열 판별
print("123".isdecimal())
print("123.45".isdecimal())
print("123.45".isnumeric())

print("hello".isalpha())
print("hello".isalnum())
print("hello".isspace())
print("안녕".isalpha())

print("안녕123".isalpha())
print("안녕!".isalnum())

print("hello".islower())
print('hello'.isupper())
print('Hello'.islower())
print('HELLO'.isupper())

print("hello world".istitle())
print("Hello world".istitle())
print("Hello World".istitle())
print("안녕하세요".istitle())