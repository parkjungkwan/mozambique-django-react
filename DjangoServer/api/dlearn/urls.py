from django.urls import re_path as url
from api.dlearn import iris_view
from api.dlearn import fashion_view

urlpatterns = [
    url(r'iris', iris_view.iris),
    url(r'fashion', fashion_view.fashion)
]
