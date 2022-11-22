from importlib.resources import contents
from unicodedata import name
from rest_framework.decorators import api_view
from googletrans import Translator
from rest_framework.response import Response

from .models import DykclubTwitter
from .models import News
from django.db.models import Q

@api_view(['GET'])
def usallyview(request, keyword, num):
    if keyword == '손흥민':
        key =  1
    elif keyword == '김연아':
        key = 2
    elif keyword == '김연경':
        key = 3
    elif keyword == '이상한 변호사 우영우':
        key = 4
    elif keyword == '태양의 후예':
        key = 5
    elif keyword == '오징어 게임':
        key = 6
    elif keyword == '기생충':
        key = 7
    elif keyword == '올드보이':
        key = 8
    elif keyword == '부산행':
        key = 9
    elif keyword == 'BTS':
        key = 10
    elif keyword == '싸이':
        key = 11
    elif keyword == '이정재':
        key = 12


    key = DykclubTwitter.objects.filter(dykclub_id=key).values('content')
    sentence = key[num]['content']
    translator = Translator()
    result = translator.translate(sentence, dest='ko').text
    
    return Response(result)


@api_view(['GET'])
def detailview(request, keyword, nation_code):
    translator = Translator()
    if nation_code == 'en':
        result = translator.translate(keyword, src='ko', dest='en').text
    elif nation_code == 'ja':
        result = translator.translate(keyword, src='ko', dest='ja').text
    elif nation_code == 'vi':
        result = translator.translate(keyword, src='ko', dest='vi').text
    elif nation_code == 'id':
        result = translator.translate(keyword, src='ko', dest='id').text
    elif nation_code == 'pt':
        result = translator.translate(keyword, src='ko', dest='pt').text
    return Response(result)




@api_view(['GET'])
def newslistview(requrst,keyword,nation_code):
    key = News.objects.filter(Q(keyword=keyword) & Q(nation_id=nation_code)).values()
    return Response(key)