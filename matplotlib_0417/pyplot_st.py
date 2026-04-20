import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
# 2차원 평면에 라인 차트 그리기
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('y label')
plt.xlabel('x label')
plt.show()
# %%
# 2차 함수 그리기
import numpy as np
x = np.arange(10)
plt.plot(x**2)
plt.show()
# plt.axis([0,100,0,100]) # 축 범위 지정
# %%
# 한 화면에 여러 그래프 그리기
x = np.arange(-20,20)
y1 = 2*x
y2 = (1/3)*x**2+5
y3 = -x**2-5
plt.plot(x,y1,'g--',x,y2,'r^-',x,y3,'b*:') #색상,도형,선 옵션
plt.axis([-30,30,-30,30])
plt.show()
# %%
x = np.linspace(0, np.pi*2,100)
plt.plot(x,np.sin(x),'r-')
plt.plot(x,np.cos(x),'b:')
plt.show()
# %%
# 이미지 저장
# plt.figure()로 생성 -> .savefig() 저장
x = np.linspace(0, np.pi*2,100)
fig = plt.figure()
plt.plot(x,np.sin(x),'r-')
plt.plot(x,np.cos(x),'b:')
fig.savefig('sin_cos_fig.png')
# %%
# 이미지 불러오기 
from IPython.display import Image
Image('sin_cos_fig.png')
# %%
# 스타일 설정
x = np.linspace(0, np.pi*2,100)
plt.plot(x,np.sin(x),'r-')
plt.plot(x,np.cos(x),'b:')
plt.title('Sin cos curve')
plt.xlabel('x value')
plt.ylabel('y value')
plt.legend(loc='upper right')
plt.show()
# %%
# 테마(스타일시트)설정 
# plt.style.use('seaborn-whitegrid')
# 사용 가능한 스타일시트 목록 보기
print(plt.style.available)
# %%
# 어노테이션(화살표 그려서 문자 출력)
# annotate(나타낼 문자열,화살표가 가리키는 점의 좌표,문자열이 출력될 위치,화살표 속성)

x = np.arange(1,10)
y = x*5

plt.plot(x,y)
plt.annotate('annotate',xy=(2,10),xytext=(5,20),arrowprops={'color':'green'})
plt.show()
# %%
# 한 화면에 다양한 그래프 그리기
# subplots(), figure 객체, axes 객체
# figure : 축,그래픽,텍스트 등 그리기 객체 포함하는 컨테이너
# axes : 그림 그릴 수 있는 공간(테두리 상자 모양)
# axes는 다차원 배열로 [0,0]과 같은 인덱스를 이용하여 특정 axes객체에 그리기 가능
# subplots(행의 수,열의 수) 로 fig,ax 반환
fig,ax = plt.subplots(2,2) # 2행,2열 총 4개의 그림 공간


# 첫 번째 공간[0,0]에 산점도 그리기
x = np.random.randn(100)
y = np.random.randn(100)
ax[0,0].scatter(x,y)

# [0,1]에 막대 차트 그리기
x = np.arange(10)
y = np.random.uniform(1,10,10)
ax[0,1].bar(x,y)

# [1,0]에 라인 차트 그리기
x = np.linspace(0,10,100)
y = np.cos(x)
ax[1,0].plot(x,y)

# [1,1]에 2D 이미지 그리기
z = np.random.uniform(0,1,(5,5))
ax[1,1].imshow(z)


# %%
# 0420 이어서 수업 
# 다양한 차트 그리기

# scatter() 산점도 
x = np.random.rand(30)
y = np.random.rand(30)
area = (30*np.random.rand(30))**2  # 점의 면적
colors = np.random.rand(30)  # 점의 색상
plt.scatter(x,y,s=area,c=colors,alpha=0.5)  # alpha: 투명도 
# %%
# bar() 막대차트
x = np.arange(3)
years = ['2010','2011','2012']
domestic = [6801,7695,8010]
foreign = [777,1046,1681]
plt.bar(x,domestic) # width = o.25 막대 너비 조정(원래 크기의 25%)
plt.bar(x,foreign)
plt.xticks(x,years)
# %%
# barh() 수평막대차트 
plt.barh(x,domestic,height=0.25)
plt.barh(x+0.3,foreign,height=0.25) # x+0.3 두 막대 겹치지 않게 조정 
plt.yticks(x,years)
# %%
# hist() 히스토그램
f1 = np.random.normal(loc=0,scale=1,size=10000)
plt.hist(f1,bins=200,color='red',alpha=0.5)
# %%
# pie() 파이차트
data = [5,4,6,11]
clist = ['cyan','gray','orange','red']
plt.pie(data,autopct='%.2f',colors=clist)
# %%
# 히트맵
data = np.random.random((10,10))
plt.imshow(data)
plt.colorbar()
# %%
# boxplot() 상자 수염
rand_data = np.random.randn(100)
plt.boxplot(rand_data)
