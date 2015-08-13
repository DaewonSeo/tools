#coding:utf-8

from bs4 import BeautifulSoup
import requests
import csv



def make_url():
	citycodes = ['1100', '2600', '2700', '2800', '2900', '3000', '3100', '5100', '4100', '4200', '4300', '4400', '4500', '4600', '4700', '4800', '4900']
	url_list = []
	for citycode in citycodes:
		url = 'http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml?electionId=0020120411&requestURI=%2Felectioninfo%2F0020120411%2Fbi%2Fbigi05.jsp&topMenuId=BI&secondMenuId=BIGI&menuId=BIGI05&statementId=BIGI05&electionCode=2&cityCode={}&townCode=-1&x=45&y=7'.format(citycode)
		url_list.append(url)

	return url_list
	


def fetch_page(url):

	req = requests.get(url)

	html = req.text

	soup = BeautifulSoup(html)

	frame = soup.find('div',{'class':'cont_table'})
	table = frame.find('tbody')
	rows = table.find_all('tr')
	data_list = []
	for row in rows:
		row_list = []
		
		if row.find_all('td')[0].get_text() == "":
			row_list.append(data_list[-1][0])
			row_list.append(row.find_all('td')[1].get_text())
			row_list.append(row.find_all('td')[2].get_text())
			data_list.append(row_list)
		else:
			row_list.append(row.find_all('td')[0].get_text())
			row_list.append(row.find_all('td')[1].get_text())
			row_list.append(row.find_all('td')[2].get_text())
			data_list.append(row_list)	

	return data_list


def make_csv_file(lst):
	with open('district.csv','ab+') as f:
		
		for lst in lsts:
			csv_writer = csv.writer(f)
			dong_list = lst[2].split(',')
			for idx in range(2,len(dong_list)):
				csv_writer.writerow([lst[0].encode('utf-8'),lst[1].encode('utf-8'),dong_list[idx].encode('utf-8')])
		


if __name__ == "__main__":
	urls = make_url()
	for url in urls:
		lsts = fetch_page(url)
		make_csv_file(lsts)
				
	
