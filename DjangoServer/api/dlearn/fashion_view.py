import json

from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework import serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from api.dlearn.fashion_service import FashionService


@api_view(["GET"])
def fashion(request, id):
    print(" ######## GET at Here ! ########  ")
    # body = request.body  # byte string of JSON data
    # print(f" ######## request.body is {body} ########  ")
    # data = json.loads(body)  # json to dict
    # print(request.headers)  # request의 header 정보
    # print(request.content_type)  # application/json
    print(f"######## React ID is {request.GET['id']} ########")
    resp = FashionService().service_model(int(request.GET['id']))
    return JsonResponse({'result': resp})

@api_view(["POST"])
def fashion(request):
    print(" ######## POST at Here ! ########  ")
    body = request.body  # byte string of JSON data
    print(f" ######## request.body is {body} ########  ")
    data = json.loads(body)  # json to dict
    print(request.headers)  # request의 header 정보
    print(request.content_type)  # application/json
    print(f"######## React ID is {data} ########")
    resp = FashionService().service_model(int(data['id']))
    return JsonResponse({'result': resp})