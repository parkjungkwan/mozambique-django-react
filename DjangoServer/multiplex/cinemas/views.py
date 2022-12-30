from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.cinemas.repository import CinemaRepository
from multiplex.cinemas.serializers import CinemaSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def cinema_list(request): return CinemaSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def cinema_update(request): return CinemaSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def cinema_delete(request): return CinemaSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def cinema_list(request): return CinemaRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def user_detail(request): return CinemaRepository().find_by_id(request.data)


