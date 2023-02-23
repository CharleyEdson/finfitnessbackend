from django.urls import path
from cashflow import views

urlpatterns = [

    path('getcashflow/', views.get_cash_flow),
    path('deletenetcashflow/<int:pk>/', views.delete_net_cash_flow),
    path('historicalnetcashflow/', views.get_historical_net_cash_flow),


]