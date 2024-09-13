from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from api.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    voiture_list = Voiture.objects.order_by("immat")
    garage_list = Garage.objects.order_by("nom")
    context = {"voiture_list": voiture_list,"garage_list": garage_list}
    return render(request, "public/index.html", context)

def details_car(request,voiture_id):
   voiture =  get_object_or_404(Voiture,id=voiture_id)
   context = {"voiture": voiture, 'reservation_active': reservation_active}
   reservation_active = Reservation.objects.filter(voiture=voiture, statut='confirmee').exists()
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


def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Associe la réservation à l'utilisateur connecté (si nécessaire)
            reservation.save()
            messages.success(request, "Votre réservation a été effectuée avec succès.")
            return redirect('index')  # Redirige vers la page d'accueil ou une page de confirmation
        else:
            messages.error(request, "Erreur lors de la réservation. Veuillez vérifier les informations.")
    else:
        form = ReservationForm()

    context = {"form": form, "voitures": Voiture.objects.all(),}
    return render(request, 'public/reservation.html', context)

