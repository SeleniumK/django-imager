from settings import *
import os

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = [
    '.us-west-2.compute.amazonaws.com',
    'localhost',
]
