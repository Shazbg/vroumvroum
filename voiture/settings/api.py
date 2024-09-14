from .base import *

INSTALLED_APPS += [
    'api',  # Ton application 'api'
]

ROOT_URLCONF = 'voiture.api-urls'

# Autres configurations spécifiques à api