from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import urllib
import json
import time
import csv
import os

#資訊類 https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=1&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc
#設計類 https://www.104.com.tw/jobs/search/?ro=0&jobcat=2013001000&order=1&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc
#行銷類 https://www.104.com.tw/jobs/search/?ro=0&jobcat=2004001000&order=1&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc
#學術類 https://www.104.com.tw/jobs/search/?ro=0&jobcat=2016001000%2C2016002002%2C2016002004%2C2016002021&order=11&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc
#金融類 https://www.104.com.tw/jobs/search/?ro=0&jobcat=2003000000&order=11&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc
page = 1
allcon=[]
while page <=150:
    print(page)
    url = f"https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&order=1&asc=0&excludeJobKeyword=%E6%8E%A5%E6%A1%88%20%E5%AE%B6%E6%95%99&excludeCompanyByCustno=53r9uag&page={page}&mode=s&jobsource=2018indexpoc"
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    rows = soup.find_all('article', class_='js-job-item')
    contents=[]

    for row in rows:
        bigtitle=row.find_next('div',attrs={'class':'b-block__left'})#標題外層
        ahref=bigtitle.find_next('h2',attrs={'class':'b-tit'})#標題內層的a
        ba=ahref.find_next('span',attrs={'class':'b-tit__date'})#標題內層的標題
        title=ba.find_next('a')#徵才連結
        thisurl=title.get('href')
        thisurl='https:'+thisurl
        urls=[thisurl]

        for url in urls:
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'lxml')
            colname = list(rows.pop(0).stripped_strings)

            idjob=soup.find('div',attrs={'class':'wrap'})#標題最外層
            out=idjob.find_next('article')
            ot=out.find_next('header')
            com=ot.find_next('div')

            job=com.find_next('h1')
            mjob=job.text.replace(' ','')
            myjob=mjob.split('\n')#標題在這 這個需要
            
            center=soup.find('div',attrs={'class':'grid-left'})#工作詳情最外層
            main=center.find_next('main')#第二層
            info1=main.find_next('section',attrs={'class':'info'})#第三層
            cont=info1.find_next('div',attrs={'class':'content'})#第四層
            detail=cont.find_next('p')#第五層 工作詳情 這個需要 有些人沒有

            dl=cont.find_next('dl')
            cate=dl.find_next('dd')
            item1=cate.find_next('span')#職務類別 相關標籤
            item2=item1.find_next('span')#職務類別 相關標籤
            item3=item2.find_next('span')#職務類別 相關標籤
            sal=cate.find_next('dd')#薪資
            alw=sal.find_next('dd')#工作性質

            addme=alw.find_next('dd',attrs={'class':'addr'})#上班地點
            addr=addme.text.replace(' ','')
            addr=addr.split('\n')#上班地點 這個需要

            info2=info1.find_next('section')#職位需求最外層
            cont2=info2.find_next('div',attrs={'class':'content'})#第二層
            dll=cont2.find_next('dl')#第三層 dl
            need1=dll.find_next('dd')#身分
            need2=need1.find_next('dd')#工作經歷
            need3=need2.find_next('dd')#學歷要求
            need4=need3.find_next('dd')#科系要求
            need5=need4.find_next('dd')#語文條件
            nee6=need5.find_next('dd')#語文條件

            need6=need5.find_next('dd')#擅長工具 這個需要
            need6=need6.text.replace(' ','')
            need6=need6.split('、')


            need7=nee6.find_next('dd')#工作技能 這個需要
            need8=need7.find_next('dd')#其他條件 這個需要
            
            
            # c=[myjob[1],addr[1],myjob[2],detail.text,need6.text,need7.text,need8.text,item1.text,item2.text,item3.text]
            if len(need6)==1:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0]]
            elif len(need6)==2:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0],need6[1]]
            elif len(need6)==3:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0],need6[1],need6[2]]
            elif len(need6)==4:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0],need6[1],need6[2],need6[3]]
            elif len(need6)==5:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0],need6[1],need6[2],need6[3],need6[4]]
            elif len(need6)==6:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0],need6[1],need6[2],need6[3],need6[4],need6[5]]
            else:
                a=[myjob[1],addr[1],myjob[2],detail.text,need7.text,need8.text,item1.text,item2.text,item3.text,need6[0]]
            
            print(a)
            contents.append(a)
            time.sleep(1)#讓他睡 不然跑到一半就壞!
    allcon.extend(contents)
    #df=pd.DataFrame(allcon,columns = ["工作職位","上班地點","徵才公司","工作詳情","工作技能","其他條件","相關標籤","相關標籤","相關標籤","擅長工具"]) 
    df=pd.DataFrame(allcon) 
    df.head()
    page = page + 1
    
    

# cwd=os.getcwd()
# timestamp=datetime.datetime.now()
# timestamp=timestamp.strftime('%Y%m%d')
# filename=os.path.join(cwd,'financial_104_{}.csv'.format(timestamp))
# df.to_csv(filename,index=False, encoding='utf_8_sig')
# print('Save csv to {}'.format(filename))






