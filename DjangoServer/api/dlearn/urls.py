from django.urls import re_path as url
from api.dlearn.iris import view as iris_view
from api.dlearn.fashion import view as fashion_view

urlpatterns = [
    url(r'iris', iris_view.iris),
    url(r'fashion', fashion_view.fashion)
]
