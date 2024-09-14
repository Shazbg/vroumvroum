from .base import *

INSTALLED_APPS += [
    'public',  # Ton application 'public'
]

ROOT_URLCONF = 'voiture.public-urls'

# Autres configurations spécifiques à public