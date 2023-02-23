from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinformation),
    path('<int:pk>/', views.edit_user_info),

]