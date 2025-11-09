# 함수
# def sum_mul(num1, num2):
#     if num1 == num2:
#         return num1 * num2
#     elif num1 != num2:
#         return num1 + num2
    
# result = sum_mul(2, 2)
# # print(result)
# result = sum_mul(2, 3)
# print(result)

# 예제 1.
def coopang(product):
    if product < 20000:
        return product + 2500
    else:
        return product

product_1 = coopang(30000)
product_2 = coopang(17500)
print(f'product_1: {product_1}')
print(f'product_2: {product_2}')