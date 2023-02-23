from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_info),
    path('currentbudget/', views.current_budget_info),
    path('<int:pk>/', views.edit_budget),

]