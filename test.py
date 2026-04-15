import requests

# 요청을 보내고 선언한 변수로 응답을 받음 
res_get = requests.get("https://books.toscrape.com/")
print(f'요청응답상태: {res_get.status_code}')

if res_get.status_code == 200:
    print('요청 성공!')
    print(res_get.text[:100])
