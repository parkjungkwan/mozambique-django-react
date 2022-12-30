from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.products.repository import ProductRepository
from shop.products.serializers import ProductSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_product(request): return ProductSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_product(request): return ProductSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_product(request): return ProductSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def product_list(request): return ProductRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_product_by_id(request): return ProductRepository().find_by_id(request.data)

