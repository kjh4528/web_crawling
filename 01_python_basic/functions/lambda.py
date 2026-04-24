
# %%
f = lambda *x:max(x)*2
f(1,2,3)
# %%
# 일반 함수와 lambda 함수 비교
def sub(a,b):
    return a-b
result = sub(200,100)
print('200-100 =',result)
# %%
f = lambda a,b : a-b
print('200-100 =',f(200,100))
