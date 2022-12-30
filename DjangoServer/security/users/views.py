from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from security.users.repositories import UserRepository
from security.users.serializers import UserSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def user_list(request): return UserSerializer().create()

@api_view(['PUT'])
@parser_classes([JSONParser])
def user_update(request): return UserSerializer().update()

@api_view(['DELETE'])
@parser_classes([JSONParser])
def user_delete(request): return UserSerializer().delete()

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().get_all()

@api_view(['GET'])
@parser_classes([JSONParser])
def user_detail(request): return UserRepository().find_by_id()

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login()


