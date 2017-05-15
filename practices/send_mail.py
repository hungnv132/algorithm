from django.core.mail import send_mail
import smtplib
from email.message import Message

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hnv132@gmail.com'
EMAIL_HOST_PASSWORD = 'ActionMan1324567*()'
EMAIL_USE_TLS = False

def send(subject, message, from_email, to_email):
    smtp = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    smtp.starttls()
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.sendmail(from_email, to_email, message)
    smtp.close()


subject = "This is a subject"
message = 'A big message'
from_email = "Hung <hnv1321@gmail.com>"
to_email = 'hungnv132@gmail.com'

send(subject, message, from_email, to_email)
print('fdfsds')

