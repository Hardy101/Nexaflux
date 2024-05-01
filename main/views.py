from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAlertForm, AddCoinForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    form = CreateAlertForm()
 