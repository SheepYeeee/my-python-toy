# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import csv

##csv寫入sql 但csv的colname也會被輸入 需手動刪除 0 6 9
db = pymysql.connect(host='localhost',user='root',password='0000',db='cardhub',charset='utf8')
cur = db.cursor()
with open('D:\py\\analysis\\designer_0_20190322.csv', encoding = "utf_8_sig") as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            item1=row[0]
            item2=row[1]
            sql = "INSERT INTO `designer_job` (`designer_job_name`, `designer_job_count`) VALUES (%s, %s)"
            cur.execute(sql,(item1,item2))

with open('D:\py\\analysis\\designer_6_20190322.csv', encoding = "utf_8_sig") as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            item1=row[0]
            item2=row[1]
            sql = "INSERT INTO `designer_item` (`designer_item_name`, `designer_item_count`) VALUES (%s, %s)"
            cur.execute(sql,(item1,item2))

with open('D:\py\\analysis\\designer_9_20190322.csv', encoding = "utf_8_sig") as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            item1=row[0]
            item2=row[1]
            sql = "INSERT INTO `designer_skill` (`designer_skill_name`, `designer_skill_count`) VALUES (%s, %s)"
            cur.execute(sql,(item1,item2))
db.commit()
cur.close()
print("Done")


#sql寫入csv
# with open("D:\py\\analysis\blabla.csv", "w") as fh:
#     chunks = pd.read_sql_query("SELECT * FROM job", db, chunksize=10000)
#     next(chunks).to_csv(fh, index=False)  # write the first chunk with the column names,
#                                           # but ignore the index (which will be screwed up anyway due to the chunking)
#     for chunk in chunks:
#         chunk.to_csv(fh, index=False, header=False) # skip the column names from now on

    



    