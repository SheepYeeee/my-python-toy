import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime
import csv
import urllib
import time
import json

page = 1
allcon=[]
while page <=20:
    url = f"https://www.518.com.tw/job-index-P-{page}.html?i=1&am=1&ab=2032001,2032002,"
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rows = soup.find_all('ul', class_='all_job_hover')
    contents=[]
    

    for row in rows:
        bigtitle=row.find_next('li',attrs={'class':'title'})#標題外層
        ahref=bigtitle.find_next('a')#標題內層的a
        title=ahref.find_next('span')#標題內層的標題
        thisurl=title.find_next('span')#徵才連結
        urls=[thisurl.string]
        # print(urls)
        for url in urls:
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'lxml')
            colname = list(rows.pop(0).stripped_strings)
            htitle=soup.find('h1',attrs={'class':'job-title'})#標題第三層
            job=htitle.find_next('strong')#標題最裡層 這個需要
            com=soup.find('div',attrs={'id':'jobnewDetail'})#工作詳情最外層
            path=com.find_next('div',attrs={'class':'path_location'})#分類最外層
            path1=path.find_next('a')#找工作 不需要
            path2=path1.find_next('a')#縣市 這個需要
            path3=path2.find_next('a')#行業類別 這個需要
            path4=path3.find_next('a')#公司 需要吧
            contentbox=soup.find('div',attrs={'id':'content'})#工作詳情 最外層
            content=contentbox.find_next('div',attrs={'class':'job-detail-box'})#工作詳情 外層
            cont=content.find_next('h4')#工作詳情 外層
            outdetail=cont.find_next('div',attrs={'class':'JobDescription'})#工作詳情 外層
            detail=outdetail.find_next('p')#工作詳情 這個需要
            jobitem=detail.find_next('div',attrs={'class':'jobItem'})#工作要點 外層
            item1=jobitem.find_next('dl')
            item2=item1.find_next('dt')
            item3=item2.find_next('dd')#薪資
            item4=item3.find_next('dt')
            item5=item4.find_next('dd')#上班地點
            item6=item5.find_next('dt')
            item7=item6.find_next('dd')#上班
            item8=item7.find_next('dt')
            item9=item8.find_next('dd')#休假    
            item10=item9.find_next('dt')
            item11=item10.find_next('dd')#職務類別 外層 
            item12=item11.find_next('a')#職務類別 這個需要
            item13=item12.find_next('a')#職務類別 這個需要
            item14=item13.find_next('a')#職務類別  這個需要

            c=[job.string, path2.string, path3.string, path4.string, detail.text,item12.string,item13.string,item14.string]
            print(c)
            contents.append(c)
    allcon.extend(contents)
    df=pd.DataFrame(allcon) #轉成dataframe 為了最後輸出成csv
    df.head()
    page = page + 1
    # url=f"https://www.518.com.tw/job-index-P-{page}.html?i=1&am=1&ab=2032001,2032002,"
    # time.sleep(1)

cwd=os.getcwd()
timestamp=datetime.datetime.now()
timestamp=timestamp.strftime('%Y%m%d')
filename=os.path.join(cwd,'518_detail{}.csv'.format(timestamp))
df.to_csv(filename,index=False, encoding='utf_8_sig')
print('Save csv to {}'.format(filename))






