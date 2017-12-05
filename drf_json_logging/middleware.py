import logging
import uuid

from django.conf import settings

from request_id.middleware import RequestIdMiddleware


logger = logging.getLogger(__name__)


class RequestLoggingIdMiddleware(RequestIdMiddleware):
    pass
