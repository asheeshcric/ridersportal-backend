from django.urls import path

from ..views.login_view import obtain_auth_token

urlpatterns = [
    path('login', obtain_auth_token),
]