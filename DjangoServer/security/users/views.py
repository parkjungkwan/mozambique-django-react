from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from security.users.repositories import UserRepository
from security.users.serializers import UserSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def signup(request): return UserSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_user(request): return UserSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_user(request): return UserSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_user_by_id(request): return UserRepository().find_by_id(request.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login(request.data)


