# pip install googletrans==4.0.0-rc1 # <- cmd로 설치하세요!

import nltk
#nltk.download("book", quiet=True)
#from nltk.book import *
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
from textblob import TextBlob
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import googletrans

def news(news_urls):
    translator = googletrans.Translator()
    for url_no in news_urls:
        print(url_no)
        driver = webdriver.Chrome()
        driver.get(url_no)
        html = driver.page_source
        soup = BeautifulSoup(html)

        str = ""
        str2 = ""
        result = ""
        for text in soup.findAll("p"):

            str += text.get_text() + "\n"
            str2 += text.get_text() + "\n"
            if(len(str)>1000):
                result1 = translator.translate(str, dest='ko')
                result += result1.text
                str = ""

        if str !="":
            result1 = translator.translate(str, dest='ko')
            result += result1.text
        return result

testnews = ['https://news.yahoo.co.jp/articles/45e111649f3f3c7029f0276d90fef6f49631a5fc']
blob = TextBlob(news(testnews))
#test = word_tokenize(news(testnews))

for a in blob.noun_phrases:
    print(a)

def Url(search):
  #  url_temp = 'https://www.google.com/search?q=%7Bsearch%7D&tbm=nws%27.format(search=search)
#     url_temp = 'https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd=%7Bsearch%7D&bgndt=20190401&enddt=20190930&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt%27.format(search=search)
    for pageNo in range(1,10,10):
        url = url_temp + "&start={pageNo}".format(pageNo=pageNo)
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html)

        news_urls = []
        # 검색 했을 때 제목과 breadcrumbs, 접속주소를 가져올 것이다.
        # #search>div>div>div>div>div
        list = soup.select('#search .MjjYud>div>div>div')
        if not list:
            print("없어어어어어어엉~")
            break

        for i in list:
            if i.select_one('div>a>div>div:nth-child(2)>div:nth-child(2)'):
                news_urls.append(i.select_one(".WlydOe").get("href"))
#                 print(i.select_one('div>a>div>div:nth-child(2)>div:nth-child(2)').attrs)
#                 print(i.select_one('.iRPxbe>div:nth-child(2)').text)
            else:
                print("text 속성 없어어어어어어엉~")
        print(news_urls)
        if not news_urls:
            break
        
        blob = TextBlob(news(news_urls))
        for a in blob.noun_phrases:
            print(a)