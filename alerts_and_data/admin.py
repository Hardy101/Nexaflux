from django.contrib import admin
# -
from .models import Alert, Coin


# Register your models here.
class AlertAdmin(admin.ModelAdmin):
    list_display = ['coin', 'target_type', 'target', 'date_created']


class CoinAdmin(admin.ModelAdmin):
    list_display = ['id', 'coinName', 'coinSymbol']

admin.site.register(Alert, AlertAdmin)
admin.site.register(Coin, CoinAdmin)