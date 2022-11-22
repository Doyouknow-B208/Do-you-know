import pymysql.cursors
import pymysql
import sys
import os
from datetime import datetime

connection = pymysql.connect(
    user='b208',
    passwd='b208root',
    host='43.201.37.208',
    db='DoYouKnow',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
with connection.cursor() as cursor:
    try:
        sql = "SELECT * FROM keywordtmp"
        insertsql = "insert into keyword (count,date,name,category_id,nation_id) values (%s,%s,%s,%s,%s)"
        trunsql = "TRUNCATE keywordtmp"

        cursor.execute(sql)
        results = cursor.fetchall()

        for index in results:

            word=index['name']
            count=index['count']

            datas = word.split(',')

            
            val=(count,datetime.strptime(datas[1],'%Y-%m-%d'),datas[0],datas[3],datas[2])
            cursor.execute(insertsql,val)
            connection.commit()
            
        cursor.execute(trunsql)
        connection.commit()
    except:
        print ("Error: unable to fecth data")
connection.close()