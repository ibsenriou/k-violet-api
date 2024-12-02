from mailersend import emails
import requests
from utils.mail.base_service import BaseService, BaseResponse
from utils.html_to_text import parse_html
from django.conf import settings

STATUS_MAPPING = {
    'sent': 'SENT',
    'delivered': 'RECEIVED',
    'opened': "READ",
    'opened_unique': "READ_FIRST",
}


class MailerResponse(BaseResponse):
    @property
    def status(self):
        status = self.response.get("data").get("type")
        return STATUS_MAPPING.get(status)

    @property
    def status_date(self):
        return self.response.get("data").get("created_at")

    @property
    def notification_id(self):
        tag_list = self.response.get("data").get("email").get("tags")
        for tag in tag_list:
            if tag.startswith("NotificationId"):
                return tag.split("=")[1]
        return None

    @property
    def notification_receiver_id(self):
        tag_list = self.response.get("data").get("email").get("tags")
        for tag in tag_list:
            if tag.startswith("NotificationReceiverId"):
                return tag.split("=")[1]
        return None


class MailerSendService(BaseService):
    def send(self, to: dict | list[dict], subject: str, body: str, notification_id: str = None, notification_receiver_id: str = None, webhook_url: str = None) -> tuple[str, str]:
        mailer = emails.NewEmail()

        mail_body = {
            "tags": [
                f"NotificationId={notification_id}",
                f"NotificationReceiverId={notification_receiver_id}",
                f"WebhookUrl={webhook_url}",
            ]
        }

        mail_from = {
            "name": settings.FROM_EMAIL_NAME,
            "email": settings.FROM_EMAIL,
        }

        if isinstance(to, list):
            recipients = []
            for recipient in to:
                recipients.append({
                    "name": recipient["name"],
                    "email": recipient["email"],
                })
        else:
            recipients = [
                {
                    "name": to["name"],
                    "email": to["email"],
                }
            ]

        reply_to = {
            "name": settings.FROM_EMAIL_NAME,
            "email": settings.FROM_EMAIL,
        }

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject(subject, mail_body)
        mailer.set_html_content(body, mail_body)
        mailer.set_plaintext_content(parse_html(body), mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        request = requests.post(
            f"{mailer.api_base}/email", headers=mailer.headers_default, json=mail_body
        )
        message_id = request.headers.get("X-Message-Id")
        return message_id, request.text

    def get_response(self, response: dict) -> MailerResponse:
        return MailerResponse(response)
