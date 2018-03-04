from django.urls import path

from ..views.login_view import obtain_auth_token
from ..views.register_view import register_user

urlpatterns = [
    path('login', obtain_auth_token),
    path('register', register_user),
]