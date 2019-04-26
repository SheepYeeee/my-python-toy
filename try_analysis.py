# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import pandas as pd
import numpy as np
import matplotlib
import datetime
import json
import time
import csv
import os
     
class MyCounter(Counter):
    def __str__(self):
        return "\n".join('{} {}'.format(k, v) for k, v in self.items())

contents=[]
allcon=[]

for num in range(0,14):
    with open('it_104_20190321.csv', encoding = "utf_8_sig") as f:
        r = csv.reader(f, delimiter=',')
        headers = next(r)
        for row in r:
            column = (row[num] for row in csv.reader(f))
            countlist=MyCounter(column)
            countlist=countlist.most_common(10)
            for k,v in countlist:
                # print("{} {}\n".format(k,v))
                c=[k,v]
                contents.append(c)
            df=pd.DataFrame(contents) 
            df.head()
        cwd=os.getcwd()
        timestamp=datetime.datetime.now()
        timestamp=timestamp.strftime('%Y%m%d')
        filename=os.path.join(cwd,'analysis\it_'+str(num)+'_{}.csv'.format(timestamp))
        df.to_csv(filename,index=False, encoding='utf_8_sig')
        print('Save csv to {}'.format(filename))
        contents=[]
              