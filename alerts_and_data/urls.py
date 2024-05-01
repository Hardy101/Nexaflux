from django.urls import path
from . import views

app_name = 'alerts_and_data'
urlpatterns = [
    path('coinlist/', views.CoinCreate.as_view(), name='coinlistapi'),
    path('coins/<str:coinSymbol>/', views.CoinRetrieve.as_view(), name='retrievecoin'),
    path('alerts/', views.AlertsRetrieve.as_view(), name='getalert'),
] 