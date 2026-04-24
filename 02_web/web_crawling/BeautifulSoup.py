import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
res = requests.get(url)

# text로 가져온 문자열 html로 변환 
soup = BeautifulSoup(res.text,'html.parser')  #res.text 태그 코드 뭉치
# 책 목록을 모두 가져오기 위해 find_all로 일치하는 태그 모두 찾기
books = soup.find_all('article', class_='product_pod') 

# 책 제목과 가격만 추출하기 
data = []
for book in books:
    title = book.h3.a['title'] # .으로 자식 태그에 접근하여 속성값 가져오기
    price = book.find('p',class_='price_color').text #속성이 일치하는 첫번째의 태그를 찾기, p태그 중에서 값만 출력(text)
    data.append({'title':title,'price':price}) #딕셔너리 형태로 저장

print(data[:3])
