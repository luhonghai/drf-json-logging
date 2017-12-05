import logging
import uuid

from django.conf import settings

from request_id.middleware import RequestIdMiddleware
from request_id import local, release_local

logger = logging.getLogger(__name__)


class RequestLoggingIdMiddleware(RequestIdMiddleware):

    def process_response(self, request, response):

        if 'favicon' in request.path:
            return response

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'pk', None) or getattr(user, 'id', None)

        message = 'method=%s path=%s status=%s'
        args = (request.method, request.path, response.status_code)

        if user_id:
            message += ' user=%s'
            args += (user_id,)

        logger.info(message, *args)

        release_local(local)
        return response
