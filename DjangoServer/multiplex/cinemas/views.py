from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import datetime

from multiplex.cinemas.repository import CinemaRepository
from multiplex.cinemas.serializers import CinemaSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def cinema_list(request): return CinemaSerializer().create()

@api_view(['PUT'])
@parser_classes([JSONParser])
def cinema_update(request): return CinemaSerializer().update()

@api_view(['DELETE'])
@parser_classes([JSONParser])
def cinema_delete(request): return CinemaSerializer().delete()

@api_view(['GET'])
@parser_classes([JSONParser])
def cinema_list(request): return CinemaRepository().get_all()

@api_view(['GET'])
@parser_classes([JSONParser])
def user_detail(request): return CinemaRepository().find_by_id()

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return CinemaRepository().login()
