from django.db import models

# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact_details=models.CharField(max_length=30)
    balance=models.SmallIntegerField()

def _str_(self):
    return f'{self.user_id} {self.name}'
