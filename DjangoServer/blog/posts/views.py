from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.comments.repository import CommentRepository
from blog.comments.serializers import CommentSerializer
from blog.posts.repository import PostRepository
from blog.posts.serializers import PostSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_post(request): return PostSerializer().create()

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_post(request): return PostSerializer().update()

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_post(request): return PostSerializer().delete()

@api_view(['GET'])
@parser_classes([JSONParser])
def post_list(request): return PostRepository().get_all()

@api_view(['GET'])
@parser_classes([JSONParser])
def find_post_by_id(request): return PostRepository().find_by_id()

