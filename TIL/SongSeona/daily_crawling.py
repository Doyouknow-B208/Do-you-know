import re
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from konlpy.tag import Mecab
from functools import wraps
import errno
import signal
import pymysql
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

DoYouKnow_db= pymysql.connect(
    user='b208', 
    passwd='b208root', 
    host='43.201.37.208', 
    db='RawData', 
    charset='utf8'
)
cursor = DoYouKnow_db.cursor(pymysql.cursors.DictCursor)
sql = "insert into rawdatatest (name,data_date,nation_id,category_id) values (%s,%s,%s,%s)"

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
    global driver
    for url_no in news_url:
        print(url_no)
        try:
            chromeTest(url_no)
        except TimeoutError as e:
            os.system("pkill chrome")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("lang=ko_KR") 
            driver = webdriver.Chrome(executable_path="/home/hadoop/S07P22B208/TIL/SongSeona/chromedriver",chrome_options=chrome_options)
            print("TimeoutError")
            continue
        html = driver.page_source
        soup = BeautifulSoup(html)
        str = ""
        for text in soup.findAll("p"):
            str += text.get_text() + "\n"
        np_tag(str)



def np_tag(text):
    global category
    global nation
    global start_year
    global start_month
    global start_day
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    text = hangul.sub('', text)
    m = Mecab()
    list = m.pos(text)
    date_time_str = str(start_year).zfill(2)+"-"+str(start_month).zfill(2)+"-"+str(start_day).zfill(2)
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    for doc in list:
        #if doc[1] == 'NNP' or doc[1] == 'NNG':
        if doc[1] == 'NNP':
            val = (doc[0].replace(" ", ""),date_time_obj,1,category)
            cursor.execute(sql,val)
            DoYouKnow_db.commit()


def Url(search):
    global start_year
    global start_month
    global start_day
    global end_year
    global end_month
    global end_day
    global driver
    url_temp = 'https://www.google.com/search?q={search}&tbm=nws'.format(search=search)
    url_temp = url_temp + "&tbs=cdr%3A1%2Ccd_min%3A{start_month}".format(start_month=start_month)
    url_temp = url_temp + "%2F{start_day}".format(start_day=start_day)
    url_temp = url_temp + "%2F{start_year}".format(start_year=start_year)
    url_temp = url_temp + "%2Ccd_max%3A{end_month}".format(end_month=end_month)
    url_temp = url_temp + "%2F{end_day}".format(end_day=end_day)
    url_temp = url_temp + "%2F{end_year}".format(end_year=end_year)
    for pageNo in range(0,10,10):
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
        news(news_urls)



# searches = ['korean drama', 'korean singer', 'korean movie', 'korean actor', 'korea sports', 'korean football', 'korean player']
# category_id = [2, 4, 3, 5, 1, 1, 1]
start = time.time()
start_year=datetime.today().year
start_month=datetime.today().month
start_day=datetime.today().day-1
end_year=start_year
end_month=start_month
end_day=start_day
category = 0
nation = 0

def crawling_category(searches, category_id, nation_id):
    global search
    global category
    global nation
    global driver

    print(searches, category_id, nation_id)
    for i in range(len(searches)):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("lang=ko_KR") 
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

        search = searches[i]
        category = category_id[i]
        nation = nation_id
        try:
            print("search, category nation", search, category, nation)
            Url(search)
        except Exception as e:
            print("timeout")
            continue
        finally:
            cnt =0
            driver.quit()
            print("============")
            
    driver.quit()
    print("time!!!!!!!!!!!!!!!!!!!!! :", time.time() - start)