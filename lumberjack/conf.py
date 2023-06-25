from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    LUMBERJACK_URL = settings.LUMBERJACK["LUMBERJACK_URL"]
    PROJECT_NAME = settings.LUMBERJACK["PROJECT_NAME"]
    APPENV = settings.LUMBERJACK["APPENV"]
    APP_LOCATION = settings.LUMBERJACK["APP_LOCATION"]
except Exception as e:
    raise ImproperlyConfigured(f"Problem with Lumberjack settings:\n\n{e}")
