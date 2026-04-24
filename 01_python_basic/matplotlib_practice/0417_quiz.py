# %%
class Book:
    title = ""
    author = ""
    price = 0

b1 = Book()
b1.title = '파이썬 기초'
b1.author = '홍길동'
b1.price = 25000
print(b1.title, b1.author, b1.price)
# %%
class timer:
    def __init__(self):
        self.count = 0
    
    def tick(self, n):
        self.count += n
        return self.count

t1 = timer()
t2 = timer()
print(t1.tick(5), t1.tick(3), t2.tick(10),t2.tick(2))
# %%
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        print(f'이름: {self.name}, 학점: {self.grade}')

s1 = Student('김민준',4.3)
s1.get_info()


# %%
class Scoreboard:
    total = 0

    def __init__(self,score):
        self.score = score
        Scoreboard.total += score

s1 = Scoreboard(80)
s2 = Scoreboard(90)
s3 = Scoreboard(70)
print(Scoreboard.total, s1.score)

# %%
import numpy as np

a = np.array([3, 6, 9, 12, 15])
print(a[2], a[-1], a[1:4])

# %%
import numpy as np

z = np.zeros(4)
o = np.ones(3)
r = np.arange(2,10,2)

print(z)
print(o)
print(r)

# %%
import numpy as np
a = np.arange(1,7)
b = a.reshape(2,3)
print(b,b.shape)

# %%
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_info(self):
        return print(f'상품명:{self.name}, 정가: {self.price}원')
    def get_sale_price(self, rate):
        self.rate = rate
        return self.price * (1-rate/100)

p1 = Product('노트북',1500000)
p1.get_info()
print(p1.get_sale_price(10))

# %%
import numpy as np

mat = np.arange(1,10).reshape(3,3)
print(mat)
print(mat[1,2])
print(mat+10)

# %%
import numpy as np

class ScoreManager:
    def __init__(self,scores):
        self.scores = scores
        self.data = np.array(self.scores)
    def get_total(self):
        return np.sum(self.data)
    def get_average(self):
        return self.get_total() / len(self.data)
    def get_above(self,cutoff):
        return [i for i in self.scores if i > cutoff]

scores = [72, 88, 95, 61, 84, 77]
s1 = ScoreManager(scores)
print(f"합계: {s1.get_total()}")
print(f"평균: {s1.get_average()}")
print(f"80점 초과: {s1.get_above(80)}")