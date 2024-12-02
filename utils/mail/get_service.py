from django.conf import settings
from utils.mail.base_service import BaseService


def get_service(service_name=settings.DEFAULT_MAIL_SERVICE, request=None) -> BaseService:
    if request is not None and request.headers.get("user-agent", "").startswith("MailerSend"):
        service_name = 'mailersend'

    if service_name == 'mailersend':
        from utils.mail.mailersend_service import MailerSendService
        return MailerSendService()
    else:
        raise Exception('Service not found')
