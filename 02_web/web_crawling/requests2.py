import requests

# get 메소드에 바로 경로 입력하고 응답 상태 코드 확인
res_get = requests.get("https://books.toscrape.com/")
print(f'요청 응답 상태: {res_get.status_code}')

# 응답 요청 성공시 내부 텍스트 일부 출력
if res_get.status_code == 200:
    print('요청 성공!')
    print(res_get.text[:100])
