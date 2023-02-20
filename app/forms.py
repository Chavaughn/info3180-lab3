from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=100)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[InputRequired(), Length(max=200)])
    message = TextAreaField('Message', validators=[InputRequired(), Length(max=1000)])
