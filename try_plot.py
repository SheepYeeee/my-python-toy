# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import pandas as pd
import numpy as np
import datetime
import json
import time
import csv
import os

plt.rcParams['font.family']='DFKai-SB'
plt.rcParams['axes.unicode_minus'] = False

df =pd.read_csv('D:\py\\analysis\it_8_20190322.csv' , encoding='utf_8_sig')
df.plot.bar(x = '0', y = '1')
plt.show()

# for num in range(0,14):
    # df =pd.read_csv('D:\py\\analysis\it_'+str(num)+'_20190322.csv' , encoding='utf_8_sig')
    # df.plot.bar(x = '0', y = '1')
    # plt.show()

              