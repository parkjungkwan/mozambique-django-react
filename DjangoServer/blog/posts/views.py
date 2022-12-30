from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.posts.repository import PostRepository
from blog.posts.serializers import PostSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_post(request): return PostSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_post(request): return PostSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_post(request): return PostSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def post_list(request): return PostRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_post_by_id(request): return PostRepository().find_by_id(request.data)

