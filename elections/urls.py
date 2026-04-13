from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('polling-unit/', views.polling_unit_results),
    path('lga-results/', views.lga_results),
    path('add-results/', views.add_results),
]