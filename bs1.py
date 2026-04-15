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
link = soup.find('a')['href']
link2 = soup.a['href']

image = soup.find('img')

product_id = product_div['id']
item_classes = product_div['class']

stock = product_div.get('data-stock') # get함수 쓰면 값이 없을 때 none 출력, 에러안뜨고 안전 

missing_attr = product_div.get('data-price','N/A')
img_alt = image.get('alt')

