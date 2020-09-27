__author__ = 'khrystyna'
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import  DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post')
