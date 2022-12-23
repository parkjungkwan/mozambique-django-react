from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
from basic.algorithms.lambdas import lambda_time

@api_view(['GET'])
def hello(request):
    print('####################################################################')
    print(f'############ Server Started At {lambda_time} ##########')
    print('####################################################################')
    return Response({'message': "Server Started !"})