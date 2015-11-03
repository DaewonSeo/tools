# -*- encoding: euc-kr -*-
import requests
from bs4 import BeautifulSoup
import time





def fetch_the_page(url):
		
	req = requests.get(url)
	html = req.text
	soup = BeautifulSoup(html,'lxml')
	profile = soup.find('div',{'class':'lmbox2'}).find('div',{'class':'rel_info'})
	name = profile.find('strong').find('span',{'class':'kr'}).text
	district = profile.find('ul').find_all('li')[1].text
	
	print name.encode('euc-kr','replace')
	print district.encode('euc-kr','replace')	
	
	try: 
		tables = soup.find_all('div',{'class':'table_t1'})[2]
		tbody = tables.find('tbody')
		for t in tbody.find_all('tr'):
			property_type = t.find_all('td')[0].text
			print property_type.encode('euc-kr','replace')
			
			site = t.find_all('td')[1].text
			print site.encode('euc-kr','replace')
			
			
		time.sleep(30)
	except IndexError:
		time.sleep(10)
		pass


url = "http://the300.mt.co.kr/db/yeuido300/yeuido300View.html?code=2014041517295569540PEO&srcParty=&g_party2=&g_cntgubun=&g_howto=&city=&district=&keyword=&page=19"
fetch_the_page(url)
