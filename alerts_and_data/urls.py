from django.urls import path, re_path
from . import views

app_name = 'alerts_and_data'
urlpatterns = [
    path('coinlist/', views.CoinList.as_view(), name='coinlistapi'),
    path('alerts/', views.AlertsRetrieve.as_view(), name='getalert'),
    path('coin/', views.CoinSearch.as_view(), name='coinsearch'),
    path('deletecoin/<str:coinSymbol>', views.DeleteCoinView.as_view(), name='deletecoin'),
] 