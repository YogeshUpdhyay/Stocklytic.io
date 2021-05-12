from .. import mail
from flask_mail import Message
from flask import url_for

def send_reset_email(user):
    token = user.generate_reset_token()
    msg = Message('Password Reset Request',
                    sender="noreply@stokclytic.com",
                    recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('user.reset_password', token=token, _external=True)}'''
    mail.send(msg)