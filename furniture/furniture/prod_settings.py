import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure21w3-z$#k==ur@0_21j@l&r3fsajpx+bfrus!(8u*el-*9q9&xfdwu=72!32tgfx'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '185.119.57.72', 'art-mebel-abh.com' ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'furniture',
        'USER': 'denis',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



STATIC_ROOT = os.path.join(BASE_DIR, "static")

