from bs4 import BeautifulSoup

html_doc = """
<p class="price_color"> £51.77 </p>
<h1> 상품 상세 정보 <br> 새로운 기능! </h1>
"""

soup = BeautifulSoup(html_doc,'html.parser')

# 가격 추출 및 정제
price_tag = soup.find('p',class_='price_color')

# 전달 받은 문자열 앞뒤 공백 제거
price_text = price_tag.get_text(strip=True) #str 함수 적용하기 위해 .text 아닌 get_text함수 사용 


#문자열 사이에 숫자가 아닌 문자가 같이 있을 때 데이터 정제
clean_price = float(price_text.replace('£',''))
print(clean_price)

# 제목 텍스트 추출 및 정제
# .text를 사용할 경우는 자식태그의 텍스트를 포함 (현재 텍스트 사이 줄바꿈<br>태그 존재)
title_raw = soup.find('h1').text
# get_text(strip)을 사용
title_clean = soup.find('h1').get_text('',strip=True)
print(title_clean)