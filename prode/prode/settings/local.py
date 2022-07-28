import os
from .base import *

STATICFILES_DIRS = (
	os.path.join(os.path.dirname(BASE_DIR),"static"),
	)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'prode_new',
        'USER': 'root',
        'PASSWORD': 'Martes.12',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



