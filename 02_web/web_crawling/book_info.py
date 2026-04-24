# 책 제목과 별점 크롤링하기 실습

import requests
from bs4 import BeautifulSoup

#1. 요청 및 응답
url = 'https://books.toscrape.com'
res = requests.get(url)

#1-1. status_code로 200(정상)인지 확인
if res.status_code == 200:
    print('정상')

#2. find_all()로 모든 article 먼저 수집 (책 정보 가져오기)
soup = BeautifulSoup(res.text,'html.parser')
books = soup.find_all('article',class_='product_pod')


#3. 별점을 숫자 형태로 변환하기 위한 dict 준비
rating_dict = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
    }

#4. 책 정보에서 책 제목과 별점만 추출하기
book_info = []
for book in books:
    title = book.h3.a['title']                      # 제목 추출
    rate = book.find('p',class_='star-rating')      # 별점 추출 : star-rating One 의 형태
    rate_text = rate['class'][-1]                   # 별점 클래스에서 별점 정보만 가져오기 'One'
    rating = rating_dict.get(rate_text,0)           # 별점 텍스트 -> 수치로 가져오기 '1'

    book_info.append({'title':title,'rating':rating})  # 책제목과 별점 딕셔너리로 리스트에 저장

print(book_info)
