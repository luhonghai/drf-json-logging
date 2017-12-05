import logging
import uuid

from django.conf import settings

from request_id.middleware import RequestIdMiddleware
from request_id import release_local, local


logger = logging.getLogger(__name__)


class RequestLoggingIdMiddleware(RequestIdMiddleware):
    pass
