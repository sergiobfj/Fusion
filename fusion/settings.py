"""
Django settings for fusion project.
"""

from pathlib import Path
import os
import sys
import dj_database_url

# -----------------------------------------------------------
# 🚀 Caminhos base
# -----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------------------------------------
# 🔐 Configurações básicas
# -----------------------------------------------------------
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-cx(%l@ilr^q35npfu1%5_*zk5ryg@8+4q%hni(-7snm^_g+cj%"
)

DEBUG = True

# 🔹 Aceita tudo localmente e *.vercel.app no deploy
ALLOWED_HOSTS = ['*', '.vercel.app']


# -----------------------------------------------------------
# 📦 Aplicativos instalados
# -----------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps do projeto
    'core',
]


# -----------------------------------------------------------
# ⚙️ Middleware
# -----------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise para servir arquivos estáticos no deploy
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------------------------------------
# 🌐 URLs e WSGI
# -----------------------------------------------------------
ROOT_URLCONF = 'fusion.urls'
WSGI_APPLICATION = 'fusion.wsgi.application'


# -----------------------------------------------------------
# 🧱 Templates
# -----------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# -----------------------------------------------------------
# 🗄️ Banco de Dados (Neon + fallback local)
# -----------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv(
            'DATABASE_URL',
            f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
        ),
        conn_max_age=600,
    )
}


# -----------------------------------------------------------
# 🔐 Validações de senha
# -----------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------------------------------------
# 🌍 Internacionalização
# -----------------------------------------------------------
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# -----------------------------------------------------------
# 🖼️ Arquivos estáticos e mídia
# -----------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# -----------------------------------------------------------
# 📧 E-mail (modo teste)
# -----------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# -----------------------------------------------------------
# 🧠 Diagnóstico para logs do Vercel
# -----------------------------------------------------------
print("✅ Django settings carregado com sucesso", file=sys.stderr)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
