# File sets up the django environment, used by other scripts that need to
# execute in django land
import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "lumberjack"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "lumberjack",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
        LOGGING={
            "version": 1,
            "handlers": {
                "mail_admins": {
                    "level": "INFO",
                    "class": "lumberjack.handlers.ExceptionHandler",
                }
            },
            "loggers": {
                "lumberjack": {
                    "handlers": ["mail_admins"],
                    "propagate": True,
                },
                "django.request": {
                    "handlers": ["mail_admins"],
                    "level": "ERROR",
                    "propagate": False,
                },
            },
        },
        LUMBERJACK={
            "LUMBERJACK_URL": "https://lumberjack-server-url.com/api/",
            "PROJECT_NAME": "PROJECT_NAME",
            "APPENV": "PRODUCTION",
            "APP_LOCATION": "LONDON",
        }
    )
    django.setup()
