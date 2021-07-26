import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = False

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}