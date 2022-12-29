from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.users.models import User
from security.users.serializers import UserSerializer
from security.users.services import UserService

@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request):
    if request.method == "GET":
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(f"로그인 정보: {request.data}")
        loginInfo = request.data
        loginUser = User.objects.get(user_email=loginInfo['user_email'])
        print(f"해당 email 을 가진  User: {loginUser}")
        if loginUser["password"] == loginInfo["password"]:
            serializer = UserSerializer(loginUser, many=False)
            print(f"")
            token = Token.objects.create(user=serializer)
            print(f" 토큰값 : {token}")
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
    except:
        return Response("LOGIN FAIL")


