DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mlpweb',
        'USER': 'mlp',
        'PASSWORD': '|c0#+R01U$0u1',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TIME_ZONE = 'Europe/Kiev'
