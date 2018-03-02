from django.contrib.auth import authenticate

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

import datetime
from pytz import utc
from ..serializers import LoginSerializer



class LoginView(ObtainAuthToken):
    def post(self, request, format=None, **kwargs):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer['email'].value, password=serializer['password'].value)
            print(serializer['email'].value, " ", serializer['password'].value)
            if user:
                token, _ = Token.objects.get_or_create(user=user)

                if not _:
                    token.created = datetime.datetime.utcnow().replace(tzinfo=utc)

                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_auth_token = LoginView.as_view()

