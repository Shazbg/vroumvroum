from django.contrib import admin
from .forms import CleForm
from .models import *


admin.site.register(Garage)
admin.site.register(Voiture)

class CleAdmin(admin.ModelAdmin):
    form = CleForm

admin.site.register(Cle, CleAdmin)