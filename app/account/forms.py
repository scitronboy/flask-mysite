#account-related forms
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
    
class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    username = StringField('Username', validators=[Required(), Length(3, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must contain only letters, numbers, dots, or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('their is already an account with that same email.')
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username taken. please pick another')
    



