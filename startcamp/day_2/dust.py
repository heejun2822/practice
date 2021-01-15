import requests
from pprint import pprint

key = '6XZvOmNttWt0i7vXfLXRHpOha18YOS75y8YL4BDdv7KELPmXggXkTlfdMu1Z9GW%2Fee2%2B1D5lIz%2Bsftr%2Fc9P15A%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'

response = requests.get(url).json()
# pprint(response)


# stationname의 미세먼지 농도는 pm10value입니다. 라는 메세지를 출력하시오.
stationname = response['response']['body']['items'][4]['stationName']
pm10value = response['response']['body']['items'][4]['pm10Value']
print(type(response))
print(f'{stationname}의 미세먼지 농도는 {pm10value}입니다.')