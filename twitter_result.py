#coding:utf-8

import tweepy
from tweepy import OAuthHandler
from time import sleep
import csv

ckey = 'GIVIpuGJkELgmPWEvOtO1CpFI'
csecret = 'I7BZV8LCBm88fA4Qr54IsU3LvzwKpimHb7h5DmbWvyQIdYlOIQ'
atoken = '871426368-lW9WVKfZpyVychFtyLSUHWQOcDFi7KsYDuwh2bCt'
asecret = 'sTHo8oLeQ80c0jJ7oKXGm5P1MKnA2VoYoFqY9q7zPK3rV' 

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth,wait_on_rate_limit=True)
f = open('daegu_04_01.csv','a')
csvWriter = csv.writer(f, delimiter=',')

#put keyword
keyword = '대구'
for tweet in tweepy.Cursor(api.search,q=keyword,since="2015-04-01",until="2015-04-02",include_entitles=True,lang="ko").items():
	try:
		text = tweet.text.encode('utf-8')
		text1 = str(tweet.created_at)

		csvWriter.writerow([text1,text])
		print text1, text
		#f.write(text)
		#f.write(str(text1))
		#f.write("\n")
		#f.write("\n")
	except tweepy.TweepError:
		sleep(10)#coding:utf-8
f.close()

