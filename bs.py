import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
res = requests.get(url)

# 문자열 형태로 응답받은 text를 html 태그에 맞게 변환 
soup = BeautifulSoup(res.text,'html.parser')  #res.text 태그 코드 뭉치
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p',class_='price_color').text #속성이 class인 첫번째 오는 p태그를 찾겠다. p태그 중에서 값만 출력(text)
    data.append({'title':title,'price':price})

print(data[:3])