from django.urls import path
from Expense import views

urlpatterns = [
    path('', views.expenseinfo),
    path('<int:pk>/', views.edit_expenses)
]