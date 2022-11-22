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

        resultcount=0
        removekeyword=[]
        File2 = open("/home/hadoop/S07P22B208/Data/removekeyword.txt", encoding='utf-8')
        while True : 
            line = File2.readline().strip()
            if not line : break
            removekeyword.append(line)

        for index in results:
            resultcount+=1
            print(resultcount,"/",len(results))
            word=index['name']
            count=index['count']

            
            datas = word.split(',')
            
            if(resultcount>=100001 and resultcount<=200000) : 
                print(resultcount,"/",len(results))
                if(datas[0] == '블랙' and datas[3] == 4) :
                    print('blackpink in your area', datas)
                    datas[0] = '블랙핑크'
                
                #단어길이가 1일때 건너뛰기
                if len(datas[0]) == 1 : continue
                #제외키워드에 걸렸을때 건너뛰기
                flag = True
                for i in range(len(removekeyword)) : 
                    if removekeyword[i] == datas[0]:
                        print(datas[0])
                        flag = False
                        break
                if flag==False : continue

                val=(count,datetime.strptime(datas[1],'%Y-%m-%d'),datas[0],datas[3],datas[2])
                cursor.execute(insertsql,val)
                connection.commit()
            
        # cursor.execute(trunsql)
        connection.commit()
    except:
        print ("Error: unable to fecth data")
connection.close()