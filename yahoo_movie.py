import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import datetime
import csv

url = 'https://movies.yahoo.com.tw/chart.html'
resp = requests.get(url)
resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
soup = BeautifulSoup(resp.text, 'lxml')

# parse colname 
rows = soup.find_all('div', class_='tr')
# get strings and convert into list
colname = list(rows.pop(0).stripped_strings) 

#parse rest content info
contents=[]

for row in rows:
    thisweek_rank=row.find_next('div',attrs={'class':'td'})#本周排名
    updown=thisweek_rank.find_next('div')#排名浮動
    lastweek_rank=updown.find_next('div')#上周排名
    movie_title=lastweek_rank.find_next('div',attrs={'class':'td'})#電影名稱的外層

    #for the data from of first row in this web page is different from other rows
    if thisweek_rank.string==str(1):
        movie_title=lastweek_rank.find_next('h2')#本周第一的格式不同 要找片名是找下一個h1
    else:
        movie_title=lastweek_rank.find_next('div',attrs={'class':'rank_txt'})#其他排名的片名是找rank_txt

    release_data=movie_title.find_next('div',attrs={'class':'td'}) #發布日期 有問題

    trailer=release_data.find_next('div',attrs={'class':'td'})
    trailer_address=trailer.find('a')['href']#預告片連結
    stars=row.find('h6',attrs={'class':'count'})#評價星數

    #replace None with empty string ''
    lastweek_rank=lastweek_rank.string if lastweek_rank.string else ''

    c=[thisweek_rank.string,lastweek_rank,movie_title.string,release_data.string,trailer_address,stars.string]
    print(c)
    contents.append(c)
    df=pd.DataFrame(contents,columns=colname)
    df.head()

cwd=os.getcwd()
timestamp=datetime.datetime.now()
timestamp=timestamp.strftime('%Y%m%d')
filename=os.path.join(cwd,'yahoo_movie_rank{}.csv'.format(timestamp))
df.to_csv(filename,index=False, encoding='utf_8_sig')
print('Save csv to {}'.format(filename))
