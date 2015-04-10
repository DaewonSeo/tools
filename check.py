#coding:utf-8
from konlpy.tag import Twitter

f = open('daegu.txt','r')
data = f.read().decode('utf-8')

twitter = Twitter()

entire_data = twitter.morphs(data)
result_list = []
for i in entire_data:
    idx = entire_data.count(i)
    info = i.encode('utf-8')
    contents = str(info) + ':' + str(idx)
    result_list.append(contents)

fp = open('result.txt','a')

for a in result_list:
    fp.write(a)
    fp.write("\n")

fp.close()
f.close()
