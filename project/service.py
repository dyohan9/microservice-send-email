import smtplib
from email.mime.text import MIMEText
from project import settings
from nameko.rpc import rpc


class Mail:
    name = 'mail'

    @rpc
    def send(self, to: list, subject: str, contents: str):
        msg = MIMEText(contents)
        msg['Subject'] = subject
        msg['From'] = settings.DEFAULT_FROM_EMAIL
        msg['To'] = ', '.join(to)

        server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.ehlo()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.DEFAULT_FROM_EMAIL, to, msg.as_string())
        server.quit()

        return True
