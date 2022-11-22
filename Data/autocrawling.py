import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from konlpy.tag import Mecab
from functools import wraps
import errno
import os
import signal
import pymysql
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

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
    for url_no in news_url:
        print(url_no)
        try:
            chromeTest(url_no)
        except TimeoutError as e:
            os.system("pkill chrome")
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            print("TimeoutError")
            continue
        html = driver.page_source
        soup = BeautifulSoup(html)
        str = ""
        for text in soup.findAll("p"):
            str += text.get_text() + "\n"
        whole_text += np_tag(str)
    return whole_text



def np_tag(text):
    global category
    global nation
    global start_year
    global start_month
    global start_day
    global exceptkeyword
    global removekeyword

    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    text = hangul.sub('', text)
    m = Mecab()
    list = m.pos(text)
    news_desc = ""
    date_time_str = str(start_year).zfill(2)+"-"+str(start_month).zfill(2)+"-"+str(start_day).zfill(2)
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    print(start_month,start_day,category)
    for doc in list:
        #if doc[1] == 'NNP' or doc[1] == 'NNG':
        flag = True
        if doc[1] == 'NNP':
            for i in range(len(exceptkeyword)) :
                if exceptkeyword[i] in doc[0] :
                    flag = False
                    # print("doc[0] : ",doc[0],", exceptkeyword : ", exceptkeyword[i])

                    val = (doc[0].replace(" ", ""),date_time_obj,nation,category)
                    for i in range(6) : 
                        cursor.execute(sql,val)
                        DoYouKnow_db.commit()
            if(flag):
                # print("doc[0] : ",doc[0])
                val = (doc[0].replace(" ", ""),date_time_obj,nation,category)
                cursor.execute(sql,val)
                DoYouKnow_db.commit()
                
                    # news_desc += doc[0].replace(" ", "_") + '\n'

    # nospacetext = text.replace(" ","")
    # for i in range(len(exceptkeyword)):
    #     if exceptkeyword[i] in nospacetext :
    #         val = (exceptkeyword[i],date_time_obj,nation,category)
    #         for i in range(5):
    #             cursor.execute(sql,val)
    #             DoYouKnow_db.commit()

    return news_desc



def Url(search):
    result = ""
    global start_year
    global start_month
    global start_day
    global end_year
    global end_month
    global end_day
    global driverd
    # here
    url_temp = 'https://www.google.com.vn/search?hl=vi&q={search}&tbm=nws'.format(search=search)
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

        # print(news_urls)
        result += news(news_urls)
    return result

start = time.time()
start_year=2022
start_month=1
start_day=1
end_year=start_year
end_month=start_month
end_day=start_day
category = 0
nation = 0

removekeyword=[]
exceptkeyword=[]
def crawling_category(searches, category_id, month, nation_id):
    global start_year
    global start_month
    global start_day
    global end_year
    global end_month
    global end_day
    global driver
    global category
    global nation
    global removekeyword
    global exceptkeyword

    print(searches, category_id, month, nation_id)
    day =[32, 29, 32, 31, 32, 31, 32, 32, 31, 6, 31, 32]
    
    start = time.time()
    start_year=2022
    start_month=month
    end_year=start_year
    end_month=month
    nation = nation_id

    #keyword remove start
    File2 = open("/home/hadoop/S07P22B208/Data/removekeyword.txt", encoding='utf-8')
    # removekeyword = []
    while True : 
        line = File2.readline().strip()
        if not line : break
        removekeyword.append(line)
    #keyword remove end

    for cnt in range(len(searches)):
        print(searches[cnt], category_id[cnt])
        category = category_id[cnt]

        # File=None
        # exceptkeyword = []
        #keyword weight start
        if category==2 :
            # print("are you comein222222222222@@??????")
            File = open("/home/hadoop/S07P22B208/Data/dramaexcept.txt", encoding='utf-8')
            while True : 
                line = File.readline().strip()
                if not line : break
                exceptkeyword.append(line)
        elif category==3 :
            File = open("/home/hadoop/S07P22B208/Data/movieexcept.txt", encoding='utf-8')
            while True : 
                line = File.readline().strip()
                if not line : break
                exceptkeyword.append(line)
        elif category==1 :
            File = open("/home/hadoop/S07P22B208/Data/sportexcept.txt", encoding='utf-8')
            while True : 
                line = File.readline().strip()
                if not line : break
                exceptkeyword.append(line)
        elif category==4 :
            File = open("/home/hadoop/S07P22B208/Data/idolexcept.txt", encoding='utf-8')
            while True : 
                line = File.readline().strip()
                if not line : break
                exceptkeyword.append(line)
        elif category==5 :
            File = open("/home/hadoop/S07P22B208/Data/actorexcept.txt", encoding='utf-8')
            while True : 
                line = File.readline().strip()
                if not line : break
                exceptkeyword.append(line)
        

        # while True : 
        #     line = File.readline().strip()
        #     if not line : break
        #     exceptkeyword.append(line)

        #keyword weight end
    
        for i in range(1,day[month-1]):
        # for i in range(1,2):
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            
            start_day=i
            end_day=start_day

            # Url(searches[cnt])
            try:
                Url(searches[cnt])
            except Exception as e:
                print("timeout")
                continue
            finally:
                driver.quit()
                print("============")
                
        driver.quit()
    print("time!!!!!!!!!!!!!!!!!!!!! :", time.time() - start)


def cawrling_month(search, category_id, nation_id):
    global start_year
    global start_month
    global start_day
    global end_year
    global end_month
    global end_day
    global driver
    global category
    global nation
    days =[32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]
    for month in range(9, 3, -1):
        start_month = month
        end_month=month
        for day in range(24,days[month-1]):
            print('month, day', month, day)
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            
            start_day=day
            end_day=start_day
            try:
                Url(search)
            except Exception as e:
                print("timeout")
                continue
            finally:
                # f = open(textname, 'w', encoding='utf-8')
                # f.write(whole_text)
                # f.close()
                driver.quit()
                print("============")
                
        driver.quit()
    print("time!!!!!!!!!!!!!!!!!!!!! :", time.time() - start)