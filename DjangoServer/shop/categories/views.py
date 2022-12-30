from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.categories.repository import CategoryRepository
from shop.categories.serializers import CategorySerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_category(request): return CategorySerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_category(request): return CategorySerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_category(request): return CategorySerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def category_list(request): return CategoryRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_category_by_id(request): return CategoryRepository().find_by_id(request.data)

