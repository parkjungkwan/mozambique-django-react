from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from security.users.repositories import UserRepository
from security.users.serializers import UserSerializer


@api_view(['POST','PUT','PATCH','DELETE','GET'])
@parser_classes([JSONParser])
def user(request):
    if request.method == "POST":
        return UserSerializer().create(request.data)
    elif request.method == "GET":
        return UserRepository().find_by_id(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return UserSerializer().update(request.data)
    elif request.method == "DELETE":
        return UserSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().get_all()

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login(request.data)


