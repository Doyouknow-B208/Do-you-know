from rest_framework.decorators import api_view
from rest_framework.response import Response
from googletrans import Translator

@api_view(['GET'])
def translate(request,keyword):
    translator = Translator()
    data = translator.translate('hi'),
    print(data)
    return Response(data)