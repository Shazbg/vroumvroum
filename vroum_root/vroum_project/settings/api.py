from .base import *

INSTALLED_APPS += [
    'api_app',  # Ton application 'api'
]

ROOT_URLCONF = 'vroum_project.api_app-urls'

# Autres configurations spécifiques à api