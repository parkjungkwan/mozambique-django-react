from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.showtimes.repository import ShowtimeRepository
from multiplex.showtimes.serializers import ShowtimeSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_showtime(request): return ShowtimeSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_showtime(request): return ShowtimeSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_showtime(request): return ShowtimeSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def showtime_list(request): return ShowtimeRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_showtime_by_id(request): return ShowtimeRepository().find_by_id(request.data)

