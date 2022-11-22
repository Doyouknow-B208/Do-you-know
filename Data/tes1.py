from cgi import print_form
import requests
import json
import pymysql

DoYouKnow_db= pymysql.connect(
    user='b208', 
    passwd='b208root', 
    host='43.201.37.208', 
    db='DoYouKnow', 
    charset='utf8'
)
cursor = DoYouKnow_db.cursor(pymysql.cursors.DictCursor)
sql = "insert into news (link,image,title,keyword,nation_id) values (%s,%s,%s,%s,%s)"

keyword = "손흥민"
searchkeyword = ["sonny","sonny","ソン・フンミン","sonny","sonny","sonny"]
language = ["en","en","jp","vi","id","pt"]

for _ in range(len(searchkeyword)):
    print(searchkeyword[_])
    print(language[_])
    url_temp = 'https://newsapi.org/v2/everything?apiKey=b7e2285d0d434655b79ad42f6584ae3f&q={search}&language={lang}&sortBy=relevancy&pageSize=10'.format(search=searchkeyword[_],lang=language[_])
    try:
        response  = requests.get(url_temp, timeout=5, verify=False)
    # Timeout 처리
    except requests.exceptions.Timeout:
       print('error')

    # InterError 및 기타에러 처리
    except Exception as e:
       print(e)
    print(response.status_code)
    js1 = json.loads(response.text)
    for a in js1['articles']:
        url = a['url']
        image = a['urlToImage']
        title = a['title']
#         if len(url)==0 or len(image)==0 or len(title)==0:
#             continue
        if url and image and title:
            print(url)
            print(image)
            print(title)
            print(keyword)
            print(str(_+1))
            val = (url,image,title,keyword,str(_+1))
            cursor.execute(sql,val)
            DoYouKnow_db.commit()