from django.db import models

# Create your models here.

class Transaction(models.Model):
    user_id=models.SmallIntegerField()
    transaction_type=models.CharField(max_length=50)
    amount=models.SmallIntegerField()
    status=models.CharField(max_length=40)
    time_stamp=models.DateField()

def _str_(self):
    return f'{user_id} {transaction_type}'
