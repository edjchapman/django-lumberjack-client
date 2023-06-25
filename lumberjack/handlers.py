import logging.config  # needed when logging_config doesn't start with logging.config

import requests
from django.conf import settings
from django.utils import timezone
from django.views.debug import ExceptionReporter
from rest_framework.renderers import JSONRenderer

from .conf import PROJECT_NAME, APPENV, APP_LOCATION, LUMBERJACK_URL
from .serializers import ExceptionSerializer

logger = logging.getLogger()


class ExceptionHandler(logging.Handler):
    """
    An exception log handler that gathers data to be posted to Lumberjack.
    """

    def __init__(self):
        super().__init__()

    def emit(self, record):
        """
        Gather data required for the record and post to Lumberjack.
        Overrides emit method of parent Handler.

        If the request is passed as the first argument to the log record,
        request data will be provided as part of the record.
        """
        try:
            request = record.request
            subject = "%s (%s IP): %s" % (
                record.levelname,
                (
                    "internal"
                    if request.META.get("REMOTE_ADDR") in settings.INTERNAL_IPS
                    else "EXTERNAL"
                ),
                record.getMessage(),
            )
        except Exception as e:
            logger.exception(
                f"Unexpected error raised when emitting record to Lumberjack: {e}"
            )
            subject = "%s: %s" % (record.levelname, record.getMessage())
            request = None
        data = self.gather_data(request=request, subject=subject, record=record)
        serialized_data = ExceptionSerializer(data).data
        json_data = JSONRenderer().render(serialized_data)
        self.post_record(data=json_data)

    @staticmethod
    def get_report(request, record):
        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)
        report = ExceptionReporter(request, *exc_info)
        return report

    @staticmethod
    def format_subject(subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace("\n", "\\n").replace("\r", "\\r")

    def gather_data(self, request, subject, record):
        report = self.get_report(request, record)
        return {
            "project_name": PROJECT_NAME,
            "appenv": APPENV,
            "app_location": APP_LOCATION,
            "created_at": timezone.localtime(),
            "level": record.levelno,
            "subject": self.format_subject(subject),
            "logger_name": record.name,
            "path_name": record.pathname,
            "func_name": record.funcName,
            "line_num": record.lineno,
            "traceback": report.get_traceback_text(),
        }

    @staticmethod
    def post_record(data):
        try:
            r = requests.post(
                f"{LUMBERJACK_URL}/api/logs/",
                data=data,
                timeout=0.5,
                headers={
                    "Content-type": "application/json",
                    "Accept": "application/json",
                },
            )
            r.raise_for_status()
        except requests.exceptions.ReadTimeout:
            logger.info(
                "Request exceeded 0.5s timeout when posting record to Lumberjack"
            )
        except Exception as e:
            logger.info(f"Exception thrown when posting record to Lumberjack: {e}")
