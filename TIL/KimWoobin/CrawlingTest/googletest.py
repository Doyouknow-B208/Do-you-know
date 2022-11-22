#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install googletrans==4.0.0-rc1


# ### 필요사항
# - 번역 정확도 높이기
# - 파파고 번역기 api 사용후 글 확인 (일본, 프랑스)
# - 전처리 과정

# In[18]:


import nltk
#nltk.download("book", quiet=True)
#from nltk.book import *
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
# from textblob import TextBlob
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import googletrans

# def Url(search):
#   #  url_temp = 'https://www.google.com/search?q=%7Bsearch%7D&tbm=nws%27.format(search=search)
# #     url_temp = 'https://search.mt.co.kr/searchNewsList.html?srchFd=TOTAL&range=IN&reSrchFlag=&preKwd=&search_type=m&kwd=%7Bsearch%7D&bgndt=20190401&enddt=20190930&category=MTNW&sortType=allwordsyn&subYear=&category=MTNW&subType=mt%27.format(search=search)
#     for pageNo in range(1,10,10):
#         url = url_temp + "&start={pageNo}".format(pageNo=pageNo)
#         driver = webdriver.Chrome()
#         driver.get(url)

#         html = driver.page_source
#         soup = BeautifulSoup(html)

#         news_urls = []
#         # 검색 했을 때 제목과 breadcrumbs, 접속주소를 가져올 것이다.
#         # #search>div>div>div>div>div
#         list = soup.select('#search .MjjYud>div>div>div')
#         if not list:
#             print("없어어어어어어엉~")
#             break

#         for i in list:
#             if i.select_one('div>a>div>div:nth-child(2)>div:nth-child(2)'):
#                 news_urls.append(i.select_one(".WlydOe").get("href"))
# #                 print(i.select_one('div>a>div>div:nth-child(2)>div:nth-child(2)').attrs)
# #                 print(i.select_one('.iRPxbe>div:nth-child(2)').text)
#             else:
#                 print("text 속성 없어어어어어어엉~")
#         print(news_urls)
#         if not news_urls:
#             break


# # In[19]:


# def news(news_urls):
#     translator = googletrans.Translator() # 번역하는 함수
#     for url_no in news_urls:
#         print(url_no)
#         driver = webdriver.Chrome()
#         driver.get(url_no)
#         html = driver.page_source
#         soup = BeautifulSoup(html)

#         str = "" # p 태그의 내용을 담는 변수
#         result = "" # 영어로 변환하여 저장할 변수
#         for text in soup.findAll("p"): # soup의 모든 p 태그를 처리
#             str += text.get_text() + "\n" 
#             if(len(str)>1000): # 번역을 위해서 str의 글자수가 1000자보다 넘을 경우에만 번역 실행
#                 # 영어로 변환, 정확도를 위해서 어떤 언어인지 알려주는 것도 좋음
#                 # ref: https://coding-kindergarten.tistory.com/98
# #                 result1 = translator.translate(str, dest='ko')
#                 print(str)
#                 result += translate(str)
# #                 result += result1.text.replace(" -", "-").replace("- ", "-")
#                 str = ""
        
#         # 마지막으로 남아있는 문장 번역
#         if str !="":
#             result += translate(str)
# #             result1 = translator.translate(str, dest='ko')
# #             result += result1.text.replace(" -", "-").replace("- ", "-")
#         return result


# # In[25]:


# import json
# import os
# import sys
# import urllib.request
# client_id = "6yrWrXVyj5VaRKnqi_fv"
# client_secret = "i9h16BCiqz"

# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)

# def translate(str):
#     encText = urllib.parse.quote(str)
#     data = "source=ja&target=en&text=" + encText
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         result = json.loads(response_body.decode('utf-8'))
#         return result['message']['result']['translatedText']
# #         print(result['message']['result']['translatedText'])
#     #     print(response_body.decode('utf-8'))
#     else:
#         print("Error Code:" + rescode)


# In[105]:


import time

def news(news_urls):
   translator = googletrans.Translator() # 번역하는 함수
   for url_no in news_urls:
       print(url_no)
       driver = webdriver.Chrome()
       driver.get(url_no)
       
   
       print("Python, time.sleep(0.5) -> 0.5초 기다림") 
       time.sleep(10)
       html = driver.page_source
       soup = BeautifulSoup(html)

       str = "" # p 태그의 내용을 담는 변수
       result = "" # 영어로 변환하여 저장할 변수
       for text in soup.findAll("p"): # soup의 모든 p 태그를 처리
           str += text.get_text()
#             if(len(str)>1000): # 번역을 위해서 str의 글자수가 1000자보다 넘을 경우에만 번역 실행
#                 # 영어로 변환, 정확도를 위해서 어떤 언어인지 알려주는 것도 좋음
#                 # ref: https://coding-kindergarten.tistory.com/98
#                 result1 = translator.translate(str, dest='en') 
#                 result += result1.text.replace(" -", "-").replace("- ", "-")
#                 str = ""
       
       # 마지막으로 남아있는 문장 번역
#         if str !="":
#             result1 = translator.translate(str, dest='en')
#             result += result1.text.replace(" -", "-").replace("- ", "-")
       return str


