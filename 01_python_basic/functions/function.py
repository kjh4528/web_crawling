# 기타 함수


# %%
# filter(함수, 범위) 
# 참(True) 결과 반환
f = lambda x: x>0
print(list(filter(f,range(-5,5))))

def func(x):
    if x > 0:
        return x
    else:
        return x - 100

print(list(filter(func,range(-5,5))))
# 반환값이 0이 아니면 모두 참으로 간주해 범위 그대로 반환


# %%
# 짝수 리스트 만들기 
a = list(range(1,11))
even_list = list(filter(lambda x:x%2==0,a))
even_list


# %%
# map(적용할 함수, 반복가능 객체)
def square(x):
    return x**2
square_a = list(map(square,a))
print(square_a)


# %%
#reduce()
from functools import reduce

b = [1,2,3,4]
n = reduce(lambda x,y: x+y,b)
print(n)

x = reduce(lambda x,y: x*y,b)
print(x)  # 4! 의 결과와 동일

