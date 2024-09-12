from django.urls import path
from .views import garage_list, voiture_list, cle_list

urlpatterns = [
    path('garages/', garage_list, name='garage-list'),
    path('voitures/', voiture_list, name='voiture-list'),
    path('cles/', cle_list, name='cle-list'),
]