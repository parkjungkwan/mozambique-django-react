from django.http import JsonResponse
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

def login(request):
    pass


