from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import RegexpParser
from nltk import Tree
import nltk
import re
import pandas as pd
from konlpy.tag import Okt
from nltk.corpus import stopwords
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from konlpy.tag import Mecab
from functools import wraps
import errno
import os
import signal
import pymysql
from datetime import datetime

DoYouKnow_db= pymysql.connect(
    user='b208', 
    passwd='b208root', 
    host='43.201.37.208', 
    db='RawData', 
    charset='utf8'
)
cursor = DoYouKnow_db.cursor(pymysql.cursors.DictCursor)
sql = "insert into rawdata (name,data_date,nation_id,category_id) values (%s,%s,%s,%s)"

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

@timeout(60)
def chromeTest(url):
    driver.get(url)
    pyautogui.hotkey('shift', 'F10')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    time.sleep(1)
    for c in range(0,5):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

def news(news_url):
    whole_text = ""
    global driver
    global cnt
    for url_no in news_url:
        print(url_no)
        # chromeTest(url_no)
        print("WFWEFWEFEWFWE")
        try:
            chromeTest(url_no)
        except TimeoutError as e:
            print("nononono")
            os.system("pkill chrome")
            cnt += 1
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(executable_path="/home/hadoop/S07P22B208/TIL/SongSeona/chromedriver",chrome_options=chrome_options)
    
            print("nononono3")
            continue
        html = driver.page_source
        soup = BeautifulSoup(html)
        str = ""
        for text in soup.findAll("p"):
            str += text.get_text() + "\n"
        whole_text += np_tag(str)
    return whole_text



def np_tag(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    text = hangul.sub('', text)
    m = Mecab()
    list = m.pos(text)
    news_desc = ""
    date_time_str = str(start_year).zfill(2)+"-"+str(start_month).zfill(2)+"-"+str(start_day).zfill(2)
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    for doc in list:
        #if doc[1] == 'NNP' or doc[1] == 'NNG':
        if doc[1] == 'NNP':
            val = (doc[0].replace(" ", "_"),date_time_obj,4,2)
            cursor.execute(sql,val)
            DoYouKnow_db.commit()
            news_desc += doc[0].replace(" ", "_") + '\n'
    return news_desc


def Url(search):
    result = ""
    global start_year
    global start_month
    global start_day
    global end_year
    global end_month
    global end_day
    url_temp = 'https://www.google.com.hk/search?gl=hk&hl=zh-CN&q={search}&tbm=nws'.format(search=search)
    url_temp = url_temp + "&tbs=cdr%3A1%2Ccd_min%3A{start_month}".format(start_month=start_month)
    url_temp = url_temp + "%2F{start_day}".format(start_day=start_day)
    url_temp = url_temp + "%2F{start_year}".format(start_year=start_year)
    url_temp = url_temp + "%2Ccd_max%3A{end_month}".format(end_month=end_month)
    url_temp = url_temp + "%2F{end_day}".format(end_day=end_day)
    url_temp = url_temp + "%2F{end_year}".format(end_year=end_year)
    for pageNo in range(0,300,10):
        url = url_temp + "&start={pageNo}".format(pageNo=pageNo)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html)
        
        news_urls = []
        # 검색 했을 때 제목과 breadcrumbs, 접속주소를 가져올 것이다.
        list = soup.select('#search .MjjYud>div>div>div')
        if not list:
            print("no articles")
            break

        for i in list:
            if i.select_one('div>a>div>div:nth-child(2)>div:nth-child(2)'):
                news_urls.append(i.select_one(".WlydOe").get("href"))
            else:
                print("no texts")

        print(news_urls)
        result += news(news_urls)
    return result

cnt = 0
start = time.time()
search = '韩剧'
start_year=2022
start_month=8

for i in range(1,31):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path="/home/hadoop/Sub2/S07P22B208/TIL/SongSeona/chromedriver",chrome_options=chrome_options)
    
    print(i)
    start_day=i
    end_year=start_year
    end_month=start_month
    end_day=start_day
    whole_text = ""
    textname = "/home/hadoop/Project/data/{search}_".format(search=search.replace(" ","_"))
    textname += str(start_year).zfill(2)+str(start_month).zfill(2)+str(start_day).zfill(2)+".txt"

    try:
        whole_text = Url(search)
    except Exception as e:
        print(e)
        print("timeout")
        continue
    finally:
        # f = open(textname, 'w', encoding='utf-8')
        # f.write(whole_text)
        # f.close()
        cnt =0
        driver.quit()
        print("============")
        
driver.quit()
print("time!!!!!!!!!!!!!!!!!!!!! :", time.time() - start)