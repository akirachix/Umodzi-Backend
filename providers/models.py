from django.db import models
from users.models import Users

# Create your models here.

class Providers(models.Model):
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    provider_name=models.CharField(max_length=30)
    billing_details=models.CharField(max_length =60)

def _str_(self):
    return f'{provider_name} {billing_details}'