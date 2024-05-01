from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CreateAlertForm

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
            

