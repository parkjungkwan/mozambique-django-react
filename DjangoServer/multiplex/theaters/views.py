from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.theater_tickets.repository import TheaterTicketRepository
from multiplex.theater_tickets.serializers import TheaterTicketSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_theater(request): return TheaterTicketSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_theater(request): return TheaterTicketSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_theater(request): return TheaterTicketSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def theater_list(request): return TheaterTicketRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_theater_by_id(request): return TheaterTicketRepository().find_by_id(request.data)

