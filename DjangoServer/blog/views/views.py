from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.views.repository import ViewRepository
from blog.views.serializers import ViewSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_view(request): return ViewSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_view(request): return ViewSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_view(request): return ViewSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def view_list(request): return ViewRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_view_by_id(request): return ViewRepository().find_by_id(request.data)

