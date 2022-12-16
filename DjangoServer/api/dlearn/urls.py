from django.urls import path, re_path as url
from api.dlearn import iris_view
from api.dlearn import fashion_view

urlpatterns = [
    url(r'iris', iris_view.iris),
    path('fashion/<int:id>', fashion_view.fashion)
]
