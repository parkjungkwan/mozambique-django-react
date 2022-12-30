from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.comments.repository import CommentRepository
from blog.comments.serializers import CommentSerializer
from blog.posts.repository import PostRepository
from blog.posts.serializers import PostSerializer
from blog.tags.repository import TagRepository
from blog.tags.serializers import TagSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_tag(request): return TagSerializer().create()

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_tag(request): return TagSerializer().update()

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_tag(request): return TagSerializer().delete()

@api_view(['GET'])
@parser_classes([JSONParser])
def tag_list(request): return TagRepository().get_all()

@api_view(['GET'])
@parser_classes([JSONParser])
def find_tag_by_id(request): return TagRepository().find_by_id()

