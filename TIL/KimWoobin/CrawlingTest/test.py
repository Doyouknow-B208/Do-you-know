from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

def Url(search):
    url_temp = 'https://www.google.com/search?q={search}&tbm=nws'.format(search=search)
#     url_temp = 'https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd={search}&bgndt=20190401&enddt=20190930&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt'.format(search=search)
    for pageNo in range(1,300,10):
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
        news(news_urls)
        
def news(news_urls):
    for url_no in news_urls:
        print(url_no)
        driver = webdriver.Chrome()
        driver.get(url_no)

        html = driver.page_source
        soup = BeautifulSoup(html)

        for text in soup.findAll("p"):
            print(text.get_text())
        
        print("================")
        test = soup.find('p').getText()
        test = test.replace('<p>',"")
        test = test.replace('</p>',"")
        print(test)   
        
search = 'korean dramas'
Url(search)