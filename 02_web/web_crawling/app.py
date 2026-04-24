# 배운 내용(requests,BeautifulSoup,streamlit) 모두 한 번에 활용해보기
# 데이터 수집해서 데이터프레임으로 저장하고 웹에 df 표시하기

import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

# 데이터 수집(책의 제목, 가격)
url = "http://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    data.append({'title': title, 'price': price})

# 웹에서 df형태로 데이터 띄우기
st.title('책 가격 비교')
keyword = st.text_input('책 제목 검색')

df = pd.DataFrame(data)
if keyword:
    df = df[df['title'].str.contains(keyword,case=False)]

st.dataframe(df)
