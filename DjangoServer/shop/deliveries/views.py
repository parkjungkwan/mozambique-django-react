from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from shop.deliveries.repository import DeliveryRepository
from shop.deliveries.serializers import DeliverySerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_delivery(request): return DeliverySerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_delivery(request): return DeliverySerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_delivery(request): return DeliverySerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def delivery_list(request): return DeliveryRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_delivery_by_id(request): return DeliveryRepository().find_by_id(request.data)

