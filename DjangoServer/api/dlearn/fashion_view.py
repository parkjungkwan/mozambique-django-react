from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from api.dlearn.fashion_service import FashionService


@api_view(['POST'])
@parser_classes([JSONParser])
def fashion(request):
    data = request.data

    service = FashionService()
    test_num = tf.constant(float(data['testNum']))
    service.plot_image(test_num)
    plt.subplot(1, 2, 2)
    service.plot_value_array(test_num)
    plt.show()
    resp = ""
    return JsonResponse({'result':resp})