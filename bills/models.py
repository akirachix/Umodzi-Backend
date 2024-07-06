from django.db import models

# Create your models here.

class Bills(models.Model):
    bill_payment_id=models.SmallIntegerField()
    user_id=models.SmallIntegerField()
    provider_id=models.SmallIntegerField()
    amount=models.SmallIntegerField()
    time_stamp=models.DateField()

def _str_(self):
    return f'{bill_payment_id} {user_id}'