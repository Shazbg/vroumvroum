from django.shortcuts import render,get_object_or_404

from api.models import Voiture,Garage
# Create your views here.


def index(request):
    voiture_list = Voiture.objects.order_by("immat")
    garage_list = Garage.objects.order_by("nom")
    context = {"voiture_list": voiture_list,"garage_list": garage_list}
    return render(request, "public/index.html", context)

def details_car(request,voiture_id):
   voiture =  get_object_or_404(Voiture,id=voiture_id)
   context = {"voiture": voiture}
   return render(request,"public/details_car.html",context)

def details_garage(request,garage_id):
    garage = get_object_or_404(Garage,id=garage_id)
    context = {"garage": garage}
    return render(request,"public/details_garage.html",context)
