# 속성값 추출하기 

from bs4 import BeautifulSoup

html_doc = """
<div id="product-123" class="item featured" data-
stock="10">

<a href="/detail/book-title-1">Book Title</a>
<img src="/images/book1.jpg" alt="Book Cover">
</div>
"""

soup = BeautifulSoup(html_doc,'html.parser')
product_div = soup.find('div')
link = soup.find('a')['href'] #
link2 = soup.a['href'] # 둘은 같은 결괏값 반환
image = soup.find('img')

# 딕셔너리처럼 접근
product_id = product_div['id']
item_classes = product_div['class']

# .get()으로 안전하게 접근 (없는 속성은 None 반환) -> 에러 없이 안전
stock = product_div.get('data-stock') #'10'
missing_attr = product_div.get('data-price','N/A')  # "N/A"
img_alt = image.get('alt')

