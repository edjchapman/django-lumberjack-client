import logging

from django import http

logger = logging.getLogger(__name__)


def handled_500_error(request: http.HttpRequest):
    """
    Trigger error using the logger to validate logging configuration
    and  that exception details are emitted to the Lumberjack server correctly.
    """
    _ = request
    try:
        1 / 0
    except Exception as e:
        logger.exception(e)
    return http.HttpResponse("Handled 500 error")


def unhandled_500_error(request: http.HttpRequest):
    """
    Trigger error outside exception clause to validate
    that unhandled exception details are emitted to the Lumberjack server correctly.
    """
    _ = request
    _ = 1 / 0
    return http.HttpResponse("Unhandled 500 error")
