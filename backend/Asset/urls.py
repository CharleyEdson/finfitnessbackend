from django.urls import path
from Asset import views

urlpatterns = [
    path('', views.assetinfo),
    path('<int:pk>/', views.edit_assets)

]