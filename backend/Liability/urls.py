from django.urls import path
from Liability import views

urlpatterns = [
    path('', views.liabilityinfo),
    path('<int:pk>/', views.edit_liabilities),
]