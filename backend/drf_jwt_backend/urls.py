"""drf_jwt_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/cars/', include('cars.urls')),
    path('api/userinfo/', include('userInfo.urls')),
    path('api/assets/', include('Asset.urls')),
    path('api/liabilities/', include('Liability.urls')),
    path('api/income/', include('Income.urls')),
    path('api/expenses/', include('Expense.urls')),
    path('api/networth/', include('netWorth.urls')),
    path('api/currentincexp/', include('currentincexp.urls')),
    path('api/cashflow/', include('cashflow.urls')),
    path('api/budget/', include('budget.urls')),
]
