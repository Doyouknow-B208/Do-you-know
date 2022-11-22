import pymysql.cursors
import pymysql
import sys
import os
from datetime import datetime
for c in range(4,5):
    for m in range(7, 8):
        days =[32, 29, 32, 31, 32, 31, 32, 32, 31, 6, 31, 32]
        for i in range(1,days[m-1]):
            year=2022
            month=m
            day=i
            date=str(year).zfill(2)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)
            # date="2022-08-06"
            nation_id=3
            category_id=c
            print(category_id, month, day)
            date_obj = datetime.strptime(date,"%Y-%m-%d")
            # Open database connection
            connection = pymysql.connect(
                user='b208', 
                passwd='b208root', 
                host='43.201.37.208', 
                db='RawData', 
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            # prepare a cursor object using cursor() method
            with connection.cursor() as cursor:
            # Prepare SQL query to select a record into the database.
                try:

                    sql = "SELECT * FROM rawdata where data_date=%s and nation_id = %s and category_id = %s"
                    # sql = "SELECT * FROM rawdata"
            # Execute the SQL command
                    val = (date_obj,nation_id,category_id)
                    cursor.execute(sql,val)
            # Fetch all the rows in a list of lists.
                    results = cursor.fetchall()
                    # print(results)
                    # path = "/home/hadoop/Project/data/"+str(date)+"_"+str(nation_id)+"_"+str(category_id)+".txt"
                    if results:
                        newfile = open("/home/hadoop/Project/data/DYKRawData.txt","a+", encoding='utf-8')

                    for index in results:
                        ltr=[]
                        ltr.append(index['name'])
                        ltr.append(',')
                        ltr.append(index['data_date'])
                        ltr.append(',')
                        ltr.append(index['nation_id'])
                        ltr.append(',')
                        ltr.append(index['category_id'])
                        lenltr=len(ltr)
                        for i in range(lenltr):
                            newfile.write('{}'.format(ltr[i]))
                        newfile.write("\n")


            # # Now print fetched result
                    #print("ename=%s,empno=%d,job=%d,hiredate=%d,comm=%s,sal=%d,deptno=%d,mgr=%d" %(ename, empno, job, hiredate, comm, sal, deptno, mgr))
                    # print(index)
                except:
                    print ("Error: unable to fecth data")
            # disconnect from server
            connection.close()
            newfile.close()