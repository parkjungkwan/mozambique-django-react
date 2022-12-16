from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from api.dlearn.fashion_service import FashionService


@api_view(['GET'])
def fashion(request, id):
    print(f"######## React ID is {id} ########")
    service = FashionService()
    resp = "TEST SUCCESS !!"
    return JsonResponse({'result':resp})