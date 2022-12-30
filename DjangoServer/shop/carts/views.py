from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.carts.repository import CartRepository
from shop.carts.serializers import CartSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_cart(request): return CartSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_cart(request): return CartSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_cart(request): return CartSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def cart_list(request): return CartRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_cart_by_id(request): return CartRepository().find_by_id(request.data)

