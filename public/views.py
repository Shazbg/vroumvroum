from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'public/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, "Erreur de connexion. Veuillez vérifier vos identifiants.")
    else:
        form = AuthenticationForm()
    return render(request, 'public/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')

