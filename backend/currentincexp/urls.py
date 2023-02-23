from django.urls import path
from currentincexp import views

urlpatterns = [
    path('', views.calculate_cash_flow),
    # path('getcurrents/', views.get_cash_flow),
    # path('deletecurrents/<int:pk>/', views.delete_currents),
    path('historicalcurrents/', views.get_historical_curents),
    path('createcurrents/', views.create_currents),
    path('editcurrents/<int:pk>/', views.edit_currents),


]