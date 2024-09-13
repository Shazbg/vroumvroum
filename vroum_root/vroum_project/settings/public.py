from .base import *

INSTALLED_APPS += [
    'public_app',  # Ton application 'public'
]

ROOT_URLCONF = 'vroum_project.public_app-urls'

# Autres configurations spécifiques à public