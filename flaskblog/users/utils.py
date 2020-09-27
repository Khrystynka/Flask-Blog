__author__ = 'khrystyna'
from flask import url_for
from flaskblog import mail
import secrets
from PIL import Image
import os
from flask_mail import Message
from flask import current_app




def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request',
                  sender=('example@demo.com'),
                  recipients=[user.email])
    msg.body = 'Hello'
    # msg.body = ' To reset your password, visit the following link:'+ \
    #            url_for('reset_token', token=token, _external = True)+'/n'+ \
    #            ' If you didn't make this request, please ignore this email'
    mail.send(msg)
