#coding:utf-8

import requests # requests라이브러리를 불러오기 위한 과정
from bs4 import BeautifulSoup # bs4 라이브러리에서 특정함수인 BeautifulSoup를 불러오기 위한 과정


def make_url(page_num): # 함수 설명 : 1번부터 page_num까지 원하는 순서까지의 번호를 받아서 해당되는 url를 만들고 그 리스트를 리턴하는 함수
	url_list = [] # 빈 리스트 생성.
	
	for page in range(1,page_num+1): # 함수인자로 받은 page_num의 수까지 url을 만들기 위해 반복하는 과정
		url = "http://www.ted.com/talks?page={}".format(page)
		url_list.append(url)

	return url_list # 만들어진 url_list 값을 리턴해주는 과정




def fetch_html(url): # 함수설명 : 함수인자로 받은 url을 대상으로 requests를 보내고 해당 결과의 html 코드를 반환하는 함수.

	req = requests.get(url) # url을 통해 requests를 보내고 그 결과를 req 변수에 저장.
	html = req.text # 저장된 req 변수의 결과값의 html 코드를 가져오는 과정.


	return html # html 코드를 리턴해주는 과정.



def parsing_html(html): # 함수설명 : 함수인자로 받은 html 변수를 bs로 분석하고 , 원하는 텍스트 값을 가져오는 함수.
	soup = BeautifulSoup(html,'html.parser') # html 변수를 BeautifulSoup로 분석하기위해 함수에 넣어주는 과정.
	frame = soup.find('div' , {'class' : 'row row-sm-4up row-lg-6up row-skinny'}) # 분석을 하기위한 프레임을 만들어주는 과정
	cols = frame.find_all('div', {'class': 'media__message'})
	speakers = [] # 강연자를 저장하기 위한 리스트를 만드는 과정.
	titles = [] # 강연 제목을 저장하기 위한 리스트를 만드는 과정.
	dates = [] # 강연 날짜를 저장하기 위한 리스트를 만드는 과정. 	
	for col in cols:
		speaker = col.find('h4', {'class':'h12 talk-link__speaker'}).get_text() #강연자를 html에서 가져오는 과정.
		title = col.find('h4', {'class':'h9 m5'}).get_text() #강연 제목을 html에서 가져오는 과정.
		date = col.find('span', {'class':'meta__val'}).get_text()
		speakers.append(speaker) # 강연자를 강연자 리스트에 저장하는 과정.
		titles.append(title) # 강연제목을 강연 제목 리스트에 저장하는 과정.
		dates.append(date) # 강연날짜를 강연 날짜 리스트에 저장하는 과정.
		print speakers
		print titles
		print dates

def main(): # 함수설명 : 지금까지 만든 3개의 함수를 합체하는 함수. 결과적으로 main함수만 실행해주게 되면 main함수에 정의된 순서대로 코드 진행.
	urls = make_url(10) # 1번부터 10번까지의 url을 만들고 그 리턴값을 urls에 저장.
	for url in urls: # 반복문을 통해 urls에 저장된 url을 하나씩 url 변수에 저장하는 과정.
		html = fetch_html(url)# url을 통해 가져온 html 리턴 값을 html 변수에 저장해주는 과정. 
		parsing_html(html) # html에 변수에 저장된 값을 함수인자로 사용해서 BeautifulSoup을 통해 원하는 자료를 가져오는 과정.


main() #전체 메인함수를 실행시키는 과정.

