url = 'http://naver.com'
#규칙1
nurl = url.replace('http://','')
#규칙2
nurl = nurl.split('.')[0]
print(nurl)
#규칙3
pw = nurl[:3] + str(len(nurl)) + str(nurl.count('e')) + '!'
print(f'{url}의 비밀번호는 {pw} 입니다.')