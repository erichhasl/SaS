from django.core import mail
from django.conf import settings


NOT_SENT, SENT, PARTLY_SENT = 0, 1, 2


def send_from_arbeitsministerium(subject, content, recipients, reply_to=None):
    return send(subject, content, settings.EMAIL_ARBEITSMINISTERIUM, recipients,
                reply_to=reply_to,
                auth_user=settings.EMAIL_ARBEITSMINISTERIUM_USER,
                auth_password=settings.EMAIL_ARBEITSMINISTERIUM_PASSWORD)


def send_from_info(subject, content, recipients, reply_to=None):
    return send(subject, content, settings.EMAIL_INFO, recipients,
                reply_to=reply_to,
                auth_user=settings.EMAIL_INFO_USER,
                auth_password=settings.EMAIL_INFO_PASSWORD)


def send(subject, content, sender, recipients, reply_to=None,
         auth_user=None, auth_password=None):
    failed, succeeded = False, False
    if type(recipients) != list:
        recipients = [recipients]
    with mail.get_connection(username=auth_user, password=auth_password) as conn:
        for recipient in set(recipients):
            try:
                msg = mail.EmailMessage(subject, content, sender, recipients,
                                        reply_to=reply_to,
                                        connection=conn)
                msg.send()
            except Exception as e:
                print("Error when sending mail:", e)
                failed = True
            else:
                succeeded = True
    return NOT_SENT if failed and not succeeded else SENT if not failed\
        and succeeded else PARTLY_SENT
