from pythonic import mail
from flask_mail import Message
from flask import url_for

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Pythonic - Reset your password", sender="adrenapoint@gmail.com",
    recipients=[user.email], 
    body= f'''To reset your password, please click the following link:
    {url_for('reset_password',token=token, _external=True)} 
    if you did not make this request, please ignore this email.'''
    )
    mail.send(msg)  