text = news(['https://www.kdramastars.com/articles/126325/20220820/k-dramas-north-south-korea-money-heist-korea-crash-landing-on-you.htm'])
text


import spacy
import re

nlp = spacy.load('ko_core_web_md')
# text = 'Yuh-jung Youn won the Oscar for best supporting actress for her performance in "Minari" on Sunday and made history by becoming the first Korean actor to win an Academy Award.'
# text = 'Korean drama "U-Yongu Lawyer is a genius skin", which depicts a new lawyer with autism spectrums, growing, and has a great response in Japan.'
# text = 'In response to the statement of Lee Sanbek, the drama official commented on the Korean media carefully commented on the Korean media. However, "The scriptwriter Moon Ji-won and Yu Insok are positive attitude", and the possibilities of Season 2 are certainly talked about among the production teams!'
# text = 'If watching Squid Game means the prospect of playing red light, green light now fills you with nerve-shredding terror rather than fond childhood memories, you aren\t alone.The Korean thriller, which tells the story of debt-ridden people competing for a huge cash prize in a deadly series of children\s games, has become Netflix\s biggest ever series launch - streamed by 111 million users in its first 28 days.In doing so it knocked Bridgerton off the top spot, making clear that Korean dramas have most certainly been given the green light by audiences worldwide. So, how can we understand this rise, and what are some of the other K-dramas to look out for if you\'re a new convert?'

# text = re.sub('"[^a-zA-Z]"', ' ', text)
text = text.replace('\"', "")
text = text.lower()
doc = nlp(text)

noun_chunks = doc.noun_chunks

print("=="*40)
str_format = "{:>30}{:>15}{:>15}{:>20}"
print(str_format.format('Text', 'Root Text', 'Root Dep', 'Root Head Text'))
print("=="*40)

data = []
for chunk in doc.noun_chunks:
    data.append(chunk.text)
    print(str_format.format(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))


# # In[54]:


# text


# # In[108]:


# from nltk.corpus import stopwords

# data
# result = []
# for token in data:
#     result.append(token.split())

# # 불용어 제거
# stops = set(stopwords.words('english'))
# for data in result:
#     for word in data:
#         if word in stops:
#             data.remove(word)


# # In[109]:


# import nltk

# tag=[nltk.pos_tag(data) for data in result if data]
# print(tag)


# # - pos: n(명사), v(동사), a(형용사), r(부사), satellite adjectives(s)
# # - NN, NNS, NNP, NNPS (n)
# # - VB, VBD, VBG, VBN, VBP, VBZ (v)
# # - RB, RBR, RBS (r)
# # - JJ (a)

# # In[48]:


# n = {'NN', 'NNS', 'NNP', 'NNPS'}
# v = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
# r = {'RB', 'RBR', 'RBS'}
# a = {'JJ'}


# # In[49]:


# list(tag)


# # In[99]:


# test = []
# for tags in tag:
#     result = []
#     for word in tags:
#         word = list(word)
#         if word[1] in n:
#             word[1] = 'n'
#         elif word[1] in v:
#             word[1] = 'v'
#         elif word[1] in r:
#             word[1] = 'r'
#         elif word[1] in a:
#             word[1] = 'a'
#         else:
#             word[1] = 'n'
#         result.append(word)
#     test.append(result)


# # In[51]:


# test


# # In[100]:


# from nltk.stem import WordNetLemmatizer

# lemma = WordNetLemmatizer()
# result = []
# for texts in test:
#     keyword = ""
#     for text in texts:
#         keyword += lemma.lemmatize(text[0],text[1]) + " "
# #         print(lemma.lemmatize(text[0],text[1]))
#     result.append(keyword.strip())


# # In[90]:


# result


# # In[91]:


# import json
# import os
# import sys
# import urllib.request
# client_id = "6yrWrXVyj5VaRKnqi_fv"
# client_secret = "i9h16BCiqz"

# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)

# def translate(str):
#     encText = urllib.parse.quote(str)
#     data = "source=en&target=ko&text=" + encText
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         result = json.loads(response_body.decode('utf-8'))
#         return result['message']['result']['translatedText']
# #         print(result['message']['result']['translatedText'])
#     #     print(response_body.decode('utf-8'))
#     else:
#         print("Error Code:" + rescode)


# # In[103]:


# translate("squid game. prospect. red light. green light. nerve-shredding terror. fond childhood memory. alone.the korean thriller. story. debt-ridden people. huge cash prize. deadly series. children's game. 111 million user. bridgerton. top spot. korean drama. green light. audience. rise. other k-dramas. new convert")


# # In[38]:


# str = "u-yongu \n squid game. prospect. red light. green light. nerve-shredding terror. fond childhood memory. alone.the korean thriller. story. debt-ridden people. huge cash prize. deadly series. children's game. 111 million user. bridgerton. top spot. korean drama. green light. audience. rise. other k-dramas. new convert"


# # In[39]:


# translator = googletrans.Translator() # 번역하는 함수
# translator.translate(str, src='en', dest='ko').text


# # In[101]:


# txt = "\n".join(result)

# print(translator.translate(txt, src='en', dest='ko').text)


# # In[102]:


# print(translate(txt))


# # In[77]:





# # In[ ]:





# # In[ ]:

