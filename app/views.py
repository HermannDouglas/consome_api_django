from django.shortcuts import render
from django.http import HttpResponse
from .models import Local
from .serializers import LocalSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import requests
import io
import json

@csrf_exempt
def local(request):
    # if request.method == "POST":
        response = requests.get('http://127.0.0.1:8000/local/')
        json_data = response.json()
        print(json_data)

        json_string = json.dumps(json_data)
        # print(json_string)

        stream = io.BytesIO(json_string.encode())
        # print(stream)
        
        data = JSONParser().parse(stream)
        print(data)

        serializer = LocalSerializer(data = data, many=True)
        # print(serializer)
        
        # verifica_validade = serializer.is_valid()
        # print(verifica_validade)
        if serializer.is_valid():
            # Os dados são válidos, você pode salvar o objeto
            serializer.save()
        else:
            # Os dados não são válidos, imprima os erros de validação
            print("\n")
            print(serializer.errors)
        # print("\n")
        # print(teste)
        # serializer.validated_data


        return HttpResponse("ok")
