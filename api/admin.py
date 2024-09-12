from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cle)
admin.site.register(Garage)
admin.site.register(Voiture)