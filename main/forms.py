from django import forms
from django.forms.widgets import TextInput, NumberInput
from alerts_and_data.models import Alert

# - Create Alert form
class CreateAlertForm(forms.ModelForm):
    coin = forms.CharField(widget=TextInput)
    target_type = forms.CharField(widget=TextInput)
    target = forms.CharField(widget=NumberInput)
    date_created = forms.CharField(widget=TextInput)

    class Meta:
        object = Alert
        fields = ['coin', 'target_type', 'target', 'date_created']


# - Add coin form
# class AddCoinForm(forms.ModelForm):
#     coinName = forms.CharField(widget=TextInput)
#     coinSymbol = forms.CharField(widget=TextInput)

#     class Meta:
#         object = Coin
#         fields = ['coinName', 'coinSymbol']
