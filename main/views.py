from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CreateAlertForm
import requests
from datetime import datetime, timezone, timedelta
# Tasks


# VARIABLES
ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    form = CreateAlertForm()
    context = {'form': form}
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
            

def check_alerts(request):
    response = requests.get(ENDPOINT)
    alert_list = response.json()

    # Process the fetched data
    current_time = datetime.now()
    for alert_data in alert_list:
        valid_until = datetime.strptime(alert_data['validuntil'], '%Y-%m-%d %H:%M:%S')
        if current_time < valid_until:
            return HttpResponse('True')
        else:
            return HttpResponse('False')
    