from django.urls import path
from netWorth import views

urlpatterns = [
    path('', views.calculate_net_worth),
    path('getnetworth/', views.get_net_worth),
    path('deletenetworth/<int:pk>/', views.delete_net_worth),
    path('historicalnetworth/', views.get_historical_net_worth),
    path('onceaday/', views.calculate_net_worth_once_a_day),


]