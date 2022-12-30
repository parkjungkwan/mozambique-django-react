from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.users.models import User
from security.users.serializers import UserSerializer
from security.users.services import UserService


class UserRepository(object):

    def __init__(self):
        print(" UserRepository 객체 생성 ")

    def get_all(self):
        return Response(UserSerializer(User.objects.all(), many=True).data)

    def get_by_id(self):
        return Response(UserSerializer(User.objects.all(), many=True).data)



    def login(self, kwargs):
        loginUser = User.objects.get(user_email=kwargs['user_email'])
        if loginUser.password == kwargs["password"]:
            dbUser = User.objects.all().filter(id=loginUser.id).values()[0]
            serializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return JsonResponse({"data": "WRONG_PASSWORD"})