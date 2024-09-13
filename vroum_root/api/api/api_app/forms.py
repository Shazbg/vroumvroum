# forms.py
from django import forms
from .models import Cle, Voiture

class CleForm(forms.ModelForm):
    class Meta:
        model = Cle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclure les voitures qui ont déjà une clé associée
        self.fields['voiture'].queryset = Voiture.objects.filter(cle__isnull=True)
