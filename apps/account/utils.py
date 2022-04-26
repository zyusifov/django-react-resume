from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data, email_body):
        email = EmailMessage(subject="confirmation", body=data, to=[email_body])
        email.send()