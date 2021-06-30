import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "kaiseifes_150th_backend",

    }
}

ALLOWED_HOSTS = []

DEBUG = True
