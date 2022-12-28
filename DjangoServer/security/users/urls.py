from django.urls import re_path as url
from security.users import views

urlpatterns = [
    url(r'user-list', views.user_list),
    url(r'login', views.login)
]
