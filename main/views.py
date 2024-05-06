from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CreateAlertForm
import requests
from datetime import datetime, timezone, timedelta
from alerts_and_data import models as apimodels
# Tasks


# VARIABLES
ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    form = CreateAlertForm()
    alertlist = apimodels.Alert.objects.all()
    context = {'form': form, 'alertlist': alertlist}
    return render(request, 'dashboard.html', context=context)


def addAlert(request):
    if request.method == 'POST':
        form = CreateAlertForm(request.POST)
        if form.is_valid():
            alert = form.save()
            return JsonResponse({'status': 'success', 'alert': alert.id})
        else:
            error = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': error}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
            
    