from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.tags.repository import TagRepository
from blog.tags.serializers import TagSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_tag(request): return TagSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_tag(request): return TagSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_tag(request): return TagSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def tag_list(request): return TagRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_tag_by_id(request): return TagRepository().find_by_id(request.data)

