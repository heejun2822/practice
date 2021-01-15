import requests
from bs4 import BeautifulSoup


# 1. url
url = 'https://finance.naver.com/sise/'

# 2. url 로 요청을 보낸 후 응답을 받는다.
response = requests.get(url).text
# print(type(response))

# 3. 받은 응답을 예쁘게 꾸며준다.
data = BeautifulSoup(response, 'html.parser')
# print(type(data))
# print(data)

# 4. 꾸민 응답중에서 원하는 데이터를 선택.
result = data.select_one('#KOSPI_now').text
print(result)