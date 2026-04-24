# %%
# lambda 사용
calc = lambda a,b:a*b

print(calc(6,8))
print(calc(3, 7))

# %%
# lambda와 filter 사용
scores = [85, 42, 91, 67, 55, 78]
print(list(filter(lambda x : x > 70,scores)))

# %%
# map과 lambda 사용 
nums = [2, 3, 4, 5]
num_list = list(map(lambda x:x*3,nums))
print(num_list)

# %%
# 리스트 컴프리헨션
print([i*2 for i in range(1,6)])

# %%
# format()
product = "노트북"
price = 1200000
qty = 2

print('상품: {}, 가격: {}원, 수량: {}개'.format(product,price,qty))

# %%
# input() 여러 값 공백으로 구분하여 입력받기 
a, b = map(int,input('입력:').split())
print('합:',a+b)
print('곱:',a*b)

# %%
# math함수 
import math

math.sqrt(144)
math.pow(2,10)

# %%
# if문과 for문 사용 리스트 컴프리헨션
print([i**2 for i in range(1,21) if i % 3 == 0])


# %%
# format()
product,price = input().split()
price = int(price)
discount = price-(price*0.1)

print('상품명: {}'.format(product))
print('정가: {:,}'.format(price))
print('할인가(10%): {:.2f}'.format(discount))

# %%
# 배운 내용 모두 활용한 문제 
import math
from functools import reduce

data = list(map(int,input().split()))
evens = [i for i in data if i % 2 ==0]
total = reduce(lambda x,y:x+y,evens)
a = math.sqrt(total)

print('짝수 목록:',evens)
print('합계:',total)
print('제곱근: {:.3f}'.format(a))
