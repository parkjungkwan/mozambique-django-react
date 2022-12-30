from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.orders.repository import OrderRepository
from shop.orders.serializers import OrderSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_order(request): return OrderSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_order(request): return OrderSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_order(request): return OrderSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def order_list(request): return OrderRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_order_by_id(request): return OrderRepository().find_by_id(request.data)

