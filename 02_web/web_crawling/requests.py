#웹에 요청 보내고 응답받기 
import requests

url = 'https://books.toscrape.com/dmcconet'
res = requests.get(url)

# 응답 상태 확인
if res.status_code == 200:
    print('요청 성공')
elif res.status_code == 404:
    print('페이지를 찾을 수 없습니다')
