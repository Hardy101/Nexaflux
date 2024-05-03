from django.db import models
# -
from datetime import datetime

# Create your models here.   
class Alert(models.Model):
    coin = models.CharField(max_length=10, null=False)
    target_type = models.CharField(max_length=10, null=False)
    target = models.DecimalField(max_digits=10, decimal_places=4 , null=False)
    date_created = models.CharField(max_length=20, null=False)
    validuntil = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M"))


# Coin list model
class Coin(models.Model):
    coinName = models.CharField(max_length=100)
    coinSymbol = models.CharField(max_length=20)
