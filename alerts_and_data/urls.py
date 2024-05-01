from django.urls import path, re_path
from . import views

app_name = 'alerts_and_data'
urlpatterns = [
    path('coinlist/', views.CoinList.as_view(), name='coinlistapi'),
    path('coins/<str:coinSymbol>/', views.CoinRetrieve.as_view(), name='retrievecoin'),
    # re_path('coins/', views.CoinRetrieve.as_view()),
    path('alerts/', views.AlertsRetrieve.as_view(), name='getalert'),
] 