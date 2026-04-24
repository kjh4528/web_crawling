# %%
# 파일 생성하기
f = open("새파일.txt",'w') #쓰기 모드
f.close() #open과 한쌍

# %%
# 생성한 파일에 출력값 입력하기
f = open("새파일.txt",'w')
for i in range(1,10):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close() #작성 완료 후 닫기 
# %%
# 파일의 한 줄 문자열로 반환
f = open('새파일.txt','r') #읽기 모드로 열기
line = f.readline()
print(line)
f.close()

# %%
# 파일 내용 전체 문자열로 가져와 리스트로 반환
f = open('새파일.txt','r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# %%
# 내용 전체 문자열로 리턴 
f = open('새파일.txt','r')
data = f.read()
print(data)
f.close()
# %%
# 기존 파일에 새로운 내용 추가하기 
# 기존 파일을 'w'모드로 열면 기존 내용 모두 사라짐
# 새로운 값만 추가할 경우 'a'모드 사용
f = open("새파일.txt",'a')
for i in range(11,20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()
# %%
# 기존 방식
f = open('foo.txt','w')
f.write('life is too short, you need python')
f.close()
# with문 
# with문을 이용하면 자동으로 close()
with open('foo.txt','w') as f:
    f.write('life is too short, you need python')
