import os
import environ


env = environ.Env()
environ.Env.read_env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = False

DATABASES = {
    'default': {
       'ENGINE': 'django.contrib.gis.db.backends.spatialite',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ELASTICSEARCH_DSL={
    'default': {
        'hosts': env('ELASTIC_HOST')
    },
}

'''
ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}
'''