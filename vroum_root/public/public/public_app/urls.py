from django.urls import path

from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("voiture/<int:voiture_id>/", views.details_car, name="details_car"),
    path("garage/<int:garage_id>/", views.details_garage, name="details_garage"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('reservation/', views.reservation_create, name='reservation_create'),
]
