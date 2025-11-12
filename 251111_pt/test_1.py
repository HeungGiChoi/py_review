# def solution(n):
#     answer = sorted([i for i in range(1, n + 1) if i % 2 == 1])
#     return answer

# a = solution(10)
# print(a)

def solution(price):
    if price >= 500000:
        return int(price - (price * 0.2))
    elif price >= 300000:
        return int(price - (price * 0.1))
    elif price >= 100000:
        return int(price - (price * 0.05))
    
print(solution(150000))
print(solution(580000))
print(solution(999990))