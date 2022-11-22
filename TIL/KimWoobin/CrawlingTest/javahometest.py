from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import RegexpParser
from nltk import Tree
import nltk
import re
import pandas as pd
import spacy
from konlpy.tag import Okt
from nltk.corpus import stopwords
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import googletrans
import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#python -m spacy download ja_core_news_sm
#ja_core_news_sm
# nlp = spacy.load("ko_core_news_sm")

def news(news_urls):
    translator = googletrans.Translator()
    for url_no in news_urls:
        print(url_no)
        # driver = webdriver.Chrome()
        driver.get(url_no)

        pyautogui.hotkey('shift', 'F10')
        # for i in range(8):
        #     pyautogui.hotkey('down')
        # pyautogui.hotkey('enter')
        pyautogui.keyDown('t')
        pyautogui.keyUp('t')


        time.sleep(1)

        for c in range(0,5):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html)

        str = ""
        str2 = ""
        result = ""
        for text in soup.findAll("p"):

            str += text.get_text() + "\n"
            str2 += text.get_text() + "\n"
        #     if(len(str)>1000):
        #         # result1 = translator.translate(str, dest='ko')
        #         result += str
        #         str = ""

        # if str !="":
        #     # result1 = translator.translate(str, dest='ko')
        #     result += result1.text.replace(" -", "-").replace("- ", "-")
            result += str
            str = ""

        return result



def np_tag(text):
    #text = re.sub('[^a-zA-Z]', ' ', text)
    #text = text.lower()
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    text = hangul.sub('', text)

    print("text :" + text)

    hannanum = Okt()
    df = pd.DataFrame(columns = ['CHUNK'])
    doc = hannanum.nouns(text)
    news_desc = '\n'.join(doc)

    # doc = nlp(text)
    # # for chunk in doc.noun_chunks:
    # #    df = df.append({'CHUNK': chunk.text}, ignore_index=True)
    # for token in doc:
    #    print(token.text, token.pos_, token.dep_)
    print(news_desc)
    return news_desc


driver = webdriver.Chrome()
# driver.get("https://www.teamtalk.com/tottenham-hotspur/son-heung-min-not-taken-richarlison-arrival-well-pundit-antonio-conte-big-problem")
testnews = ['https://www.football.london/tottenham-hotspur-fc/transfer-news/tottenham-son-conte-ndombele-transfer-24937341']
wl =np_tag(news(testnews))
#wl=np_tag("Actors and actresses who are the “leading actors” are absolutely indispensable in Korean dramas.")
#print(no_capitals)
#stops = set(stopwords.words('english'))
#print(no_capitals)

# print(wl)

testnews = ['https://news.yahoo.co.jp/articles/45e111649f3f3c7029f0276d90fef6f49631a5fc']
wl =np_tag(news(testnews))
#wl=np_tag("Actors and actresses who are the “leading actors” are absolutely indispensable in Korean dramas.")
# no_capitals = wl.values.tolist()
#print(no_capitals)
#stops = set(stopwords.words('english'))
#print(no_capitals)

# print(wl)


testnews = ['https://www.kdramastars.com/articles/126325/20220820/k-dramas-north-south-korea-money-heist-korea-crash-landing-on-you.htm']
wl =np_tag(news(testnews))
#wl=np_tag("Actors and actresses who are the “leading actors” are absolutely indispensable in Korean dramas.")
# no_capitals = wl.values.tolist()
#print(no_capitals)
#stops = set(stopwords.words('english'))
#print(no_capitals)

# print(wl)



driver.quit()

# stemmer = nltk.stem.SnowballStemmer('english')

#testmemo =""
# f = open("C:/Users/multicampus/Desktop/test/test.txt", 'w', encoding='utf-8')
# for no_capital in no_capitals:
#     no_stops = [word for word in no_capital if not word in stops]
#     for tmp in no_stops:
#         #testmemo=testmemo+tmp+'\n'
#         f.write(tmp+'\n')
# f.close()