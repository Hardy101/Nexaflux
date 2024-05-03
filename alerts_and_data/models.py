from django.db import models
# -
from datetime import datetime
import django
import django.utils
import django.utils.timezone

# Create your models here.   
class Alert(models.Model):
    coin = models.CharField(max_length=10, null=False)
    target_type = models.CharField(max_length=10, null=False)
    target = models.DecimalField(max_digits=10, decimal_places=4 , null=False)
    date_created = models.CharField(max_length=20, null=False)
    validuntil = models.DateTimeField(default=django.utils.timezone.now)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')


# Coin list model
class Coin(models.Model):
    coinName = models.CharField(max_length=100)
    coinSymbol = models.CharField(max_length=20)
