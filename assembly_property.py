# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import csv


def make_url(url, page):

    board_url_list = [url.format(num) for num in range(1, page+1)]

    return board_url_list


def make_detail_url(url):

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html)
    frame = soup.find('ul', 'list_p2 dtv mgt10')
    lis = frame.find_all('li', {'class': 'bundle1'})
    url_list = []
    for li in lis:
        for content in li.find_all('li', {'class': 'bundle2'}):

            back_url = content.find('a', href=True)['href'][1:]
            base_url = 'http://the300.mt.co.kr/db/yeuido300{}'
            url = base_url.format(back_url)

            url_list.append(url)

    return url_list


def fetch_the_page(url, csv_writer):

    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    profile = soup.find('div', {'class':'lmbox2'}).find('div', {'class': 'rel_info'})
    name = profile.find('strong').find('span', {'class': 'kr'}).text
    party = soup.select('.lmbox2 .rel_info span img')[0]['alt']
    election_district = profile.find('ul').find_all('li')[1].text

    # print name
    # print district

    try:
        tables = soup.find_all('div',{'class':'table_t1'})[2]
        tbody = tables.find('tbody')
        for t in tbody.find_all('tr'):

            role = t.find_all('td')[0].text
            type = t.find_all('td')[1].text
            location = t.find_all('td')[2].text.split()
            city = location[0]
            district = location[1]
            width = float(t.find_all('td')[3].text[:-1])
            cost = int(t.find_all('td')[4].text.replace(",",""))

            csv_writer.writerow([name.encode('utf-8'), party.encode('utf-8'), election_district.encode('utf-8'), role.encode('utf-8'), type.encode('utf-8'), city.encode('utf-8'), district.encode('utf-8'), width, cost])

        time.sleep(30)
    except IndexError:
        time.sleep(10)
        pass


def main():
    with open('assembly_property.csv', 'wb') as f:
        csv_writer = csv.writer(f)
        url = 'http://the300.mt.co.kr/db/yeuido300/yeuido300List.html?srcParty=&g_party2=&g_cntgubun=&g_howto=&city=&district=&keyword=&page={}'
        page = 19
        url_list = make_url(url, page)
        for urls in url_list:
            print "{} / {}".format(url_list.index(urls), len(url_list))
            contents = make_detail_url(urls)
            for content in contents:
                print "{} / {}".format(contents.index(content), len(contents))
                fetch_the_page(content, csv_writer)


if __name__ == "__main__":
    main()
