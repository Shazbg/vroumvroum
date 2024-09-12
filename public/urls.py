from django.urls import path

from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("voiture/<int:voiture_id>/", views.details_car, name="details_car"),
    path("garage/<int:garage_id>/", views.details_garage, name="details_garage"),
]
