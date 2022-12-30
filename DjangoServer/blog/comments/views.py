from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.comments.repository import CommentRepository
from blog.comments.serializers import CommentSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_comment(request): return CommentSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_comment(request): return CommentSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_comment(request): return CommentSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def comment_list(request): return CommentRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_comment_by_id(request): return CommentRepository().find_by_id(request.data)

