from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    contact = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    own_bike = models.BooleanField(default=False)
    bike_model = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
