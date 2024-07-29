from django.db import models
from users.models import Users

# Create your models here.

class Bills(models.Model):
    bill_payment_id=models.SmallIntegerField()
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    provider_id=models.SmallIntegerField()
    amount=models.SmallIntegerField()
    time_stamp=models.DateField()

def _str_(self):
    return f'{self.bill_payment_id} {self.user_id}'