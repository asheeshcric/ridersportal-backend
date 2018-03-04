from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from ..models.user_details import UserDetails, User

class RegisterView(ObtainAuthToken):
    def post(self, request, format=None, **kwargs):
        # print(request.data)
        try:
            details = request.data
            user, created_status = User.objects.get_or_create(username=details['email'])
            print(created_status)
            if not created_status:
                return Response({'User Already Exists'})
            user.first_name = details['fname']
            user.last_name = details['lname']
            user.email = details['email']
            user.password = make_password(details['password'])
            user.is_active = 1
            user.is_staff = 1
            user.is_superuser = 0
            user.save()
            userdetails = UserDetails.objects.create(
                address=details['address'],
                bike_model=details['bike_model'],
                contact=details['contact'],
                user=user
            )
            if details['bike_model']:
                userdetails.own_bike = 1
                userdetails.save()
            return Response({'User Created Successfully!'})

        except Exception as error:
            return Response({'Bad Request - Exception Occured!'})



register_user = RegisterView.as_view()