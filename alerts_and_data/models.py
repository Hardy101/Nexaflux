from django.db import models
# -


# Create your models here.   
class Alert(models.Model):
    coin = models.CharField(max_length=10, null=False)
    target_type = models.CharField(max_length=10, null=False)
    target = models.DecimalField(max_digits=10, decimal_places=4 , null=False)
    date_created = models.CharField(max_length=20, null=False)


class Coin(models.Model):
    coinName = models.CharField(max_length=100)
    coinSymbol = models.CharField(max_length=20)